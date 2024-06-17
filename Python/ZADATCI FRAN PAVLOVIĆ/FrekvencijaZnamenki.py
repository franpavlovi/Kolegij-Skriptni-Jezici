#Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu
#listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja
#određene brojčane znamenke u svim brojevima iz liste
#Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd
#Napomena: ključevi rječnika neka budu brojevi, a ne stringovi

import random



lista = random.choices(range(1,100), k=10)

print(lista)


rjecnik_frekvencija = {}

for broj in lista:
    
    str_broj = str(broj)
    
    for znamenka in str_broj:
        
        if znamenka in rjecnik_frekvencija:
            
            rjecnik_frekvencija[znamenka] +=1
        else:
            rjecnik_frekvencija[znamenka] = 1
    
    


print(rjecnik_frekvencija)
        
        
        
        



