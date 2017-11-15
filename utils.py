def what_case(word):
    if word.upper() == word:
        return 'up'
    elif word[0].upper() == word[0]:
        return 'capitalize'
    else:
        return 'down'

def normalize(word, c='down'):
    if c == 'up':
        return word.upper()
    elif c == 'capitalize':
        return word.capitalize()
    else:
        return word.lower()

CYRILLIC_TO_LATIN = [
    ["а", "ә", "б", "в", "г", "ғ", "д", "е", "ё", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п", "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "ъ", "ы", "і", "ь", "э", "ю", "я"],
    ["a", "ä", "b", "v", "g", "ğ", "d", "e", "ïo", "j", "z", "ï", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "ö", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "", "y", "i", "", "e", "ïw", "ïa"]
]
# "ч" әріпінен тұратын "чек" сөзі бар.
# "ч" әріпінен тұратын "щетка" сөзі бар.
# "э" әріпінен тұратын "электр" сөзі бар.
LATIN_TO_CYRILLIC = [
    ["ұй", "үй", "уй", "ый", "ей", "эй", "aï", "äï", "oï", "öï", "ïw", "ïa", "ïo", "a", "ä", "b", "v", "g", "ğ", "d", "e", "j", "z", "ï", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "ö", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "", "y", "i", "", "e"],
    ["uï", "üï", "wï", "yï", "eï", "eï", "ай", "әй", "ой", "өй", "ю", "я", "ё", "а", "ә", "б", "в", "г", "ғ", "д", "е", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п", "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "", "ы", "і", "", "э"]
]

def convert_to_latin(word):
    wc = what_case(word)
    word = word.lower()

    for i in range(0, len(CYRILLIC_TO_LATIN[0])):
        word = word.replace(CYRILLIC_TO_LATIN[0][i], CYRILLIC_TO_LATIN[1][i])
    
    return normalize(word, wc)

def convert_to_cyrillic(word):
    wc = what_case(word)
    word = word.lower()

    for i in range(0, len(LATIN_TO_CYRILLIC[0])):
        word = word.replace(LATIN_TO_CYRILLIC[0][i], LATIN_TO_CYRILLIC[1][i])
    
    return normalize(word, wc)

def convert_to_tote(word):
    wc = what_case(word)
    word = word.lower()

    for i in range(0, len(CYRILLIC_TO_TOTE[0])):
        word = word.replace(CYRILLIC_TO_TOTE[0][i], CYRILLIC_TO_TOTE[1][i])
    
    return normalize(word, wc)

KZ_WORDS = [
    'қазақ',
    'ел',
    'тіл',
    'әлем',
    'ең',
    'бай',
    'электр',
    'тоқ',
    'тоғ', # тоғы
    'құр',
    'эх',
    'жар',
    'сүй',
    'сүт'
    'ет',
    'сол',
    'ар',
    'мен',
    'асыл',
    'сөз',
    'сен',
    'ең',
    'мәр',
    'қаһарман',
    'бат',
    'ірімшік'
]

KZ_WORDS.sort(key = len, reverse=True)

REPAIRED_WORD_FROM_LATIN = dict()
for word in KZ_WORDS:
    REPAIRED_WORD_FROM_LATIN[ convert_to_cyrillic(convert_to_latin(word)) ] = word
    del word

import re
def get_cyrillic_words(text):
    FINDED_WORDS = list()

    for word in KZ_WORDS:
        words = re.findall(r'(({})([аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]*))'.format(word), text, flags=re.I)
        for i in range(0, len(words)):
            FINDED_WORDS.append(words[i][0])
            del i
        del word, words

    return FINDED_WORDS

def get_latin_words(text):
    FINDED_WORDS = list()

    for word in KZ_WORDS:
        word = convert_to_latin(word)
        words = re.findall(r'(({})([aäbvgğdejzïïkqlmnŋoöprstwuüfhhcčšşyi]*))'.format(word), text, flags=re.I)
        for i in range(0, len(words)):
            FINDED_WORDS.append(words[i][0])
            del i
        del word, words

    return FINDED_WORDS

CONVERTED_KZ_WORDS_FROM_LATIN = list()
for word in KZ_WORDS:
    CONVERTED_KZ_WORDS_FROM_LATIN.append( convert_to_cyrillic(convert_to_latin(word)) )
    del word

def get_cyrillic_words_from_latin(text):
    FINDED_WORDS = list()

    for word in CONVERTED_KZ_WORDS_FROM_LATIN:
        words = re.findall(r'({})'.format(word), text, flags=re.I)
        for w in words:
            FINDED_WORDS.append(w)
            del w
        del word, words

    return FINDED_WORDS
