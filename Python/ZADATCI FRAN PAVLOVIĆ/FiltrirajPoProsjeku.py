#Za dani riječnik čiji su ključevi imena studenata, a vrijednosti ocjene. Vrijednosti trebaju
#biti u obliku ntorke. Potrebno je vratiti rječnik čiji će ključevi biti prosječna ocjena
#(zaokružena - koristiti round() funkciju),a vrijednosti sortirana lista studenata koji su
#dobili tu prosječnu ocjenu.
#Npr. u rječniku {'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}, 'ivan' ima ocjene 3, 2, 4 i
#prosječna ocjena je 3.0, 'marko' ima ocjene 5, 4 i prosječna ocjena je 4.0, 'ana' ima
#ocjene 2, 3, 4 i prosječna ocjena je 3.0.
#Izlazni rječnik će biti {3: ['ana', 'ivan'], 4: ['marko']} jer 'ivan' i 'ana' imaju prosjek 3.0, a'marko' prosjek 4

def filtriraj_po_prosjeku(rjecnik):
    prosjeci = {}
    
    for ime, ocjene in rjecnik.items():
        
        prosjek = sum(ocjene) / len(ocjene)
        prosjek = round(prosjek)  
        
        if prosjek not in prosjeci:
            prosjeci[prosjek] = []
        
        prosjeci[prosjek].append(ime)
    
    
    return prosjeci


studenti_ocjene = {'ivan': (3, 2, 4), 'marko': (5, 5, 4), 'ana': (2, 3, 4)}

rezultat = filtriraj_po_prosjeku(studenti_ocjene)
print(rezultat)

