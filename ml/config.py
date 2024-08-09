MORAL_FEATURES = ['moral_care', 'moral_fairness', 'moral_loyalty', 'moral_authority', 'moral_purity']
EMOTION_FEATURES = ['emotion_fear','emotion_anger','emotion_anticip','emotion_trust','emotion_surprise','emotion_positive','emotion_negative','emotion_sadness','emotion_disgust','emotion_joy','emotion_anticipation']
READABILITY_GRADE_FEATURES = ['readability_Kincaid',
                                'readability_ARI',
                                'readability_Coleman-Liau',
                                'readability_FleschReadingEase',
                                'readability_GunningFogIndex',
                                'readability_LIX',
                                'readability_SMOGIndex',
                                'readability_RIX',
                                'readability_DaleChallIndex']
READABILITY_SENTENCEINFO_FEATURES = ['readability_characters_per_word',
                                'readability_syll_per_word',
                                'readability_words_per_sentence',
                                'readability_sentences_per_paragraph',
                                'readability_type_token_ratio',
                                'readability_directspeech_ratio',
                                'readability_characters',
                                'readability_syllables',
                                'readability_words',
                                'readability_wordtypes',
                                'readability_sentences',
                                'readability_paragraphs',
                                'readability_long_words',
                                'readability_complex_words',
                                'readability_complex_words_dc']

READABILITY_WORDUSAGE_FEATURES = ['readability_tobeverb', 'readability_auxverb', 'readability_conjunction', 'readability_pronoun','readability_preposition', 'readability_nominalization']
READABILITY_SENTENCEBEGINNING_FEATURES = [ 
                                'readability_interrogative',
                                'readability_article',
                                'readability_subordination',]
SENTIMENT_FEATURES = ['sentiment_neu', 'sentiment_pos', 'sentiment_neg', 'sentiment_compound']
LIWC_LINGUISTIC_FEATURES = ['liwc_function',
                                'liwc_pronoun',
                                'liwc_ppron',
                                'liwc_i',
                                'liwc_we',
                                'liwc_you',
                                'liwc_shehe',
                                'liwc_they',
                                'liwc_ipron',
                                'liwc_article',
                                'liwc_prep',
                                'liwc_auxverb',
                                'liwc_adverb',
                                'liwc_conj',
                                'liwc_negate',
                                'liwc_verb',
                                'liwc_adj',
                                'liwc_compare',
                                'liwc_interrog',
                                'liwc_number',
                                'liwc_quant']
LIWC_AFFECTIVEPROCESSES_FEATURES = ['liwc_affect',
                                'liwc_posemo',
                                'liwc_negemo',
                                'liwc_anx',
                                'liwc_anger',
                                'liwc_sad']
LIWC_SOCIALPROCESSES_FEATURES = ['liwc_social',
                                'liwc_family',
                                'liwc_friend',
                                'liwc_female',
                                'liwc_male']
LIWC_COGNITIVEPROCESSES_FEATURES = [ 'liwc_cogproc',
                                'liwc_insight',
                                'liwc_cause',
                                'liwc_discrep',
                                'liwc_tentat',
                                'liwc_certain',
                                'liwc_differ']
LIWC_PERCEPTUALPROCESSES_FEATURES = [ 'liwc_percept',
                                'liwc_see',
                                'liwc_hear', 'liwc_feel']

LIWC_BIOLOGICALPROCESSES_FEATURES = ['liwc_bio',
                                    'liwc_body',
                                    'liwc_health',
                                    'liwc_sexual',
                                    'liwc_ingest']
LIWC_DRIVES_FEATURES = ['liwc_drives',
 'liwc_affiliation',
 'liwc_achiev',
 'liwc_power',
 'liwc_reward',
 'liwc_risk']

LIWC_TIMEORIENTATION_FEATURES = [ 'liwc_focuspast',
 'liwc_focuspresent',
 'liwc_focusfuture',]

LIWC_RELATIVITY_FEATURES = ['liwc_relativ',
 'liwc_motion',
 'liwc_space',
 'liwc_time',]

LIWC_PERSONALCONCERNS_FEATURES = ['liwc_work',
 'liwc_leisure',
 'liwc_home',
 'liwc_money',
 'liwc_relig',
 'liwc_death',]

LIWC_INFORMALLANGUAGE_FEATURES = ['liwc_informal',
 'liwc_swear',
 'liwc_netspeak',
 'liwc_assent',
 'liwc_nonflu',
 'liwc_filler']
