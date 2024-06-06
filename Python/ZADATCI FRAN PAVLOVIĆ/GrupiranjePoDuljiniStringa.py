#Grupiranje po duljini stringa:
#Napiši funkciju grupiraj_po_duljini(lista_stringova) koja grupira stringove po njihovoj duljini i vraća rječnik gdje su ključevi duljine,
#a vrijednosti liste stringova te duljine


def grupiraj_po_duljini(lista_stringova):
    
    rjecnik = {}
    
    for string in lista_stringova:
        
        duljina = len(string)
        
        if duljina not in rjecnik:
            
            rjecnik[duljina] = []
            
        rjecnik[duljina].append(string)
        
    
    return rjecnik



lista_stringova = ["mačka", "pas", "krokodil", "ptica", "riba", "slon"]

print(grupiraj_po_duljini(lista_stringova))
