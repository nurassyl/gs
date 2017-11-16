# Cyrillic to latin.
# Cyrillic to tote.
# Latin to cyrillic.
# Latin to tote.
# Tote to cyrillic
# Tote to latyn.

from gss.cyrillic_to_latin import cyrillic_to_latin
from gss.latin_to_cyrillic import latin_to_cyrillic
from gss.tote import latin_to_tote, tote_to_latin
from gss.converter import *

def translate_cyril_to_lat(input, with_converter=True):
    translated = cyrillic_to_latin(input)
    if with_converter == True:
        translated = convert_cyril_to_lat(translated)
    return translated
def translate_cyril_to_tote(input, with_converter=True):
    translated = latin_to_tote( cyrillic_to_latin(input) )
    if with_converter == True:
        translated = convert_cyril_to_tote(translated)
    return translated

def translate_lat_to_cyril(input, with_converter=True):
    translated = latin_to_cyrillic(input)
    if with_converter == True:
        translated = convert_lat_to_cyril(translated)
    return translated
def translate_lat_to_tote(input, with_converter=True):
    translated = latin_to_tote(input)
    if with_converter == True:
        translated = convert_lat_to_tote(translated)
    return translated

def translate_tote_to_cyril(input, with_converter=True):
    translated = latin_to_cyrillic( tote_to_latin(input) )
    if with_converter == True:
        translated = convert_tote_to_cyril(translated)
    return translated
def translate_tote_to_lat(input, with_converter=True):
    translated = tote_to_latin(input)
    if with_converter == True:
        translated = convert_tote_to_lat(translated)
    return translated
    
# print(translate_cyril_to_lat('Қазақ тілі'))
# print(translate_cyril_to_tote('үкі'))
# print(translate_lat_to_cyril('Qazaq tili'))
# print(translate_lat_to_tote('Qazaq tili'))
# print(translate_tote_to_cyril( translate_cyril_to_tote('үкі') ))
# print(translate_tote_to_lat( translate_cyril_to_tote('Қазақ тілі') ))
