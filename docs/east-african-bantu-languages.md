# East African Bantu Languages - Data Availability & Inclusion

## Overview

This document provides comprehensive information about East African Bantu languages with **existing data resources** that can be integrated into the African Native Oral LLM framework.

## East African Bantu Language Groups

### 1. Northeast Bantu (Kenya, Tanzania, Uganda)

#### Kenyan Bantu Languages

| Language | ISO 639-3 | Family | Data Status | Primary Sources |
|----------|-----------|--------|-------------|-----------------|
| **Swahili** | swa | Northeast Coast | ✅ Extensive | KenCorpus, Helsinki Corpus, NLLB, CCAligned |
| **Kikuyu/Gikuyu** | kik | Thagicu | ✅ Available | Khaya AI, NLLB, GitHub translation datasets |
| **Kamba** | kam | Central | ✅ Available | NLLB, CCAligned, NLP Kenya |
| **Meru** | mer | Thagicu | ✅ Available | CCAligned, Khaya AI |
| **Embu** | emb | Thagicu | 🟡 Limited | Community sources |
| **Mbeere** | mbe | Thagicu | 🟡 Limited | Community sources |
| **Luhya (multiple)** | luy | Luhya | ✅ Available | KenCorpus (Lumarachi, Logooli, Lubukusu dialects) |
| **Kisii/Ekegusii** | eke | Luhya | ✅ Available | CCAligned, community data |
| **Kuria** | kuj | Luhya | 🟡 Limited | Community sources |
| **Suba** | sxb | Luhya | ✅ Available | Building African Voices dataset |
| **Maragoli/Logooli** | lrg | Luhya | ✅ Available | KenCorpus |
| **Lubukusu** | bxk | Luhya | ✅ Available | KenCorpus, POS tagged |
| **Taita** | dav | Taita | 🟡 Limited | Community sources |
| **Taveta** | ttv | Taita | ✅ Available | CCAligned, storybooks |
| **Pokomo** | pkb | Northeast Coast | ✅ Available | CCAligned, community data |

#### Ugandan Bantu Languages

| Language | ISO 639-3 | Family | Data Status | Primary Sources |
|----------|-----------|--------|-------------|-----------------|
| **Luganda** | lug | Luganda | ✅ Extensive | Luganda-NLP, Masakhane, parallel corpora, TTS models |
| **Kinyarwanda** | kin | Rwanda-Rundi | ✅ Available | Masakhane, NLLB, Kinyarwanda-NLP |
| **Kirundi** | run | Rwanda-Rundi | ✅ Available | NLLB, community data |
| **Ankole/Nkore** | nyn | Luganda | 🟡 Limited | Community sources |
| **Tooro** | ttj | Luganda | 🟡 Limited | Community sources |
| **Nyoro** | nyo | Luganda | 🟡 Limited | Community sources |
| **Soga** | xog | Luganda | ✅ Available | Community data, religious texts |
| **Gungu** | rub | Luganda | 🟡 Limited | Community sources |
| **Gwere** | gwr | Luganda | 🟡 Limited | Community sources |
| **Chiga** | cgg | Luganda | 🟡 Limited | Community sources |

#### Tanzanian Bantu Languages

| Language | ISO 639-3 | Family | Data Status | Primary Sources |
|----------|-----------|--------|-------------|-----------------|
| **Chaga** | kki | Chaga | 🟡 Limited | Community sources |
| **Pare** | asa | Pare | 🟡 Limited | Community sources |
| **Zigua** | ziw | Zigula | 🟡 Limited | Community sources |
| **Ngulu** | ngw | Zigula | 🟡 Limited | Community sources |
| **Shambala** | ksb | Shambala | ✅ Available | CCAligned, community data |
| **Bondei** | bou | Northeast Coast | 🟡 Limited | Community sources |
| **Ngasa** | nsg | Chaga | 🟡 Limited | Community sources |
| **Gogo** | gog | Central | ✅ Available | NLLB, community data |
| **Sukuma** | suk | Sukuma-Nyamwezi | ✅ Available | NLLB, CCAligned |
| **Nyamwezi** | nym | Sukuma-Nyamwezi | ✅ Available | NLLB, community data |
| **Kimbu** | kiv | Sukuma-Nyamwezi | 🟡 Limited | Community sources |
| **Nilamba** | nim | Sukuma-Nyamwezi | 🟡 Limited | Community sources |
| **Haya** | hay | Haya-Jita | ✅ Available | NLLB, community data |
| **Zinza** | zin | Haya-Jita | 🟡 Limited | Community sources |
| **Kerewe** | ked | Haya-Jita | 🟡 Limited | Community sources |
| **Jita** | jit | Haya-Jita | 🟡 Limited | Community sources |
| **Vinza** | vin | Haya-Jita | 🟡 Limited | Community sources |
| **Fipa** | fip | Fipa | 🟡 Limited | Community sources |
| **Mambwe** | mgr | Mambwe | 🟡 Limited | Community sources |
| **Nyiha** | nyh | Mambwe | 🟡 Limited | Community sources |
| **Malila** | mgu | Mambwe | 🟡 Limited | Community sources |
| **Lungu** | dne | Mambwe | 🟡 Limited | Community sources |
| **Makonde** | kde | Makonde | ✅ Available | Community data, NLLB |
| **Machinga** | mgh | Makonde | 🟡 Limited | Community sources |
| **Yao** | yao | Yao | ✅ Available | NLLB, community data |
| **Makua** | pma | Makua | ✅ Available | NLLB, community data |
| **Lomwe** | ngl | Makua | ✅ Available | NLLB, community data |

