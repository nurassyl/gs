from gss.dictionary import *

# 1 сөз = 100 байт.
# 10 сөз = 1 Кбайт.
# 10000 сөз = 1 Мбайт.
# 10 000 000 = 1 Гбайт.
# 640 000 000 = 64Гбайт.

words = [
    'қазақ',
    'электр'
]

print(create_dict_tote_cyrillic(words))
