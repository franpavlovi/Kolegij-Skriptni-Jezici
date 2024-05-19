#Pronađi sve particije skupa S 
#Neka je S = {1, 2, 3, 4} 
#Particije od S su
#{}, 
#{1}, {2}, {3}, {4},
#{1,2}, {1,3}, {1,4}, {2,3}, {2,4},{3,4} 
#{1,2,3},{1,2,4},{1,3,4},{2,3,4} 
#{1,2,3,4}


def sve_particije(S):
    
    elementi = list(S)
    
    n = len(elementi)
    
    particije = []
    
    for i in range(1 << n):
        
        podskup = set()
        
        for j in range(n):
            
            if i & (1 << j):
                
                podskup.add(elementi[j])
                
        particije.append(podskup)
        
    
    return particije


S = {1, 2, 3, 4}
rezultat = sve_particije(S)


for podskup in rezultat:
    print(podskup)

