#Problem: Uz pomoć danog dvojezičnog rječnika prijevoda prevedi božićne i novogodišnje čestitke s hrvatskog na engleski jezik
#Ulaz: rječnik prijevoda, čestitka na hrvatskom
#Izlaz: čestitka na engleskom
#Podproblemi
#rečenicu na hrvatskom jeziku razbiti na listu riječi
#za svaku riječ iz liste riječi na hrvatskom pronaći njen prijevod i ubaciti je u novu listu riječi na engleskom jeziku
#spojiti listu riječi na engleskom jeziku u rečenicu na engleskom jeziku


prijevod = {
  'sretan': 'happy',
  'sretna': 'happy',
  'nova': 'new',
  'godina': 'year',
  'čestit': 'merry',
  'božić': 'christmas',
  'i': 'and'
}


recenica = 'sretna nova godina'

lista_hrvatski = []

lista_engleski = []

lista_hrvatski = recenica.split(' ')
print(lista_hrvatski)

for rijec in lista_hrvatski:
    
    if rijec in prijevod:
        lista_engleski.append(prijevod[rijec])
    else:
        lista_engleski.append(rijec)
        

print(lista_engleski)