#Ispis prostih brojeva:
#Napiši funkciju prosti_brojevi(n) koja prima broj n i ispisuje sve proste brojeve manje od tog broja.


def prosti_brojevi(n):
    
    brojevi = []
    
    for broj in range (2,n):
        
        if prost(broj):
            
            brojevi.append(broj)
            
    
    return brojevi
            
            

def prost(m):
    
    brojac = 0
    
    for i in range (2,m):
        
        if m % i == 0:
            
            brojac += 1
            
    
    if brojac == 0:
        
        return True
    
    elif brojac >= 1:
         
        return False
    
    
        
        

print(prosti_brojevi(20))
        