## Priority Languages for Immediate Inclusion

### Tier 1: Extensive Data Available (Ready for Immediate Training)

| Language | Data Sources | Est. Tokens | Est. Hours Audio |
|----------|---------------|-------------|------------------|
| Swahili | KenCorpus, Helsinki, NLLB, CC100 | 500M+ | 46+ hrs |
| Luganda | Luganda-NLP, Masakhane, Web | 50M+ | 5+ hrs |
| Kinyarwanda | NLLB, Kinyarwanda-NLP, Web | 30M+ | 3+ hrs |
| Kikuyu | Khaya, NLLB, CCAligned, GitHub | 5M+ | 2+ hrs |

### Tier 2: Moderate Data Available (Ready with Preprocessing)

| Language | Data Sources | Est. Tokens | Est. Hours Audio |
|----------|---------------|-------------|------------------|
| Kamba | NLLB, CCAligned, NLP Kenya | 2M+ | 1+ hrs |
| Luhya (Lubukusu) | KenCorpus | 2.2M | 58 hrs |
| Luhya (Logooli) | KenCorpus | Incl. above | Incl. above |
| Dholuo | KenCorpus, Building African Voices | 1.3M | 99 hrs |
| Sukuma | NLLB, CCAligned | 1M+ | 0.5+ hrs |
| Nyamwezi | NLLB | 500K+ | Limited |

### Tier 3: Limited but Growing Data

| Language | Data Sources | Est. Tokens | Est. Hours Audio |
|----------|---------------|-------------|------------------|
| Meru | CCAligned, Khaya | 500K+ | 0.5+ hrs |
| Suba | Building African Voices | 500K+ | 1+ hrs |
| Ekegusii | CCAligned | 300K+ | Limited |
| Embu | Community | 100K+ | Limited |
| Taita | Community | 50K+ | Limited |

## Language-Specific Documentation

### Swahili (Kiswahili)

**ISO 639-3**: swa  
**Speakers**: 200+ million (L1+L2)  
**Region**: Kenya, Tanzania, Uganda, DRC, Rwanda, Burundi, Mozambique, Comoros, Somalia  

**Data Resources**:
- **KenCorpus**: 1.8M words text, 46 hrs speech
- **Helsinki Corpus**: Extensive written Swahili
- **NLLB**: Parallel corpus with 200 languages
- **CC100**: Web-crawled monolingual corpus
- **CCAligned**: Cross-lingual web documents
- **Swahili Wikipedia**: 100K+ articles
- **Bible**: Parallel translations
- **JW.org**: Religious texts

**Special Considerations**:
- Tonal patterns are lexical but not written
- Extensive Arabic loanwords (15-20%)
- Multiple dialects (Kiunguja, Kimvita, Kipemba, etc.)
- Standard orthography established
- Roman script with special letters: ch, dh, gh, kh, ng', ny, sh, th

**Tokenizer Recommendations**:
```python
# Swahili-specific tokenizer settings
swahili_special_tokens = [
    "ch", "dh", "gh", "kh", "ng'", "ny", "sh", "th",
    "mw", "nd", "mb", "ng", "nj"
]
```

### Luganda

**ISO 639-3**: lug  
**Speakers**: ~8 million (Uganda)  
**Region**: Central Uganda, Buganda region  

**Data Resources**:
- **Luganda-NLP**: Community NLP project
- **Luganda TTS**: Text-to-speech models trained
- **Parallel Corpus**: Luganda-English (academic papers)
- **Gendered Corpus**: For bias research (ACL 2022)
- **Common Voice**: Mozilla speech dataset
- **Religious Texts**: Bible, Quran translations
- **News**: Bukedde newspaper archives

