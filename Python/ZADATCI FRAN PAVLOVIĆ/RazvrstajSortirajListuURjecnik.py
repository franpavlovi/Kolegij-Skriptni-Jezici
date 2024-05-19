#Problem: Za danu listu brojeva stvori rječnik u kojemu ćeš imati podlistu parnih i podlistu neparnih brojeva sortiranih uzlazno, Npr. za [4,5,1,3,2] se dobije rječnik {'parni': [2,4], 'neparni': [1,3,5]}
#Ulaz: lista brojeva
#Izlaz: rječnik s dva elementa 'parni' i 'neparni'
#Podproblemi:
#stvori rječnik s ključevima 'parni' i 'neparni' čije su vrijednosti prazne liste
#za svaki broj iz dane liste provjeri jeli paran ili neparan i ovisno o tome ga dodaj u rječnik
#sortiraj liste parnih i neparnih u rječniku

def razdvoji(lista):
    
    rjecnik = {
        
        'parni': [],
        'neparni': []
        
        }
    
    for broj in lista:
        
        if broj % 2 == 0:
            
            rjecnik['parni'].append(broj)
        
        else:
            
            rjecnik['neparni'].append(broj)
            
    
    rjecnik['parni'] = sorted(rjecnik['parni'])
    rjecnik['neparni'] = sorted(rjecnik['neparni'])
    
    return rjecnik



brojevi = [11,7,9,8,76,5,3,2,33,22,28,44,17,15,12]

razvrstaj_brojeve = razdvoji(brojevi)

print(razvrstaj_brojeve)