from gs.analyzer import get_all_cyrillic_words, get_all_latin_words

__CYRILLIC = (
    ["а", "ә", "б", "в", "г", "ғ", "д", "е", "ё", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п", "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "ъ", "ы", "і", "ь", "э", "ю", "я"],
    ["a", "ä", "b", "v", "g", "ğ", "d", "e", "ïo", "j", "z", "ï", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "ö", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "", "y", "i", "", "e", "ïu", "ïa"],
    ["ا", "ا", "ب", "ۆ", "گ", "ع", "د", "ە", "يو", "ج", "ز", "ي", "ي", "ك", "ق", "ل", "م", "ن", "ڭ", "و", "و", "پ", "ر", "س", "ت", "ۋ", "ۇ", "ۇ", "ف", "ح", "ھ", "س", "چ", "ش", "ش", "", "ى", "ى", "", "ە", "يۋ", "يا"],
)
__LATIN = (
    ["ïu", "ïa", "ïo", "uï", "üï", "wï", "yï", "aï", "äï", "oï", "öï", "a", "ä", "b", "v", "g", "ğ", "d", "e", "j", "z", "ï", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "ö", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "", "y", "i", "", "e"],
    ["ю", "я", "ё", "ұй", "үй", "уй", "ый", "ай", "әй", "ой", "өй", "а", "ә", "б", "в", "г", "ғ", "д", "е", "ж", "з", "и", "й", "к", "қ", "л", "м", "н", "ң", "о", "ө", "п", "р", "с", "т", "у", "ұ", "ү", "ф", "х", "һ", "ц", "ч", "ш", "щ", "", "ы", "і", "", "э"],
)
__TOTE = (
    ["ا", "ب", "ۆ", "گ", "ع", "د", "ە", "ج", "ز", "ي", "ك", "ق", "ل", "م", "ن", "ڭ", "و", "پ", "ر", "س", "ت", "ۋ", "ۇ", "ۇ", "ف", "ح", "ح", "س", "چ", "ش", "ش", "ى", "ى"],
    ["a", "b", "v", "g", "ğ", "d", "e", "j", "z", "ï", "k", "q", "l", "m", "n", "ŋ", "o", "p", "r", "s", "t", "w", "u", "ü", "f", "h", "h", "c", "č", "š", "ş", "y", "i"],
)

for i in range(0, len(__CYRILLIC[0])):
    __CYRILLIC[0].append(__CYRILLIC[0][i].capitalize())
    __CYRILLIC[1].append(__CYRILLIC[1][i].capitalize())
    __CYRILLIC[2].append(__CYRILLIC[2][i].capitalize())
for i in range(0, len(__LATIN[0])):
    __LATIN[0].append(__LATIN[0][i].capitalize())
    __LATIN[1].append(__LATIN[1][i].capitalize())

def convert_cyrillic_to_latin(text):
	all_words = get_all_cyrillic_words(text)
	def replace_word(text):
		if text[:1] == 'е':
			text = 'ye'+text[1:]
		if text[:1] == 'Е':
			text = 'Ye'+text[1:]
		for i in range(0, len(__CYRILLIC[0])):
			text = text.replace(__CYRILLIC[0][i], __CYRILLIC[1][i])
		return text
	for word in all_words:
		text = text.replace(word, replace_word(word), 1)
	return text
def convert_cyrillic_to_tote(text):
    for i in range(0, len(__CYRILLIC[0])):
        text = text.replace(__CYRILLIC[0][i], __CYRILLIC[2][i])
    return text

def convert_latin_to_cyrillic(text):
	all_words = get_all_latin_words(text)
	def replace_word(text):
		if text[:1] == 'e':
			text = 'э'+text[1:]
		elif text[:1] == 'E':
			text = 'Э'+text[1:]
		elif text[:2] == 'ye':
			text = 'е'+text[2:]
		elif text[:2] == 'Ye':
			text = 'Е'+text[2:]
		for i in range(0, len(__LATIN[0])):
			text = text.replace(__LATIN[0][i], __LATIN[1][i])
		return text
	for word in all_words:
		text = text.replace(word, replace_word(word), 1)
	return text
def convert_latin_to_tote(text):
    text = convert_latin_to_cyrillic(text)
    text = convert_cyrillic_to_tote(text)
    return text

def convert_tote_to_latin(text):
    for i in range(0, len(__TOTE[0])):
        text = text.replace(__TOTE[0][i], __TOTE[1][i])
    return text
def convert_tote_to_cyrillic(text):
    text = convert_tote_to_latin(text)
    text = convert_latin_to_cyrillic(text)
    return text
