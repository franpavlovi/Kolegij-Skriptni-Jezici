#Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar
#liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30.
#Primjer ulaza: [4, 6, 6, 6, 3, 8, 21, 21,21, 7, ...]

import random


def provjeri_ponavljanje(l):
    
    obradjeni = []
    
    for broj in l:
        if broj in obradjeni:
            continue
    
        brojac=0;
        
        for brojevi in l:
            
            if broj == brojevi:
                brojac+=1
        
        if brojac >= 3:
            print (f"{broj} se ponavlja {brojac} puta")
        
        obradjeni.append(broj)
        

lista = random.choices(range(1,31), k=100)

print(lista)

provjeri_ponavljanje(lista)