from utils import *

input = 'Elektrondy qurylğylar.'

latin_words = list()
for word in get_latin_words(input):
    input = re.sub(word, convert_to_cyrillic(word), input)
    del word

for word in get_cyrillic_words_from_latin(input):
    original = word
    wc = what_case(word)
    word = word.lower()
    word = REPAIRED_WORD_FROM_LATIN[word]
    word = normalize(word, wc)
    input = input.replace(original, word)
    del word, wc

print(input)
del input
