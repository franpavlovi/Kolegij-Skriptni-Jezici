#Za dani skup S nađi sve dvočlane podskupove od S 

def dvoclani_podskupovi(s):
    
    elementi = list(s)
    
    podskupovi = []
    
    for i in range(len(elementi)):
        
        for j in range(i + 1, len(elementi)):
            
            podskupovi.append((elementi[i], elementi[j]))
            
            
    return podskupovi


s = {1, 2, 3, 4}
rezultat = dvoclani_podskupovi(s)

print(rezultat)
