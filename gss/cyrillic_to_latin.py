from gss.utils import *

# Cyrillic to latin.
def cyrillic_to_latin(input):
    for word in get_cyrillic_words(input):
        input = re.sub(word, convert_to_latin(word), input)
        del word
    
    return input
