#Sumiranje vrijednosti u rječniku:
#Napiši funkciju suma_vrijednosti(rjecnik) koja vraća zbroj svih vrijednosti u rječniku.



def suma_vrijednosti(rjecnik):
    
    return sum(rjecnik.values())



r = {1: 10, 2: 15, 3: 18, 4: 22, 5: 28}

print(suma_vrijednosti(r))  
