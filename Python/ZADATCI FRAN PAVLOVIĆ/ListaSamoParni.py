#Filtriranje listi:
#Napiši funkciju samo_parni(brojevi) koja prima listu brojeva i vraća novu listu koja sadrži samo parne brojeve.

def samo_parni(brojevi):
    
    lista_parnih = []
    
    for broj in brojevi:
        
        if broj % 2 == 0:
            
            lista_parnih.append(broj)
            
    
    return lista_parnih
            
    
    
    
lista = [ 3,4,5,6,13,42,52,34,57,87,33,28,1,11,10,15]

print(samo_parni(lista))