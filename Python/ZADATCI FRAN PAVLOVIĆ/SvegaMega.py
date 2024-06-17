#Za danu listu stringova, vrati rječnik čiji će ključevi biti znakovi iz stringova, a vrijednosti
#lista stringova koji sadrže taj znak po redoslijedu pojavljivanja u originalnom stringu.
#Napravite vlastitu funkciju,
#Npr. za listu ['dobar','dan'] će se dobiti rječnik
#{'d': ['dobar', 'dan'], 'o': ['dobar'],'b':['dobar'],'a':['dobar', 'dan'], 'r': ['dobar'], 'n': ['dan']}

def nova(l):
    
    rjecnik = {}
    
    for rijec in l:
        
        for slovo in rijec:
            
            if slovo not in rjecnik:
                rjecnik[slovo] = []
            
            if rijec not in rjecnik[slovo]:
                rjecnik[slovo].append(rijec)
    
    return rjecnik


lista = ['dobar' , 'dan']

rezultat = nova(lista)

print(rezultat)