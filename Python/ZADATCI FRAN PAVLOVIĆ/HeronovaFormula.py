import math

#Problem: Za dane tri stranice trokuta vratiti njegovu površinu (ako a, b i c definiraju trokut)
#Ulaz: stranice trokuta su brojevi
#Izlaz: broj koji predstavlja površinu trokuta
#Podproplemi:
#Heronova formula za površinu trokuta
#Uvjet trokuta: zbroj bilo koje dvije stranica trokuta mora biti veći ili jednak trećoj stranici

def trokut(a , b , c):
    
    povrsina = 0;
    
    if a+b>=c and b+c>=a and a+c>=b:
        povrsina=a*b*c
    else:
        print("Unesene duzine stranica ne mogu tvoriti trokut")
    
        
        
    return povrsina


rezultat=trokut(5,4,3)
print(rezultat)
        




