from gs.dictionary import *
from gs.analyzer import *
from gs.utils import *

# letters: ('cyrillic', 'latin', 'tote')
def __translate(text, _dict, letters='cyrillic'):
    result = {
        'unknowns': list(),
        'output': ''
    }

    if letters == 'latin':
        words = get_all_latin_words(text)
    elif letters == 'tote':
        words = get_all_tote_words(text)
    else:
        words = get_all_cyrillic_words(text)

    words.sort(key = len, reverse=True)

    for word in words:
        try:
            wc = what_case(word)
            text = text.replace(word, normalize(_dict[word.lower()], wc))
        except KeyError:
            result['unknowns'].append(word)
        del word, wc
    
    if letters == 'tote':
        text = text.lower()

    result['output'] = text
    del text, _dict, words
    return result

def translate_cyrillic_to_latin(text, _dict):
    return __translate(text, _dict)
def translate_cyrillic_to_tote(text, _dict):
    return __translate(text, _dict)

def translate_latin_to_cyrillic(text, _dict):
    return __translate(text, _dict, 'latin')
def translate_latin_to_tote(text, _dict):
    return __translate(text, _dict, 'latin')

def translate_tote_to_latin(text, _dict):
    return __translate(text, _dict, 'tote')
def translate_tote_to_cyrillic(text, _dict):
    return __translate(text, _dict, 'tote')
