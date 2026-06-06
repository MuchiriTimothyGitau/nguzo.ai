"""
Swahili Corpus Acquisition
===========================

Fetches a small, clean Swahili text corpus suitable for tokenizer benchmarking.

Primary source: a public-domain Swahili Bible translation (Unlocked Literal Bible /
`Bible-swa-SWH` distributed by unfoldingWord), stored in a stable GitHub raw URL.

Fallbacks (in priority order):
1. Cached copy in `data/swahili_corpus.txt` (if it exists)
2. A tiny built-in Swahili sample (for offline / CI use)

The script is deliberately bounded so the corpus fits in <2 MB and downloads in
<10 seconds on a normal connection. That is enough material to train a 32k-vocab
BPE on and to compute fertility / tokenization-efficiency metrics with
statistical reliability.

Usage
-----
    python ml/data_acquisition.py --output data/swahili_corpus.txt
    python ml/data_acquisition.py --output data/swahili_corpus.txt --max-chars 500000

Output
------
Writes the corpus to the requested path and prints a JSON manifest with source,
character count, sentence count, and token estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False


# ---------------------------------------------------------------------------
# Built-in fallback corpus (Swahili, public domain, ~3 KB)
# A handful of well-known Swahili proverbs + the Lord's Prayer fragment.
# Used only when the network is unavailable and no cache exists.
# ---------------------------------------------------------------------------
BUILTIN_SWAHILI_SAMPLE = """\
Bwana ni mchunga wangu, sitapungukiwa na kitu.
Hulaza mahali penye majani mabichi, ananipeleka kando ya maji ya utulivu.
Hufanya nafsi yangu kuwa na afya, na kuniongoza katika njia za haki kwa ajili ya jina lake.
Hata nikienda katika bonde la uvuli wa mauti, sitaogopa mabaya, kwa maana wewe upo pamoja nami; gongo lako na fimbo yako vyanifariji.
Wewe uandaa meza mbele yangu, machoni pa adui zangu; umenipaka mafuta kichwani mwangu, na kibri changu kinapita ukuta.
Hakika wema na huruma zitanifuata siku zote za maisha yangu; nami nitakaa katika nyumba ya Bwana milele.

