#Zadatak: Filtriranje liste rječnika
#Napiši Python funkciju koja prima listu rječnika i ključ,
#te vraća novu listu rječnika koja sadrži samo one rječnike koji sadrže zadani ključ.

#Na primjer, ako imamo listu rječnika koja sadrži podatke o osobama,
#a želimo filtrirati samo one rječnike koji sadrže informacije o dobi (ključ "dob"),
#funkcija bi trebala vratiti novu listu s tim rječnicima.


def filtriraj_listu(rjecnik, kljuc):
    
    nova_lista = []
    
    for rjecnici in osobe:
        
        for kljucevi in rjecnici.keys():
            
            if kljucevi == kljuc:
                
                nova_lista.append(rjecnici)
                
    
    return nova_lista
                
                
                
                
        
osobe = [
    {"ime": "Ana", "prezime": "Anić", "godine": 25},
    {"ime": "Ivan", "prezime": "Ivanić", "godine": 30},
    {"ime": "Petra", "prezime": "Petrović", "grad": "Zagreb"}
]

kljuc = "godine"


print(filtriraj_listu(osobe, kljuc))