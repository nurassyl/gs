TOTE = {
    "a": "ا",
    "ä": "ا",
    "b": "ب",
    "v": "ۆ",
    "g": "گ",
    "ğ": "ع",
    "d": "د",
    "e": "ە",
    "j": "ج",
    "z": "ز",
    "ï": "ي",
    "k": "ك",
    "q": "ق",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "ŋ": "ڭ",
    "o": "و",
    "ö": "ٴو",
    "p": "پ",
    "r": "ر",
    "s": "س",
    "t": "ت",
    "w": "ۋ",
    "u": "ۇ",
    "ü": "ۇ",
    "f": "ف",
    "h": "ح",
    "c": "س",
    "č": "چ",
    "š": "ش",
    "ş": "ٴش",
    "y": "ى",
    "i": "ى",
}


def latin_to_tote(value):
    value = value.lower()
    for k, v in TOTE.items():
        value = value.replace(k, v)
    return value

def tote_to_latin(value):
    for k, v in TOTE.items():
        value = value.replace(v, k)
    return value
