#Zadatak 2: Sortiranje stringova po dužini
#Napiši Python funkciju koja sortira listu stringova po dužini stringova, od najkraćeg do najdužeg.


def izdvoji_po_duzini(s):
    
    return len(s)


def sortiraj_pod_duzini(lista):
    
    return sorted(lista , key=izdvoji_po_duzini)
                           
            
            
rijeci = ["jabuka", "banana", "kivi", "ananas"]


print(sortiraj_pod_duzini(rijeci))