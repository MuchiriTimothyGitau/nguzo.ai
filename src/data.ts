export interface Language {
  code: string;
  name: string;
  family: string;
  region: string;
  script: "Latin" | "Ge'ez" | "Arabic" | "Latin/Ajami";
  flag: string;
  status: string;
}

export interface MedicalPhrase {
  id: string;
  category: "symptoms" | "body_parts" | "instructions" | "emergencies";
  english: string;
  translations: Record<string, { text: string; transliteration: string }>;
}

export interface Flashcard {
  id: string;
  language: string;
  front: string;
  back: string;
  category: string;
}

export const LANGUAGES: Language[] = [
  {
    code: "sw",
    name: "Swahili",
    family: "Bantu (Niger-Congo)",
    region: "East & Central Africa (Kenya, Tanzania, Uganda, DRC)",
    script: "Latin",
    flag: "🇰🇪",
    status: "Primary Anchor - 200M+ Speakers"
  },
  {
    code: "am",
    name: "Amharic",
    family: "Semitic (Afroasiatic)",
    region: "Ethiopia",
    script: "Ge'ez",
    flag: "🇪🇹",
    status: "High Priority Pair - 50M+ Speakers"
  },
  {
    code: "yo",
    name: "Yoruba",
    family: "Defoid (Niger-Congo)",
    region: "Nigeria, Benin, Togo",
    script: "Latin",
    flag: "🇳🇬",
    status: "Tonal Register - 45M+ Speakers"
  },
  {
    code: "ha",
    name: "Hausa",
    family: "Chadic (Afroasiatic)",
    region: "West Africa (Nigeria, Niger, Ghana)",
    script: "Latin/Ajami",
    flag: "🇳🇪",
    status: "Broad Trade Language - 80M+ Speakers"
  },
  {
    code: "xh",
    name: "Xhosa",
    family: "Bantu (Niger-Congo)",
    region: "South Africa, Lesotho",
    script: "Latin",
    flag: "🇿🇦",
    status: "Click Accents - 10M+ Speakers"
  }
];