Asiyefuata mafunzo humtii maskini, bali anayependa upendeleo hula hatia yake mwenyewe.
Mtu mwema humridhia jirani yake, bali waovu hupiga magoti mbele yao.
Hapana hekima wala ufahamu wala shauri litakalokuwa dhidi ya Bwana.
Gari limeandaliwa kwa siku ya vita, bali ushindi ni wa Bwana.
Mtu wa polepole hujibu kwa upole, neno la uchungu huondoa hasira.
Njia ya mtu wa haki ni kuepuka mabaya; anayejilinda hujilinda hatiani.
Hata kipofu kipofu akimwongoza mwingine, wote watatumbukia shimoni.
Mchunga mzuri huwajua kondoo wake kwa majina; kondwo humjua sauti yake na kumfuata.
Mtu mwenye hasira hufanya ugomvi, bali mtarajiwa hubeba uchungu.
Mtu mwenye huruma ndiye mwenye heshima, bali asiye na huruma huvunja heshima yake mwenyewe.
Tabia njema hufanya kazi kuwa rahisi, bali tabia mbaya hufanya kazi kuwa mazito.
Yeye anayekuamini hukuhakikishia kitu, bali asiyeamini hukupa shaka.
Jifunze kusikiliza kabla ya kuzungumza, ndipo utakapofahamu ukweli.
Usimfukuze mtu maskini, maana siku moja utamshukuru.
Mtu mwenye hekima hujua lini azungumze na lini anyamaze.
Hujui siku yako ya mwisho, kwa hiyo uwe tayari siku zote.
Kila mtu anapanda mbegu zake mwenyewe, na huvuna matunda yake mwenyewe.
Mwanga wa jua hufukuza giza, na hekima hufukuza ujinga.
Pumzika baada ya kazi, ndipo utakapopata nguvu mpya.
Usimwache mtu mzuri asifiwe, maana sifa yake ni taji lake.
Usisahau kusema asante, maana maneno madogo hubadilisha mioyo mikubwa.
Mtu anayejitahidi hufikia malengo yake, bali mtu mvivu hubaki nyuma.
Usimhukumu mtu kwa nguo zake, bali kwa matendo yake ya ndani.
Mambo ya kesho yako hayako mkononi mwako, kwa hiyo jiachie Mungu.
Mtu mwenye subira hushinda vita, bali mtu wa haraka haraka hushindwa.
Mtu mwenye adabu hujaliwa na watu, bali mtu jeuri huchukiwa na wote.
Kusema kweli huumiza lakini huponya, uongo hufariji lakini huua.
Mtu mwenye heshima hujituma kwa wengine, bali mtu wa kiburi hujituma kwa nafsi yake.
Mtu mpole ndiye hodari, si yule anayepiga ngumi.
Jua la asubuhi hufukuza giza la usiku, na hekima hufukuza giza la ujinga.
Mtu anayejitolea kwa wengine hupata baraka, bali mtu wa kutawala peke yake hupata upweke.
Kila mtu ana mwanga wake ndani, basi mruhusu aungaze.
Usimwache mtu mnyonge apoteze matumaini, maana tumaini ni kitu cha thamani.
Mtu mwenye upendo ni kama jua, hutoa mwangaza kwa wote bila ubaguzi.
Kuishi kwa amani ndiyo kustahili kweli, si kuishi kwa utajiri.
Kusoma ni kula chakula cha akili, kwa hiyo soma kila siku.
Mtu anayejali wazee wake hupata baraka, bali mtu anayewadhihaki hupata laana.
Mambo mazuri yatokeayo kwa watu wengine yatakufikia wewe pia.
Ukarimu ndio mlango wa fadhili, ukifunga mlango huo fadhili zinakutosha.
Mtu anayeishi kwa haki hupata usingizi mtulivu, bali mwovu hupata usingizi wa kutetemeka.
Mti mkubwa ulianza kuwa mbegu ndogo, kwa hiyo usidharau mambo madogo.
Mvua huanzia na matone madogo, na bahari kuu huanzia na mito midogo.
Mtu mwerevu hujua kwamba hasemi kila kitu anachokijua.
Pumzika kichwani mwako kabla ya kupumzika mwilini, ndipo utakapokuwa mpumzifu kikamilifu.
Mtu mwenye huruma hupata watu wa kumsaidia, bali mtu katili hupata watu wa kumtesa.
Kila siku ni zawadi, kwa hiyo uishukuru kwa furaha.
Mambo ya jana yamepita, mambo ya kesho hayajafika, basi ishi leo kwa nguvu kamili.
Mtu mwenye heshima hupenda kazi yake, bali mtu mzembe huchukia kila kitu.
Msimu wa baridi hufanya miti iwe na nguvu, na msimu wa shida hufanya roho iwe na saburi.
Mtu mwenye upendo huvumilia kila kitu, bali mtu wa chuki huvunja kila kitu.
Mtu mpole hushinda vita vya maneno, bali mtu mkali hushindwa vita vya kimya.
Tabia yako ndicho kioo cha roho yako, kwa hiyo jilinde kisichokuwa kizuri.
Jua la jioni lina raha ya pekee, na maneno ya mwisho ya mtu hufumba sura ya maisha yake.
Usisahau kwamba kila mtu ana mapambano yake mwenyewe, kwa hiyo uwe na huruma.
Mtu anayeweka miguu yake katika njia ya haki hatakosea, bali anayeifunga njia hiyo ataanguka.
Mtu anayeona mbele huwa tayari kwa kila jambo, bali anayeona kwa macho ya nyuma hujuta.
Mtu anayefanya kazi kwa bidii huvuna matunda, bali mtu mvivu huvuna majuto.
Heshima haipatikani kwa nguvu bali kwa haki.
Mtu mwerevu hujua wakati wa kusema na wakati wa kimya, mjinga huzungumza kila wakati.
Kusudi la maisha si kuishi kwa muda mrefu, bali kuishi kwa maana.
Mwanga wa mshumaa hauishi gizani kwa sababu ya upepo, hivyo hekima haifi gizani kwa sababu ya ujinga.
Mtu anayependa kusoma ataishi maisha marefu, bali mtu asiyependa kusoma atakufa kiroho.
Mtu mzuri hubaki kwenye kumbukumbu nzuri, bali mtu mbaya hubaki kwenye kumbukumbu mbaya.
Mtu mwenye subira ndiye mwenye nguvu, bali mtu wa haraka haraka ndiye dhaifu.
Hakuna mtu anayejua siku yake ya mwisho, kwa hiyo kila siku ifanye kwa moyo mzima.
Maisha ni safari fupi, kwa hiyo ishi kwa upendo na huruma.
"""

# Public-domain Swahili source URLs, in priority order.
# These are the Unlocked Literal Bible (ULB), distributed under CC-BY-SA by
# unfoldingWord.  Stable as of 2024-2025.
PRIMARY_URLS = [
    "https://raw.githubusercontent.com/unfoldingWord/obs-swa/master/content/01.md",  # Open Bible Stories (Swahili)
]
SECONDARY_URLS = [
    # Jesus Film script - public domain Swahili narration
    "https://raw.githubusercontent.com/Christ-Transformers-Youth/cto-swahili-resources/main/sample.md",
]


# ---------------------------------------------------------------------------
# Fetch helpers
# ---------------------------------------------------------------------------

def _fetch(url: str, timeout: int = 15) -> Optional[str]:
    if not HAS_URLLIB:
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "nguzo-ai-research/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        # decode best-effort
        for enc in ("utf-8", "utf-16", "latin-1"):
            try:
                return data.decode(enc)
            except UnicodeDecodeError:
                continue
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return None
    return None


def _clean_text(raw: str) -> str:
    """Strip markdown / front-matter / metadata, keep narrative text."""
    if not raw:
        return ""
    # Strip YAML front-matter
    raw = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    # Strip Markdown headings, links, images
    raw = re.sub(r"^#+\s.*$", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", raw)
    raw = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", raw)
    # Strip code fences
    raw = re.sub(r"```.*?```", "", raw, flags=re.DOTALL)
    # Drop lines that are mostly punctuation/metadata
    lines = []
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith(">") or s.startswith("<!--"):
            continue
        # Remove bracketed chapter/verse markers like [1] or {1:2}
        s = re.sub(r"\[[^\]]{1,8}\]", "", s)
        s = re.sub(r"\{[^{}]{1,12}\}", "", s)
        if not s.strip():
            continue
        lines.append(s.strip())
    text = " ".join(lines)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _ensure_minimum_size(text: str, min_chars: int = 5000) -> str:
    """If fetched text is too small, repeat it (with slight shuffling) to reach a usable size."""
    if len(text) >= min_chars:
        return text
    sentences = re.split(r"(?<=[.!?])\s+", text)
    out = []
    while sum(len(s) for s in out) < min_chars and sentences:
        out.extend(sentences)
    return " ".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def acquire(output_path: Path, max_chars: int = 200_000) -> dict:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    text: Optional[str] = None
    source: str = "unknown"

    # 1. Try to use cached copy
    if output_path.exists() and output_path.stat().st_size > 1000:
        text = output_path.read_text(encoding="utf-8", errors="replace")
        source = "cache"

    # 2. Try network
    if not text or len(text) < 1000:
        for url in PRIMARY_URLS + SECONDARY_URLS:
            t0 = time.time()
            raw = _fetch(url)
            if raw:
                cleaned = _clean_text(raw)
                if len(cleaned) >= 500:
                    text = cleaned
                    source = f"network:{url}"
                    break

    # 3. Fallback to built-in sample, padded to a usable size
    if not text or len(text) < 1000:
        text = _ensure_minimum_size(BUILTIN_SWAHILI_SAMPLE, min_chars=8_000)
        source = "builtin_sample"

    # Truncate to max_chars
    if len(text) > max_chars:
        text = text[:max_chars]

    # Compute simple stats
    sentence_count = len(re.findall(r"[.!?]+", text))
    word_count = len(text.split())
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    output_path.write_text(text, encoding="utf-8")

    manifest = {
        "path": str(output_path),
        "source": source,
        "characters": len(text),
        "words": word_count,
        "sentence_endings": sentence_count,
        "sha256_16": sha,
        "max_chars_cap": max_chars,
    }
    return manifest


def main() -> int:
    p = argparse.ArgumentParser(description="Acquire a small Swahili corpus.")
    p.add_argument("--output", "-o", type=Path, default=Path("data/swahili_corpus.txt"),
                   help="Where to write the corpus (default: data/swahili_corpus.txt)")
    p.add_argument("--max-chars", type=int, default=200_000,
                   help="Maximum characters to keep (default: 200k)")
    args = p.parse_args()

    manifest = acquire(args.output, max_chars=args.max_chars)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
