from gs.dictionary import *
from gs.translator import *
from gs.converter import *

# 1 сөз = 100 байт.
# 10 сөз = 1 Кбайт.
# 10000 сөз = 1 Мбайт.
# 10 000 000 = 1 Гбайт.
# 640 000 000 = 64Гбайт.

words = [
    'қазақ',
    'тілі',
]

cyrillic_latin_dict = create_dict_cyrillic_latin(words)
cyrillic_tote_dict = create_dict_cyrillic_tote(words)
latin_cyrillic_dict = create_dict_latin_cyrillic(words)
latin_tote_dict = create_dict_latin_tote(words)
tote_latin_dict = create_dict_tote_latin(words)
tote_cyrillic_dict = create_dict_tote_cyrillic(words)

print(translate_cyrillic_to_latin('Қазақ тілі', cyrillic_latin_dict))
print(translate_cyrillic_to_tote('Қазақ тілі', cyrillic_tote_dict))
print(translate_latin_to_cyrillic('Qazaq tili', latin_cyrillic_dict))
print(translate_latin_to_tote('Qazaq tili', latin_tote_dict))
print(translate_tote_to_latin('قازاق تىلى', tote_latin_dict))
print(translate_tote_to_cyrillic('قازاق تىلى', tote_cyrillic_dict))

print(convert_cyrillic_to_latin('Ел'))
print(convert_cyrillic_to_latin('Экономика'))
print(convert_latin_to_cyrillic('Yel'))
print(convert_latin_to_cyrillic('Ekonomïka'))
