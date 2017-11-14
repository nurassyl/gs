from utils import *

input = 'Қазақ тілі әлемдегі ең бай тіл!'

for word in get_cyrillic_words(input):
    input = re.sub(word, convert_to_latin(word), input)
    del word

print(input)
del input
