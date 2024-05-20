#napisi program i funckiju loto koja simulira loto 6/45 koja izvlaci brojeve preko random generatora
#funkcija vraca listu loto brojeva,osim funkcije loto morate napraviti i funkciju brojevi_igraca
#koja ce provejravati koliko je brojeva pogodjeno
#brojeve igraca mozete unijeti pri inicijalizaciji

import random

def loto():
    
    brojevi = random.sample(range(1,46), 6)
    
    return brojevi
    
    

def brojevi_igraca(zaokruzeni_brojevi , loto_brojevi):
    
    pogodjeni = []
    
    for brojeviL in loto_brojevi:
        
        for brojeviI in zaokruzeni_brojevi:
            
            if brojeviL == brojeviI:
                
                pogodjeni.append(brojeviI)
            
            
                      
    return pogodjeni
    
    


igrac1 = [2,11,13,22,26,33]
igrac2 = [4,9,17,24,39,41]
igrac3 = [28,8,12,3,30,44]
igrac4 = [22,3,43,34,7,8]
igrac5 = [1,7,16,27,31,44]


rezultat_lota = loto()

pogodjeni_igrac1 = brojevi_igraca(igrac1,rezultat_lota)
pogodjeni_igrac2 = brojevi_igraca(igrac2,rezultat_lota)
pogodjeni_igrac3 = brojevi_igraca(igrac3,rezultat_lota)
pogodjeni_igrac4 = brojevi_igraca(igrac4,rezultat_lota)
pogodjeni_igrac5 = brojevi_igraca(igrac5,rezultat_lota)

print(f"Izvuceni brojevi su {rezultat_lota} \n")

print(f"igrac1 je igrao {igrac1} i pogodio {pogodjeni_igrac1}")
print(f"igrac2 je igrao {igrac2} i pogodio {pogodjeni_igrac2}")
print(f"igrac3 je igrao {igrac3} i pogodio {pogodjeni_igrac3}")
print(f"igrac4 je igrao {igrac4} i pogodio {pogodjeni_igrac4}")
print(f"igrac5 je igrao {igrac5} i pogodio {pogodjeni_igrac5}")

