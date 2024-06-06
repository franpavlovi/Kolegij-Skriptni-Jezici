#Uklanjanje duplikata iz liste:
#Napiši funkciju ukloni_duplikate(lista) koja vraća novu listu bez duplikata zadržavajući redoslijed elemenata.



def ukloni_duplikate(lista):
    
    viđeni = {}
    
    rezultat = []
    
    for element in lista:
        
        if element not in viđeni:
            
            viđeni[element] = True
            
            rezultat.append(element)
            
            
    return rezultat



lista = [1, 2, 3, 2, 4, 1, 5, 3, 6]

print(ukloni_duplikate(lista))
