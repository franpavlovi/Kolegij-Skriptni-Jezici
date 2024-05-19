#Problem:
#Za dani prirodni broj N generiraj listu svih parova gdje je prvi element prirodni broj manji od N
#a drugi element njegov kvadrat. Npr, za N = 4 dobije se lista [(1,1),(2,4),(3,9)]
#Zatim za navedenu listu generiraj listu brojeva čiji su elementi razlika drugog i prvog elementa.
#Npr. za [(1,1),(2,4),(3,9)] se dobije [0,2,6]


def lista_kvadrata(n):
    
    a = [(i,i**2) for i in range(1,n)]
    
    return a


def lista_razlika(m):
    
    b = [y-x for x,y in m]
    
    return b


rezultat = lista_kvadrata(5)
print(rezultat)

rezultat2 = lista_razlika(rezultat)
print(rezultat2)


