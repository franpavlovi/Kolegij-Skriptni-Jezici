#Problem: za dani broj redaka kvadratne matrice, vrati matricu koja ima jedinice na obje dijagonale,
#a sve ostale vrijednosti su 0.Npr. za n = 5 dobije se

def kvadratna_matrica(n):
    
    matrica = [ [0 for i in range(n)] for i in range(n) ]
    
    for i in range(n):
        matrica[i][i] = 1
        matrica[i][-1-i] = 1
        
    return matrica


rezultat = kvadratna_matrica(5)
print(rezultat)
