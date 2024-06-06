#Sortiranje rječnika po vrijednostima:
#Napiši funkciju sortiraj_po_vrijednostima(rjecnik) koja prima rječnik i vraća rječnik sortiran po vrijednostima

def sortiraj_po_vrijednostima(rjecnik):
    
    sorted_rjecnik = dict(sorted(rjecnik.items(), key=lambda item: item[1]))
    
    return sorted_rjecnik




r = {1:10 , 2:15, 3:18, 4:22, 4:28}

print(sortiraj_po_vrijednostima(r))