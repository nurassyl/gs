def what_case(word):
    if word.upper() == word:
        return 'up'
    elif word[0].upper() == word[0]:
        return 'capitalize'
    else:
        return 'down'

def normalize(word, c='down'):
    if c == 'up':
        return word.upper()
    elif c == 'capitalize':
        return word.capitalize()
    else:
        return word.lower()
