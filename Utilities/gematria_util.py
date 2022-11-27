#!/usr/bin/env python
# Forked from: https://github.com/ironsmile/gematria
import argparse
import math
import sys

alphabets = {
    "he": {
        "א": 1,
        "ב": 2,
        "ג": 3,
        "ד": 4,
        "ה": 5,
        "ו": 6,
        "ז": 7,
        "ח": 8,
        "ט": 9,
        "י": 10,
        "כ": 11,
        "ל": 12,
        "מ": 13,
        "נ": 14,
        "ס": 15,
        "ע": 16,
        "פ": 17,
        "צ": 18,
        "ק": 19,
        "ר": 20,
        "ש": 21,
        "ת": 22,
        "ך": 23,
        "ם": 24,
        "ן": 25,
        "ף": 26,
        "ץ": 27,
    },

    "en": {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    },
}

def letterToNumber(x):
    return (math.pow(10, math.floor((x-1)/9))) * (((x-1) % 9) + 1)

def nameToNumber(name, language):
    sum = 0
    for letter in name.lower():
        if letter in [' ', '']:
            continue
        sum += int(letterToNumber(alphabets[language][letter]))
    return sum

if __name__ == "__main__":
    lang = "he"
    
    for char in alphabets[lang]:
        print(f'Letter: {char}  Value: {letterToNumber(alphabets[lang][char])}')
    