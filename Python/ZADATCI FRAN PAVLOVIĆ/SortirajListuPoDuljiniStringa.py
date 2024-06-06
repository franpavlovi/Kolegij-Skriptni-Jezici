#Sortiranje listi:
#Napiši funkciju sortiraj_po_duljini(stringovi) koja sortira listu stringova po duljini stringa.


def sortiraj_po_duljini(stringovi):
    
    
    stringovi.sort(key=len)
        
    
    return stringovi
        
        
            

    

lista_stringova = [ 'Ana voli milovana' , 'Odabrao Đelo Hadžiselimović' , 'Dobar dan'
                    , 'Večernji list' , 'Sveučilište u Mostaru' , 'Kolegij Skriptni Jezici' ]


print(sortiraj_po_duljini(lista_stringova))

