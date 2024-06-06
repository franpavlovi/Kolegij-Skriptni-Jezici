#Invertiranje rječnika:
#Napiši funkciju invertiraj_rjecnik(rjecnik) koja vraća novi rječnik gdje su ključevi i vrijednosti zamijenjeni.



def invertiraj_rjecnik(rjecnik):
    
    invertirani_rjecnik = {}
    
    for kljuc, vrijednost in rjecnik.items():
        
        invertirani_rjecnik[vrijednost] = kljuc
        
        
    return invertirani_rjecnik



r = {1: 10, 2: 15, 3: 18, 4: 22, 5: 28}

print(invertiraj_rjecnik(r))  
