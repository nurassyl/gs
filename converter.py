from utils import convert_to_latin, convert_to_cyrillic
from tote import latin_to_tote, tote_to_latin

def convert_cyril_to_lat(input):
    return convert_to_latin(input)
def convert_cyril_to_tote(input):
    return latin_to_tote( convert_to_latin(input) )

def convert_lat_to_cyril(input):
    return convert_to_cyrillic(input)
def convert_lat_to_tote(input):
    return latin_to_tote( convert_to_latin(input) )

def convert_tote_to_cyril(input):
    return convert_to_cyrillic( tote_to_latin(input) )
def convert_tote_to_lat(input):
    return tote_to_latin(input)

# print(convert_cyril_to_lat('Қазақ тілі'))
# print(convert_cyril_to_tote('Қазақ тілі'))
# print(convert_lat_to_cyril('Qazaq tili'))
# print(convert_lat_to_tote('Qazaq tili'))
# print(convert_tote_to_cyril( cyril_to_tote('Қазақ тілі') ))
# print(convert_tote_to_lat( cyril_to_tote('Қазақ тілі') ))
