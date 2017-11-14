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
    ["aï", "äï", "oï", "öï", "ïw", "ïa", "ïo", "a", "ä", "b", "v", "g", "ğ", "d", "e", "j", "z", "ï", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "ö", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "", "y", "i", "", "e"],
    ["ай", "әй", "ой", "өй", "ю", "я", "ё", "а", "ә", "б", "в", "г", "ғ", "д", "е", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п", "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "", "ы", "і", "", "э"]
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


KZ_WORDS = [
    'қазақ',
    'ел',
    'тіл',
    'әлем',
    'ең',
    'бай'
]

import re
def get_kz_words(text):
    FINDED_CYRILLIC_WORDS = list()

    for kz_word in KZ_WORDS:
        words = re.findall(r'(({})([аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]*))'.format(kz_word), text, flags=re.I)
        for i in range(0, len(words)):
            FINDED_CYRILLIC_WORDS.append(words[i][0])
            del i
        del kz_word, words
    return FINDED_CYRILLIC_WORDS


input = 'Қазақ еліндегі қазақ тілі әлемдегі ең бай тіл!'
for word in get_kz_words(input):
    input = re.sub(word, convert_to_latin(word), input)
    del word

print(input)
del input
