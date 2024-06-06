#Manipulacija stringovima:
#Napiši funkciju ukloni_samoglasnike(string) koja prima string i vraća isti string s uklonjenim svim samoglasnicima (a, e, i, o, u).

def ukloni_samoglasnike(s):
    
    samogl = 'aeiouAEIOU'
    
    for slovo in s:
        
        if slovo in samogl:
            s = s.replace(slovo,' ')
            
            
    return s
    
    


string = 'svegamegabratemoj'

print(ukloni_samoglasnike(string))