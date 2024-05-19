#Problem: dani broj u brojevnom sustavu s bazom 12 vrati vrijednost tog broja u dekadskom brojevnom sustavu
#Ulaz: broj u bazi 12 (predstavljen kao string, npr. b3a8)
#Izlaz: broj u bazi 10 (predstavljen kao integer)
#Podproblemi
#Kako uzimati znak po znak iz zadanog stringa?
#Kako provjeriti jeli znak broj ili slovo?
#Kako izvršiti pretvorbu iz baze 12 u bazu 10?


b10 = 0;
b12 = 'b3a8'

suma = 0

for i , broj in enumerate(reversed(b12)):
    
    if broj.isalpha():
        
        if broj == 'a':
            suma += 10*pow(12,i)
            
        elif broj == 'b':
            suma += 11*pow(12,i)
            
    else:
        suma += int(broj) * pow(12,i)
         
         
rezultat = suma
print(f"Broj {b12} u decimalnom sustavu iznosi {rezultat}")