**Special Considerations**:
- Tone distinguishes meaning (must be captured in oral data)
- Vowel length contrastive
- Agglutinative morphology
- Roman script with standard orthography
- Extensive noun class system (15+ classes)

**Phonological Features**:
- High tone (´), Low tone (unmarked), Falling tone (^)
- Example: `mu-limi` (farmer) vs `mu-lími` (in the garden)

**Tokenizer Recommendations**:
```python
# Luganda-specific tokenizer settings
luganda_prefixes = [
    "mu", "ba", "lu", "bu", "gu", "ku", "tu", "lu", "n",
    "a", "o", "e", "i", "u"
]
```

### Kikuyu/Gikuyu

**ISO 639-3**: kik  
**Speakers**: ~6.6 million (Kenya)  
**Region**: Central Kenya (Mt. Kenya region)  

**Data Resources**:
- **Khaya AI**: Translation dataset and models
- **GitHub Translation**: Kikuyu-Swahili parallel corpus
- **NLLB**: Meta's No Language Left Behind
- **CCAligned**: Web documents
- **Storybooks**: African Storybook Initiative
- **Community Data**: Khaya app contributions

**Special Considerations**:
- Two main dialects: Kikuyu proper vs Southern Gikuyu
- Implosive consonants: /ɓ/, /ɗ/
- Prenasalized stops: mb, nd, ng, nj
- Tone system (High, Low, Falling)
- Roman script

**Phonological Features**:
- Implosives: `b` vs `ɓ`, `d` vs `ɗ`
- Prenasalization: `mb`, `nd`, `ng`, `nj`
- Vowel reduction in unstressed positions

### Kinyarwanda

**ISO 639-3**: kin  
**Speakers**: ~12 million (Rwanda, DRC, Uganda, Burundi)  
**Region**: Rwanda (official language)  

**Data Resources**:
- **NLLB**: Parallel corpus
- **Kinyarwanda-NLP**: GitHub repositories
- **Masakhane**: Community translation project
- **Luganda-Kinyarwanda**: Cross-lingual models
- **Government Documents**: Rwanda open data
- **Igihe.com**: News corpus
- **Religious Texts**: Bible, Quran

**Special Considerations**:
- Mutually intelligible with Kirundi
- Tone language (tone distinguishes meaning)
- Complex verbal morphology
- Roman script standardized
- Post-genocide language revitalization efforts

**Phonological Features**:
- High tone marked with acute accent: `´`
- Contrastive vowel length
- Palatalized consonants

### Kamba

**ISO 639-3**: kam  
**Speakers**: ~4 million (Kenya)  
**Region**: Eastern Kenya (Machakos, Kitui, Makueni)  

**Data Resources**:
- **NLLB**: Included in Meta's dataset
- **CCAligned**: Web documents
- **NLP Kenya**: Academic research data
- **Storybooks**: African Storybook Initiative
- **Community collections**: Oral histories

**Special Considerations**:
- Related to Kikuyu (similar phonology)
- Prenasalized consonants
- Tone system
- Roman script
- Lower resource than Kikuyu but growing

### Luhya Languages

**ISO 639-3**: luy (macrolanguage)  
**Speakers**: ~6-7 million (Kenya)  
**Region**: Western Kenya  

**Major Dialects with Data**:
1. **Lubukusu** (bxk): ~1.3M speakers
   - KenCorpus: 2.2M words, POS tagged
   - 58 hours audio
   - Maseno University resources

2. **Logooli/Maragoli** (lrg): ~600K speakers
   - KenCorpus included
   - Oral tradition rich

3. **Lumarachi**: 
   - KenCorpus included
   - Part of larger Luhya collection

**Special Considerations**:
- Macro-language with 15+ varieties
- Some mutual intelligibility between dialects
- Roman script used
- Rich oral tradition (folktales, proverbs)
- Tone systems vary by dialect

### Sukuma

**ISO 639-3**: suk  
**Speakers**: ~5.4 million (Tanzania)  
**Region**: Mwanza, Shinyanga, Geita regions  

**Data Resources**:
- **NLLB**: Parallel corpus
- **CCAligned**: Web documents
- **Community**: Growing language technology community
- **Oral traditions**: Rich storytelling tradition

**Special Considerations**:
- Closely related to Nyamwezi
- Roman script
- Prenasalized consonants
- Tone system
- Significant oral literature corpus

## Data Source Details

### 1. KenCorpus (Kenyan Languages Corpus)

