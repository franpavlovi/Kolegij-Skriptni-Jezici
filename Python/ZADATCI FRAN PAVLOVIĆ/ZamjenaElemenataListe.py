#Problem: Za danu listu brojeva zamjeni svaki broj djeljiv s 3 stringom '*'.Npr. za [1,2,3,4,5,6,7,8,9] se dobiva [1,2,'*',4,5,'*', 7,8,'*’]
#Ulaz: lista brojeva
#Izlaz: lista brojeva


lista = [1,2,3,4,5,6,7,8,9]

nova_lista = []


for i in lista:
    
    if i % 3 == 0:
        nova_lista.append('*')
        
    else:
        nova_lista.append(i)
        
        
        
print(nova_lista)
        
