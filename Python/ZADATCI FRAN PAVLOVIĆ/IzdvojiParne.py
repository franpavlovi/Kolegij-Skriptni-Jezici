#Zadatak 1: Napiši Python funkciju koja prima listu brojeva i vraća novu
#listu koja sadrži samo parne brojeve iz originalne liste.


def izdvoji_parne(lista):
    
    parni_brojevi = []
    
    for i in lista:
        
        if i % 2 == 0:
            
            parni_brojevi.append(i)
            
            
    return parni_brojevi
            

    
brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(izdvoji_parne(brojevi))