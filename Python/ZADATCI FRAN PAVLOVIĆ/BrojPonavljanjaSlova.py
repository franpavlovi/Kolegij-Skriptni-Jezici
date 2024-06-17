#Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem
#dvije znamenke jednake prvoj znamenci.
#Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2

def provjeri(l):
    
    brojac = 0
    
    broj_ponavljanja = 0
    
    for rijec in l:
        
        if len(rijec) >= 3:
            
            prvo_slovo = rijec[0]
            
            
            for slovo in rijec:
                if slovo == prvo_slovo:
                    broj_ponavljanja +=1
            
            
        
            if broj_ponavljanja >= 2:
                brojac += 1
        
    
    return brojac


lista =['abc', 'aba', 'cc', 'ijki']

rezultat = provjeri(lista)

print(rezultat)