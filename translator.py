# Cyrillic to latin.
# Cyrillic to tote.
# Latin to cyrillic.
# Latin to tote.
# Tote to cyrillic
# Tote to latyn.

from cyrillic_to_latin import cyrillic_to_latin
from latin_to_cyrillic import latin_to_cyrillic
from tote import latin_to_tote, tote_to_latin

def cyril_to_lat(input):
    return cyrillic_to_latin(input)
def cyril_to_tote(input):
    return latin_to_tote( cyrillic_to_latin(input) )

def lat_to_cyril(input):
    return latin_to_cyrillic(input)
def lat_to_tote(input):
    return latin_to_tote(input)

def tote_to_cyril(input):
    return latin_to_cyrillic( tote_to_latin(input) )
def tote_to_lat(input):
    return tote_to_latin(input)

print(cyril_to_lat('Қазақ тілі'))
print(cyril_to_tote('Қазақ тілі'))
print(lat_to_cyril('Qazaq tili'))
print(lat_to_tote('Qazaq tili'))
print(tote_to_cyril('قازاق تىلى'))
print(tote_to_lat('قازاق تىلى'))