**URL**: https://kencorpus.maseno.ac.ke/corpus-datasets/  
**Maintainer**: Maseno University  
**License**: Academic/Research  

**Contents**:
- Swahili: 2,585 texts (~1.8M words), 19 hrs speech
- Dholuo: 546 texts (~1.3M words), 99 hrs speech
- Luhya: 987 texts (~2.2M words), 58 hrs speech
- POS tagged: 50K words (Dholuo), 90K words (Luhya)

**Access**: Registration required  
**Format**: Text, Audio, POS annotations

### 2. Building African Voices

**URL**: https://www.africanvoices.tech/  
**Maintainer**: African Voices Lab  
**License**: Open (CC-BY)  

**Contents**:
- 16 African languages
- Kenyan: Dholuo (13,897 utterances), Suba (2,078), Kenyan English (1,150)
- Sources: Books, websites, social media

**Format**: Text + Speech pairs

### 3. NLLB (No Language Left Behind)

**URL**: https://github.com/facebookresearch/fairseq/tree/nllb  
**Maintainer**: Meta AI  
**License**: CC-BY-SA 4.0  

**Contents**:
- 200 languages including:
  - Swahili, Kikuyu, Kamba, Dholuo, Luhya
  - Luganda, Kinyarwanda, Kirundi, Runyankore
  - Sukuma, Nyamwezi, Gogo, Haya
  - Yao, Makonde, Makua, Lomwe
  - Many others

**Format**: Parallel text (sentence-aligned)

### 4. CCAligned & CC100

**URL**: https://github.com/facebookresearch/cc_net  
**Maintainer**: Meta AI  
**License**: Open  

**Contents**:
- Web-crawled monolingual text
- Multiple East African Bantu languages
- Kenya: Swahili, Kikuyu, Dholuo, Kamba, Ekegusii, Luhya
- Tanzania: Sukuma, Nyamwezi, Haya, Swahili
- Uganda: Luganda, Kinyarwanda, Runyankore

**Format**: Cleaned web text

### 5. Masakhane

**URL**: https://www.masakhane.io/  
**Maintainer**: African NLP Community  
**License**: Various (mostly open)  

**Contents**:
- Machine translation datasets
- Luganda, Kinyarwanda participation
- Community-contributed parallel corpora

### 6. Luganda-NLP

**URL**: https://k4all.org/project/luganda-language/  
**Maintainer**: Knowledge for All  
**License**: Open  

**Contents**:
- Luganda corpus
- TTS models
- Translation systems
- Gender bias research corpus

### 7. Khaya AI

**URL**: https://khaya.africa/  
**Maintainer**: Ghana NLP (expanded to Kenya)  
**License**: Commercial/Research  

**Contents**:
- Translation models: Kikuyu, Kamba, Meru, Luo
- Mobile app data collection
- Growing datasets through user contributions

### 8. African Storybook Initiative

**URL**: https://www.africanstorybook.org/  
**Maintainer**: Saide  
**License**: CC-BY  

**Contents**:
- Children's stories in multiple languages
- Kikuyu, Kamba, Ekegusii, Luhya, Dholuo, Swahili
- Simple language, good for training

### 9. Common Voice (Mozilla)

**URL**: https://commonvoice.mozilla.org/  
**Maintainer**: Mozilla  
**License**: CC0 (Public Domain)  

**Contents**:
- Crowdsourced speech dataset
- Swahili: Extensive validation
- Luganda: Growing dataset
- Kinyarwanda: Available

### 10. Bible & Religious Texts

