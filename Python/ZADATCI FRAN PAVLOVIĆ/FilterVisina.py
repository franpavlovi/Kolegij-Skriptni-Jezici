#Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat
#daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira.
#(primjer: filtrira sve osobe koje su vece od odredene visine)
#Rjecnik:{'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190}


def filter_visine(r,mv):
    
    zadovoljili = {}
    
    for ime,visina in r.items():
        
        if visina > mv:
            
            zadovoljili[ime] = visina
            
    
    return zadovoljili
            
            
            

rjecnik = {'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165,
           'Marija Maric': 190 , 'Niko Nikic': 185 , 'Ante Antic': 195}

minimalna_visina = 180



print(filter_visine(rjecnik,minimalna_visina))