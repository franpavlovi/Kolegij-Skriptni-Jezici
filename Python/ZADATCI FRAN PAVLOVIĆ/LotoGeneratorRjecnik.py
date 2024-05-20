#napisi program i funckiju loto koja simulira loto 6/45 koja izvlaci brojeve preko random generatora
#funkcija vraca listu loto brojeva,osim funkcije loto morate napraviti i funkciju brojevi_igraca
#koja ce provejravati koliko je brojeva pogodjeno
#brojeve igraca mozete unijeti pri inicijalizaciji

import random

def loto():
    
    brojevi = random.sample(range(1,46), 6);
    
    return brojevi


def brojevi_igraca(igraci , loto_brojevi):
    
    rezultati = {}
    
    for igraci , zaokruzeni_brojevi in igraci.items():
        
        pogodjeni = []
        
        for brojeviL in loto_brojevi:
            
            if brojeviL in zaokruzeni_brojevi:
                pogodjeni.append(brojeviL)
                
            
        rezultati[igraci] = pogodjeni
        
    
    
    return rezultati



igraci = {
    
    'Igrac1': [2,11,13,22,26,33],
    'Igrac2': [4,9,17,24,39,41],
    'Igrac3': [28,8,12,3,30,44],
    'Igrac4': [22,3,43,34,7,8],
    'Igrac5': [1,7,16,27,31,44]
    
    }



rezultat_lota = loto()
rezultati = brojevi_igraca(igraci,rezultat_lota)

print(f"Loto brojevi: {rezultat_lota}")

for igraci , pogodjeni in rezultati.items():
    print(f"{igraci}, pogodjeni brojevi: {pogodjeni}")