**Sources**:
- Bible.com (YouVersion API)
- JW.org (Jehovah's Witnesses)
- Islamic texts

**Languages**: Most major East African Bantu languages
**Format**: Parallel translations available
**License**: Generally open for research

## Integration Roadmap

### Phase 1: Immediate (Ready to Integrate Now)

1. **Swahili**
   - Load Helsinki Corpus
   - Add KenCorpus
   - Integrate CC100 Swahili
   - Status: Can train 1B+ token model immediately

2. **Luganda**
   - Contact Luganda-NLP for corpus access
   - Integrate Masakhane MT data
   - Add Common Voice speech
   - Status: Can train 100M+ token model

3. **Kinyarwanda**
   - Download NLLB parallel data
   - Integrate GitHub community data
   - Add Common Voice
   - Status: Can train 50M+ token model

### Phase 2: Short-term (3-6 months)

1. **Kikuyu**
   - Download Khaya datasets
   - Integrate GitHub translation corpus
   - Collect oral traditions from communities
   - Target: 20M+ token model

2. **Luhya (Lubukusu)**
   - Request KenCorpus access
   - Focus on oral tradition collection
   - Target: 10M+ token model

3. **Dholuo**
   - Access KenCorpus
   - Note: Nilotic (not Bantu) but included for regional completeness
   - Target: 15M+ token model

4. **Kamba**
   - Extract from NLLB
   - Community data collection
   - Target: 5M+ token model

### Phase 3: Medium-term (6-12 months)

1. **Sukuma, Nyamwezi**
   - Extract from NLLB
   - Tanzania community partnerships
   - Target: 2M+ token models

2. **Meru, Embu**
   - Community data collection
   - Close relationship to Kikuyu
   - Target: 1M+ token models

3. **Other Tier 3 languages**
   - Community-driven collection
   - Oral tradition focus
   - Target: 500K+ token baseline

## Technical Integration Notes

### Text Preprocessing

```python
# East African Bantu language preprocessor
class EastAfricanBantuNormalizer:
    """
    Normalizer for East African Bantu languages.
    Handles prenasalization, tone marks, and dialect variation.
    """
    
    PRENASALIZED = ['mb', 'nd', 'ng', 'nj', 'nz', 'mv', 'nv']
    
    TONE_MARKS = {
        '\u0301': 'HIGH',    # acute
        '\u0300': 'LOW',     # grave
        '\u0302': 'FALLING', # circumflex
        '\u0304': 'MID',     # macron
    }
    
    def normalize(self, text, language_code):
        # Language-specific rules
        if language_code in ['kik', 'mer', 'emb', 'kam']:
            # Thagicu group - handle prenasalization
            text = self._normalize_prenasalized(text)
        
        if language_code in ['lug', 'kin', 'run']:
            # Luganda/Rwanda-Rundi - preserve tone marks
            text = self._preserve_tones(text)
        
        return text
```

### Tokenization Strategy

For East African Bantu languages, we recommend:

1. **Byte-Pair Encoding (BPE)** with language-specific seeds
2. **Special tokens** for:
   - Prenasalized consonants (mb, nd, ng, nj)
   - Common affixes (mu-, ba-, ki-, i-, u-)
   - Tone combinations (for tonal languages)

```python
# Example tokenizer configuration
tokenizer_config = {
    'swa': {
        'special_tokens': ['ch', 'dh', 'gh', 'kh', "ng'", 'ny', 'sh', 'th'],
        'prefixes': ['ku', 'wa', 'mw', 'mi', 'ma', 'ki', 'vi'],
    },
    'kik': {
        'special_tokens': ['mb', 'nd', 'ng', 'nj', 'ng\'', 'ny', 'th'],
        'prefixes': ['mu', 'wa', 'mi', 'ma', 'ki', 'i', 'u'],
    },
    'lug': {
        'special_tokens': ['mb', 'nd', 'ng', 'nj', 'ny', 'ng\'', 'gy', 'ky'],
        'prefixes': ['mu', 'ba', 'lu', 'bu', 'gu', 'ku', 'tu'],
        'tone_aware': True,
    }
}
```

### Speech Processing

East African Bantu languages share phonological features requiring:

1. **Prenasalization detection** in audio
2. **Tone contour extraction** for tonal languages
3. **Vowel length modeling** for Luganda, Kinyarwanda
4. **Implosive detection** for Kikuyu, related languages

## Ethical Considerations

### Data Sovereignty
- Partner with **Maseno University** for KenCorpus languages
- Collaborate with **Kampala Language Communities** for Luganda
- Work with **Rwanda Language Academy** for Kinyarwanda
- Engage **Tanzanian language institutes** for Sukuma, Nyamwezi

### Community Benefit
- Prioritize languages with active community technology groups
- Share models back to communities
- Support local NLP capacity building
- Include language stewards in governance

### Attribution Requirements
- Acknowledge KenCorpus (Maseno University)
- Credit Masakhane contributors
- Recognize Khaya AI community contributions
- Honor oral tradition keepers by name (with permission)

## References

1. Wanjawa et al. (2023). *KenCorpus: A Kenyan Language Corpus for Machine Learning*
2. Ogayo et al. (2022). *Building African Voices*
3. Costa-jussà et al. (2022). *No Language Left Behind*
4. Luganda-NLP Project: https://k4all.org/project/luganda-language/
5. Masakhane MT: https://www.masakhane.io/
6. Khaya AI: https://khaya.africa/

---

**Last Updated**: May 2026  
**Contributors**: African Native Oral LLM Research Team  
**Contact**: research@african-native-oral-llm.org
