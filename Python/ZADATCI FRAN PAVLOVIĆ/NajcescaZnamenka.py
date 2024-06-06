#Pronalaženje najčešće znamenke:
#Napiši funkciju koja prima listu brojeva i vraća znamenku koja se najčešće pojavljuje među svim znamenkama u listi.



def najcesca_znamenka(lista_brojeva):
    frekvencija = {}
    
    
    for broj u lista_brojeva:
        
        for znamenka u str(broj):
            
            if znamenka.isdigit():
                
                if znamenka in frekvencija:
                    frekvencija[znamenka] += 1
                else:
                    frekvencija[znamenka] = 1
    
    
    najcesca = max(frekvencija, key=frekvencija.get)
    
    return int(najcesca)



lista_brojeva = [123, 456, 789, 123, 456, 789, 123]

print(najcesca_znamenka(lista_brojeva))
