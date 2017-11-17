import re

def get_all_cyrillic_words(text):
    finded_words = list()
    words = re.findall(r'([аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]+(\-[аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]+)?)', text, flags=re.I)
    for word in words:
        finded_words.append(word[0])
    del words
    return finded_words

def get_all_latin_words(text):
    finded_words = list()
    words = re.findall(r'([\'aäbvgğdejzïïkqlmnŋoöprstwuüfhhcčšşyi]+(\-[\'aäbvgğdejzïïkqlmnŋoöprstwuüfhhcčšşyi]+)?)', text, flags=re.I)
    for word in words:
        finded_words.append(word[0])
    del words
    return finded_words

def get_all_tote_words(text):
    finded_words = list()
    words = re.findall(r'([\u0674\u0627\u0628\u06C6\u06AF\u0639\u062F\u06D5\u062C\u0632\u064A\u0643\u0642\u0644\u0645\u0646\u06AD\u0648\u067E\u0631\u0633\u062A\u06CB\u06C7\u06C7\u0641\u062D\u062D\u0633\u0686\u0634\u0634\u0649\u0649]+(\-[\u0674\u0627\u0628\u06C6\u06AF\u0639\u062F\u06D5\u062C\u0632\u064A\u0643\u0642\u0644\u0645\u0646\u06AD\u0648\u067E\u0631\u0633\u062A\u06CB\u06C7\u06C7\u0641\u062D\u062D\u0633\u0686\u0634\u0634\u0649\u0649]+)?)', text, flags=re.I)
    for word in words:
        finded_words.append(word[0])
    del words
    return finded_words
