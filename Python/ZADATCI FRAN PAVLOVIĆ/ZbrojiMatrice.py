#Zadatak 4: Sabiranje matrica
#Napiši Python funkciju koja prima dvije matrice (liste listi) istih dimenzija i vraća njihovu sumu

def zbroji_matrice(mat1, mat2):
    
    zbroj_matrica = []
    
    for i in range(len(mat1)):
        
        red = []
        
        for j in range(len(mat1[0])):
            
            red.append(mat1[i][j] + mat2[i][j])
            
            
        zbroj_matrica.append(red)
        
        
    return zbroj_matrica




mat1 = [
    [1, 2, 3],
    [4, 5, 6]
       ]

mat2 = [
    [7, 8, 9],
    [10, 11, 12]
       ]

print(zbroji_matrice(mat1, mat2))