#Napisi program i funkciju loto642 koja simulira loto 6/42.
#a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
#brojeva. Funkcija vraća listu loto brojeva.
#b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno).
#c. Potrebno je odrediti ukupan broj pogodataka pri izvlačenju i ispisati na ekran.

import random

def loto():
    loto_brojevi = random.sample(range(1, 43), 7)  
     
    return loto_brojevi 

def izvlacenje(loto_brojevi, igrac):
    
    pogodjeni = []
    
    for broj in igrac:
        
        if broj in loto_brojevi:
            pogodjeni.append(broj)
            
    return pogodjeni



igrac1 = [5, 23, 33, 15, 28, 11, 1]
igrac2 = [4, 8, 16, 25, 32, 28, 40]
igrac3 = [1, 9, 13, 21, 29, 25, 41]


loto_brojevi = loto()
print("Izvučeni loto brojevi:", loto_brojevi)


igrac1_pogodjeni = izvlacenje(loto_brojevi, igrac1)
igrac2_pogodjeni = izvlacenje(loto_brojevi, igrac2)
igrac3_pogodjeni = izvlacenje(loto_brojevi, igrac3)


print("Igrač 1 je pogodio:", igrac1_pogodjeni)
print("Igrač 2 je pogodio:", igrac2_pogodjeni)
print("Igrač 3 je pogodio:", igrac3_pogodjeni)



suma_pogodjenih = sum(igrac1_pogodjeni) + sum(igrac2_pogodjeni) + sum(igrac3_pogodjeni)
print("Suma pogođenih brojeva:", suma_pogodjenih)







