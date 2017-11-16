from gss.converter import *

def create_dict_cyrillic_latin(words):
    dictionary = dict()
    for word in words:
        dictionary[word] = convert_cyrillic_to_latin(word)
        del word

    return dictionary

def create_dict_cyrillic_tote(words):
    dictionary = dict()
    for word in words:
        dictionary[word] = convert_cyrillic_to_tote(word)
        del word

    return dictionary

def create_dict_latin_cyrillic(words):
    dictionary = dict()
    for word in words:
        dictionary[convert_cyrillic_to_latin(word)] = word
        del word

    return dictionary

def create_dict_latin_tote(words):
    dictionary = dict()
    for word in words:
        dictionary[convert_cyrillic_to_latin(word)] = convert_latin_to_tote(word)
        del word

    return dictionary

def create_dict_tote_latin(words):
    dictionary = dict()
    for word in words:
        dictionary[convert_cyrillic_to_tote(word)] = convert_cyrillic_to_latin(word)
        del word

    return dictionary

def create_dict_tote_cyrillic(words):
    dictionary = dict()
    for word in words:
        dictionary[convert_cyrillic_to_tote(word)] = word
        del word

    return dictionary
