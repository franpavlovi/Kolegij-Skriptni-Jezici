#generiraj listu od 50 brojeva koristenjem random funkcije
#nakon toga napravi rjecnik u kojem ces pohranjivati frekvencije nekog broja u listi
#u svim elementima , za kljuc koristi brojeve umjesto stringova

import random

def brojevi():
    
    lista_brojeva = random.sample(range(1,51), 50)
    
    return lista_brojeva


def provjera_frekvencija(lista):
    
    frekvencije = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        }
    
    for broj in lista:
        for znamenka in str(broj):
            frekvencije[znamenka] += 1
    
    return frekvencije
        



listabr = brojevi()
print(listabr)

rezultat_provjere = provjera_frekvencija(listabr)
print("\n")
print(rezultat_provjere)