export const MEDICAL_PHRASES: MedicalPhrase[] = [
  {
    id: "m1",
    category: "symptoms",
    english: "Please point to where you feel the pain.",
    translations: {
      sw: { text: "Tafadhali onyesha wapi unapohisi maumivu.", transliteration: "tah-fah-dah-lee oh-nyeh-shah wah-pee oo-nah-poh-hee-see mah-oo-mee-voo" },
      am: { text: "እባክዎን ሕመሙ የት እንደሆነ ያመልክቱ።", transliteration: "uh-bahk-wohn huh-meh-moo yet uhn-deh-hohn yah-mehl-k-too" },
      yo: { text: "Ẹ jọ̀ọ́, tọ́ka sí ibi tí ebi ti ń dun yín.", transliteration: "eh jaw-or, taw-kah see ee-bee tee eh-bee tee n doon yeen" },
      ha: { text: "Don Allah nuna min inda ke ciwo.", transliteration: "dohn ahl-lah noo-nah meen een-dah keh chee-woh" },
      xh: { text: "Khawuncede ubonise apho uva khona intlungu.", transliteration: "kah-woon-cheh-deh oo-boh-nee-seh ah-poh oo-vah koh-nah een-tloon-goo" }
    }
  },
  {
    id: "m2",
    category: "symptoms",
    english: "How many days have you had this fever?",
    translations: {
      sw: { text: "Je, una homa hii kwa siku ngapi?", transliteration: "jeh, oo-nah hoh-mah hee kwah see-koo ngah-pee" },
      am: { text: "ይህ ትኩሳት ለስንት ቀናት ቆይቷል?", transliteration: "yeeh tuh-koo-saht luh-suhnt k'uh-naht k'oy-twahl" },
      yo: { text: "Ọjọ́ mélòó ni ibà yí ti bẹ̀rẹ̀?", transliteration: "aw-jaw meh-loh nee ee-bah yee tee beh-reh" },
      ha: { text: "Kwanaki nawa ka yi da wannan zazzabi?", transliteration: "kwah-nah-kee nah-wah kah yee dah wahn-nahn zahz-zah-bee" },
      xh: { text: "Zintsuku zongaphi unale fiva?", transliteration: "zeen-tsoo-koo zohn-gah-pee oo-nah-leh fee-vah" }
    }
  },
  {
    id: "m3",
    category: "body_parts",
    english: "Does your chest or heart feel heavy?",
    translations: {
      sw: { text: "Je, kifua chako au moyo unahisi uzito?", transliteration: "jeh, kee-foo-ah chah-koh ah-oo moh-yoh oo-nah-hee-see oo-zee-toh" },
      am: { text: "ደረትዎ ወይም ልብዎ ይከብድዎታል?", transliteration: "deh-reht-woh wehy-m lihb-woh yee-kehbd-woh-tahl" },
      yo: { text: "Ǹjẹ́ àyà rẹ tàbí ọkàn rẹ ń nira?", transliteration: "n-jeh ah-yah reh tah-bee aw-kahn reh n nee-rah" },
      ha: { text: "Kirjinka ko zuciyarka tana jin nauyi?", transliteration: "keer-jeen-kah koh zoo-chee-yahr-kah tah-nah jeen now-yee" },
      xh: { text: "Ingaba isifuba sakho okanye intliziyo yakho iziva inzima?", transliteration: "eeng-ah-bah ee-see-foo-bah sah-koh oh-kahn-yeh een-tlee-zee-yoh yah-koh ee-zee-vah een-zee-mah" }
    }
  },
  {
    id: "m4",
    category: "instructions",
    english: "Take this medicine three times a day after meals.",
    translations: {
      sw: { text: "Kunywa dawa hii mara tatu kwa siku baada ya chakula.", transliteration: "koo-nywah dah-wah hee mah-rah tah-too kwah see-koo bah-ah-dah yah chah-koo-lah" },
      am: { text: "ይህን መድኃኒት ከምግብ በኋላ በቀን ሦስት ጊዜ ይውሰዱ።", transliteration: "yeeh-n mih-dah-neet kh-mih-gb-bwah-lah b-k'uhn sohst gee-zee yee-wuh-seh-doo" },
      yo: { text: "Gba oògùn yìí lẹ́mẹ̀ta lójúmọ́ lẹ́yìn oúnjẹ.", transliteration: "gbah oh-goon yee leh-meh-tah loh-joo-maw leh-yeen ohn-jeh" },
      ha: { text: "Sha wannan magani sau uku a rana bayan kin ci abinci.", transliteration: "shah wahn-nahn mah-gah-nee sow oo-koo ah rah-nah bah-yahn keen chee ah-been-chee" },
      xh: { text: "Thatha eli yeza kathathu ngemini emva kokutya.", transliteration: "tah-tah eh-lee yeh-zah kah-tah-too ngeh-mee-nee ehm-vah koh-koo-tyah" }
    }
  },
  {
    id: "m5",
    category: "instructions",
    english: "Rest and drink plenty of warm water.",
    translations: {
      sw: { text: "Pumzika na unywe maji mengi ya joto.", transliteration: "poom-zee-kah nah oo-nyweh mah-jee mehn-gee yah joh-toh" },
      am: { text: "እረፍት ያድርጉ እና ብዙ የሞቀ ውሃ ይጠጡ።", transliteration: "uh-rehft yah-dr-goo-nah bih-zoo yuh-mokh-wh-wh-yee-t'u-t'oo" },
      yo: { text: "Sinmi kí o sì mu omi gbóná púpọ̀.", transliteration: "seen-mee kee oh see moo oh-mee gbaw-nah poo-paw" },
      ha: { text: "Huta ka sha ruwan dumi mai yawa.", transliteration: "hoo-tah kah shah roo-wahn doo-mee my yah-wah" },
      xh: { text: "Phumla kwaye usele amanzi amaninzi afudumeleyo.", transliteration: "poom-lah kwah-yeh oo-seh-leh ah-mahn-zee ah-mah-neen-zee ah-foo-doo-meh-leh-yoh" }
    }
  },
  {
    id: "m6",
    category: "emergencies",
    english: "This is an emergency. We are taking you to the clinic now.",
    translations: {
      sw: { text: "Hii ni dharura. Tunakupeleka kliniki sasa hivi.", transliteration: "hee nee dah-roo-rah. too-nah-koo-peh-leh-kah klee-nee-kee sah-sah hee-vee" },
      am: { text: "ይህ ድንገተኛ አደጋ ነው። አሁን ወደ ክሊኒክ እንወስድዎታለን።", transliteration: "yeeh dihn-geh-teh-nyah ah-deh-gah n-wuh. ah-hoon wuh-deh klee-neek n-wuh-seh-dwuh-tah-lehn" },
      yo: { text: "Pàjáwìrì ni èyí. A ń mu ọ lọ sí ilé-ìwòsàn nísinsìnyí.", transliteration: "pah-jah-wee-ree nee eh-yee. ah n moo aw law see ee-leh-ee-woh-sahn nee-seen-seen-yee" },
      ha: { text: "Wannan babban gaggawa ne. Muna kaimu asibiti yanzu.", transliteration: "wahn-nahn bahb-bahn gahg-gah-wah neh. moo-nah ky-moo ah-see-bee-tee yahn-zoo" },
      xh: { text: "Ezi ziime ezikhawulezileyo. Siyakumsa ekliniki ngoku.", transliteration: "eh-zee zeey-meh eh-zee-kah-woo-leh-zee-leh-yoh. see-yah-koom-sah eh-klee-nee-kee ngoh-koo" }
    }
  }
];

