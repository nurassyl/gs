from gss.utils import *

# Latin to cyrillic.
def latin_to_cyrillic(input):
    latin_words = list()
    for word in get_latin_words(input):
        input = re.sub(word, convert_to_cyrillic(word), input)
        del word

    for word in find_cyrillic_words_from_text(input):
        original = word
        wc = what_case(word)
        word = word.lower()
        word = REPAIRED_WORD_FROM_LATIN[word]
        word = normalize(word, wc)
        input = input.replace(original, word)
        del word, wc

    return input
