from utils import convert_to_latin, convert_to_cyrillic
from tote import latin_to_tote, tote_to_latin

def cyril_to_lat(input):
    return convert_to_latin(input)
def cyril_to_tote(input):
    return latin_to_tote( convert_to_latin(input) )

def lat_to_cyril(input):
    return convert_to_cyrillic(input)
def lat_to_tote(input):
    return latin_to_tote( convert_to_latin(input) )

def tote_to_cyril(input):
    return convert_to_cyrillic( tote_to_latin(input) )
def tote_to_lat(input):
    return tote_to_latin(input)

# print(cyril_to_lat('Қазақ тілі'))
# print(cyril_to_tote('Қазақ тілі'))
# print(lat_to_cyril('Qazaq tili'))
# print(lat_to_tote('Qazaq tili'))
# print(tote_to_cyril( cyril_to_tote('Қазақ тілі') ))
# print(tote_to_lat( cyril_to_tote('Қазақ тілі') ))
