import re
import contractions
from spellchecker import SpellChecker

def tokenize(text):
    return '\n\n'.join(
     '\n'.join(' '.join(token.value for token in sentence)
        for sentence in paragraph)
     for paragraph in segmenter.analyze(text))

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

def chat_words_conversion(text):
    chat_words_str = """
        AFAIK=As Far As I Know
        AFK=Away From Keyboard
        ASAP=As Soon As Possible
        ATK=At The Keyboard
        ATM=At The Moment
        A3=Anytime, Anywhere, Anyplace
        BAK=Back At Keyboard
        BBL=Be Back Later
        BBS=Be Back Soon
        BFN=Bye For Now
        B4N=Bye For Now
        BRB=Be Right Back
        BRT=Be Right There
        BTW=By The Way
        B4=Before
        B4N=Bye For Now
        B.S.=bullshit
        B.S.,=bullshit,
        BS=bullshit
        BFF=Best Friends Forever
        CU=See You
        CUL8R=See You Later
        CYA=See You
        FAQ=Frequently Asked Questions
        FC=Fingers Crossed
        FWIW=For What It's Worth
        FYI=For Your Information
        GAL=Get A Life
        GG=Good Game
        GN=Good Night
        GMTA=Great Minds Think Alike
        GR8=Great!
        G9=Genius
        IC=I See
        ICQ=I Seek you (also a chat program)
        ILU=ILU: I Love You
        IMHO=In My Honest/Humble Opinion
        IMO=In My Opinion
        IOW=In Other Words
        IRL=In Real Life
        KISS=Keep It Simple, Stupid
        LDR=Long Distance Relationship
        LMAO=Laugh My A.. Off
        LOL=Laughing Out Loud
        LTNS=Long Time No See
        L8R=Later
        MTE=My Thoughts Exactly
        M8=Mate
        NRN=No Reply Necessary
        OIC=Oh I See
        PITA=Pain In The A..
        PRT=Party
        PRW=Parents Are Watching
        ROFL=Rolling On The Floor Laughing
        ROFLOL=Rolling On The Floor Laughing Out Loud
        ROTFLMAO=Rolling On The Floor Laughing My A.. Off
        SK8=Skate
        STATS=Your sex and age
        ASL=Age, Sex, Location
        THX=Thank You
        TTFN=Ta-Ta For Now!
        TTYL=Talk To You Later
        U=You
        U2=You Too
        U4E=Yours For Ever
        WB=Welcome Back
        WTF=What The F...
        WTG=Way To Go!
        WUF=Where Are You From?
        W8=Wait...
        7K=Sick:-D Laugher
    """

    chat_words_map_dict = {}
    chat_words_list = []
    for line in chat_words_str.split("\n"):
        line = line.strip()
        if line != "":
            cw = line.split("=")[0]
            cw_expanded = line.split("=")[1]
            chat_words_list.append(cw)
            chat_words_map_dict[cw] = cw_expanded
    chat_words_list = set(chat_words_list)

    new_text = []
    for w in text.split():
        if w.upper() in chat_words_list:
            new_text.append(chat_words_map_dict[w.upper()])
        else:
            new_text.append(w)
    return " ".join(new_text)

# creating an empty list

def expand_contractions(text):
    expanded_words = []   
    for word in text.split():
        # using contractions.fix to expand the shortened words
        try:
            expanded_words.append(contractions.fix(word))  
        except:
            print(word)
    expanded_text = ' '.join(expanded_words)
    return expanded_text


def correct_spellings(text):
    spell = SpellChecker()
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_word = spell.correction(word)
            if corrected_word != None:
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)
        else:
            corrected_text.append(word)
    try:
        return " ".join(corrected_text)
    except:
        print(text)