export const FLASHCARDS: Flashcard[] = [
  { id: "f1", language: "sw", front: "Umoja", back: "Unity (The foundational pillar of community solidarity)", category: "Nguzo Pillars" },
  { id: "f2", language: "sw", front: "Kujichagulia", back: "Self-Determination (To define, name, and speak for ourselves)", category: "Nguzo Pillars" },
  { id: "f3", language: "sw", front: "Ujima", back: "Collective Work and Responsibility (Building community together)", category: "Nguzo Pillars" },
  { id: "f4", language: "sw", front: "Ujamaa", back: "Cooperative Economics (Shared wealth and supporting local business)", category: "Nguzo Pillars" },
  { id: "f5", language: "am", front: "ሰላም (Selam)", back: "Peace / Common Greeting of well-being", category: "Greetings" },
  { id: "f6", language: "am", front: "አመሰግናለሁ (Ameseginalehu)", back: "Thank you very much (Exhibiting high gratitude)", category: "Social" },
  { id: "f7", language: "yo", front: "Ẹ kú àárọ̀", back: "Good morning (Said with honorific respect for peers or elders)", category: "Greetings" },
  { id: "f8", language: "yo", front: "Adúpẹ́", back: "We give thanks / Thank you", category: "Social" },
  { id: "f9", language: "ha", front: "Ina kwana", back: "How did you sleep? / Standard morning greeting", category: "Greetings" },
  { id: "f10", language: "ha", front: "Na gode", back: "Thank you (Gratitude response)", category: "Social" },
  { id: "f11", language: "xh", front: "Molo", back: "Hello (Singular greeting to one person)", category: "Greetings" },
  { id: "f12", language: "xh", front: "Enkosi", back: "Thank you", category: "Social" }
];

export interface TimelinePhase {
  phaseNum: number;
  title: string;
  days: string;
  items: string[];
}

export const TIMELINE_PHASES: TimelinePhase[] = [
  {
    phaseNum: 1,
    title: "Foundation & System Shell",
    days: "Days 1–7",
    items: [
      "Create developer & Hub accounts: HuggingFace, Firebase, GitHub, Google AI Studio.",
      "Use AI Studio Build Mode to bootstrap react and Node/Express backend layers.",
      "Build live translation API gateway routes wrapping HuggingFace Inference with FastAPI and python fallback protocols.",
      "Pass full ARIA accessibility standards for visual impairment, blind reader compliance, and large click targets.",
      "Activate Voice Input (Web Speech API) + Meta MMS voice output models."
    ]
  },
  {
    phaseNum: 2,
    title: "Accessibility & Deeper Integration",
    days: "Days 8–14",
    items: [
      "Fine-tune NLLB-200 utilizing free Kaggle/Colab GPU hardware on Masakhane datasets for direct Amharic-Xhosa-Swahili loops.",
      "Build educational TeachingMode modules: spaced repetition flashcard system, audio phrase of the day player.",
      "Launch MedicalMode medical vocabulary phrase packs covering symptoms, instructions, and emergencies.",
      "Quantize direct translation parameters into optimized TFLite files for Offline Android and mobile usage."
    ]
  },
  {
    phaseNum: 3,
    title: "Doc Compilation & Grant Delivery",
    days: "Days 15–21",
    items: [
      "Prepare interactive MIT Deep Tech program application specializing in healthcare linguistics.",
      "Draft LINGUA Africa proposals focusing on high accessibility tools for differently-abled African communities.",
      "Record full 2-minute demonstration video and compute translation BLEU benchmarks (scores 25-45).",
      "Release open source system assets to HuggingFace under CC-BY and code outputs under MIT/Apache 2.0 license."
    ]
  }
];

export interface FreeTierReference {
  platform: string;
  offered: string;
  limits: string;
  usage: string;
}

