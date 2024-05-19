#Za dani prirodni broj n ispiši sumu svih parnih brojeva manjih od n

def suma_parnih(n):
    
    suma=0;
    i=0;
    
    while i < n:
        
        if i % 2 == 0:
            suma +=i
            
        i +=1  
          
    return suma;
    
    

rezultat=suma_parnih(10);
print(rezultat)
      
    
    
    
    
            
            
     
