#Zadatak 3: Filtriranje rječnika
#Napiši Python funkciju koja prima rječnik i vraća novi rječnik koji sadrži samo 
#one parove ključ-vrijednost gdje je vrijednost veća od 10.

def filtriraj_vrijednosti(r):
    
    filtrirani_rjecnik = {}
    
    for kljuc, vrijednost in r.items():
        
        if vrijednost > 10:
            
            filtrirani_rjecnik[kljuc] = vrijednost
            
    
    return filtrirani_rjecnik
            
    

rjecnik = {
           "a": 5,
           "b": 15,
           "c": 10,
           "d": 25
          }


print(filtriraj_vrijednosti(rjecnik))