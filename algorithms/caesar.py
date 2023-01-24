from constants.constants import LETTERS

SHIFT = 11


def encrypt(text):
    translated = ''
    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num + SHIFT
            if num > len(LETTERS) - 1:
                num = num - len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    return translated


def decrypt(text):
    translated = ''
    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - SHIFT
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    return translated
