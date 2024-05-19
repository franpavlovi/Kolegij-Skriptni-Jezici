#Problem: Za dani prirodni broj n generiraj listu svih potencija od 2 manji od n. Npr. za n = 100 se vraća [1, 2, 4, 8, 16, 32, 64]
#Ulaz: prirodni broj n
#Izlaz: lista brojeva


def lista_potencija(n):
    
    lista = []
    
    for i in range(1,n):
        potencija = 2 ** i
        lista.append(potencija)
        
        
    return lista


rezultat = lista_potencija(10)

print(rezultat)


