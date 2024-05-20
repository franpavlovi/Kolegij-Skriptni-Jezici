#generiraj listu od 50 brojeva koristenjem random funkcije
#nakon toga napravi rjecnik u kojem ces pohranjivati frekvencije nekog broja u listi
#u svim elementima , za kljuc koristi brojeve umjesto stringova

import random

def brojevi():
    
    lista_brojeva = random.sample(range(1,51), 50)
    
    return lista_brojeva


def provjera_frekvencija(lista):
    
    frekvencije = {str(i): 0 for i in range(10)}
    
    for broj in lista:
        for znamenka in str(broj):
            frekvencije[znamenka] += 1
            
    
    return frekvencije
        



listabr = brojevi()
print(listabr)

rezultat_provjere = provjera_frekvencija(listabr)
print("\n")
print(rezultat_provjere)
