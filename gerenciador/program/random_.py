from random import *

def __randstr() -> str:
    letter = randint(1, 26)
    if letter == 1:
        retornar = 'a'
    if letter == 2:
        retornar = 'b'
    if letter == 3:
        retornar = 'c'
    if letter == 4:
        retornar = 'd'
    if letter == 5:
        retornar = 'e'
    if letter == 6:
        retornar = 'f'
    if letter == 7:
        retornar = 'g'
    if letter == 8:
        retornar = 'h'
    if letter == 9:
        retornar = 'i'
    if letter == 10:
        retornar = 'j'
    if letter == 11:
        retornar = 'z'
    if letter == 12:
        retornar = 'k'
    if letter == 13:
        retornar = 'l'
    if letter == 14:
        retornar = 'm'
    if letter == 15:
        retornar = 'n'
    if letter == 16:
        retornar = 'o'
    if letter == 17:
        retornar = 'p'
    if letter == 18:
        retornar = 'q'
    if letter == 19:
        retornar = 'r'
    if letter == 20:
        retornar = 's'
    if letter == 21:
        retornar = 't'
    if letter == 22:
        retornar = 'u'
    if letter == 23:
        retornar = 'v'
    if letter == 24:
        retornar = 'w'
    if letter == 25:
        retornar = 'x'
    if letter == 26:
        retornar = 'y'
    return retornar

randletter = __randstr
