from . import random_ as random
def __letter_type(string:str, type:int):
    if type == 1:
        return string.lower()
    else:
        return string.upper()

def generate(caracteres:int):
    lista:list[str] = list()
    for _ in range(caracteres):
        n1 = random.randint(1, 3)
        if n1 == 1:
            lista.append(str(random.randint(1, 9)))
        else:
            letter = random.randletter()
            n2 = random.randint(1, 2)
            lista.append(__letter_type(letter, n2))

    return ''.join(lista)