export const FREE_TIER_REFERENCES: FreeTierReference[] = [
  { platform: "Google AI Studio", offered: "Build Mode, Cloud Starter deploys, Gemini Flash models", limits: "Flash rate limits (15 req/min); Pro paid after Apr 2026", usage: "App shell updates, language translation, context extraction" },
  { platform: "Firebase Spark", offered: "50K reads/day, 5GB Storage, 2M functions/mo, Auth", limits: "Upgrade if scales beyond 50K daily active transactions", usage: "Offline user cache, translation history storing, user credentials" },
  { platform: "HuggingFace", offered: "Free Model weight repository, Spaces CPU host, Datasets Repo", limits: "Spaces run on CPU only unless GPU compute tokens applied", usage: "NLLB-200 base translation, MMS speech syntheses, corpus storage" },
  { platform: "Kaggle Notebooks", offered: "2x T4 GPU cores, 30hr/week quota, persistent kernels", limits: "Weekly cap must be managed carefully for training intervals", usage: "Direct bilingual model fine-tuning on open Africa text corpus" },
  { platform: "Google Colab", offered: "T4 GPU cluster, virtual Python 3 runtimes, 12hr sessions", limits: "Disconnects and clears local space after idle intervals", usage: "Real-time experiments, code prototyping and weight verification" },
  { platform: "Expo (EAS)", offered: "EAS build service for cross platform deployment", limits: "Free queue delays on active request traffic hours", usage: "iOS + Android mobile native app shells compilation" }
];

export interface StartupComparison {
  name: string;
  whatTheyDo: string;
  differentiation: string;
  feasibilityRating: string;
  grantRelevance: string;
}

export const COMPETING_STARTUPS: StartupComparison[] = [
  {
    name: "Lelapa AI (South Africa)",
    whatTheyDo: "African language NLP tools & APIs.",
    differentiation: "Nguzo adds direct cross-language pairs and a local medical device watch layer.",
    feasibilityRating: "HIGH. Beginners can call Lelapa's public NLP wrappers directly in Python rather than coding massive custom attention models.",
    grantRelevance: "MIT & LINGUA Africa: Validates our focus on applying core research to actual medical clinical interfaces."
  },
  {
    name: "Ubenwa (Nigeria)",
    whatTheyDo: "Baby cry diagnostic AI utilizing African speech data.",
    differentiation: "Focuses on infant diagnostic acoustics; Nguzo adopts their community-first clinic validation ethos for direct translation.",
    feasibilityRating: "HIGH. Rather than training complex infant respiratory audio models, a beginner replicates their grassroots research framework.",
    grantRelevance: "MIT Deep Tech: Reflects Ubenwa's highly successful clinical trial playbook, which reviewers look for."
  },
  {
    name: "InstaDeep (Africa)",
    whatTheyDo: "Enterprise decision-making AI, major DeepMind research partner.",
    differentiation: "Nguzo is grassroots, open-source, and optimized for lightweight mobile environments instead of enterprise supercomputers.",
    feasibilityRating: "HIGH. Avoids heavy reinforcement learning nodes in favor of high-level pre-trained models on Hugging Face.",
    grantRelevance: "LINGUA Africa & MIT: Directly addresses local, field-level healthcare challenges ignored by enterprise clusters."
  },
  {
    name: "Masakhane Translate",
    whatTheyDo: "Open-source machine translation for low-resource African languages.",
    differentiation: "Masakhane is foundational data infrastructure; Nguzo is the consumer app layer with visual and audio accessibility features.",
    feasibilityRating: "EXCELLENT (Very High). Masakhane shares open translation corpora, permitting beginner-friendly loading into Colab in just 5 lines.",
    grantRelevance: "LINGUA Africa: Shows direct ecosystem alignment and respect for Africa's leading open linguistics project."
  },
  {
    name: "Google Translate (African)",
    whatTheyDo: "State of translation for Swahili, Amharic, Zulu, etc.",
    differentiation: "Routes translations through English-centric relays; lacks assistive spoken/visual modes; closed source.",
    feasibilityRating: "HIGH. By replacing expensive proprietary APIs with open NLLB weights in Google Colab, a beginner bypasses commercial billing hurdles.",
    grantRelevance: "MIT deep-tech: Directly solves the relay-bias problem (where translating Swahili-to-Amharic via English distorts gender and respect)."
  },
  {
    name: "Siri / Alexa",
    whatTheyDo: "Global voice assistants with limited low-resource phonetic or accent support.",
    differentiation: "Nguzo's model is custom-trained to respect Swahili, Amharic, and Yoruba accents, click consonants, and vocal tones.",
    feasibilityRating: "MEDIUM. Raw audio feature extraction can be intensive, but beginners can utilize pre-trained Meta MMS weights to abstract complexity.",
    grantRelevance: "LINGUA Africa: Focuses on voice-first accessibility for under-represented languages, serving non-literate community populations."
  },
  {
    name: "Deep Voice / Mozilla TTS",
    whatTheyDo: "Open-source text-to-speech synthesis research platforms.",
    differentiation: "Nguzo uses these as underlying precompiled pipeline components rather than competing with them as a broad audio framework.",
    feasibilityRating: "VERY HIGH. Reusing their pre-built synthesizers allows beginners to render audio locally without custom GPU model architectures.",
    grantRelevance: "MIT & LINGUA Africa: Demonstrates prudent technical resource management, accelerating MVP flight timelines."
  }
];

