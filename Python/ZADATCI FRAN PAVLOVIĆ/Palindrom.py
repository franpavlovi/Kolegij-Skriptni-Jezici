#Provjera palindroma:
#Napiši funkciju je_palindrom(string) koja provjerava je li string palindrom (čita se isto sprijeda i straga).


def je_palindrom(s):
    
    bez_razmaka = s.replace(" ","")
    obrnuti_string = bez_razmaka[::-1]
    
    if bez_razmaka == obrnuti_string:
        
        return 'Palindrom je'
    
    else:
        
        return 'Nije palindrom'
    
    
    
    
r = 'ana voli milovana'
k = 'anja voli milovanja'
g = 'fakultet'


print(je_palindrom(r))
print(je_palindrom(k))
print(je_palindrom(g))