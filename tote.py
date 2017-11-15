TOTE = {
    "a": "ا",
    "ä": "ٴا",
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
    "ü": "ٴۇ",
    "f": "ف",
    "h": "ح",
    "c": "س",
    "č": "چ",
    "š": "ش",
    "ş": "ٴش",
    "y": "ى",
    "i": "ى"
}
TOTE_KEYS = TOTE.copy().keys()

for k in TOTE_KEYS:
    TOTE[k.upper()] = TOTE[k]



def latin_to_tote(value):
    for k, v in TOTE.items():
        value = value.replace(k, v)
    return value.lower()

def tote_to_latin(value):
    for k, v in TOTE.items():
        value = value.replace(v, k)
    return value.lower()
