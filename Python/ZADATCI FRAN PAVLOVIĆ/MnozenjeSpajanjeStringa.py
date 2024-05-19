#Problem: za dani string vrati string u kojemu je svaki znak zamijenjen s tri takva ista znaka. Npr, za "Problem" dobije se "PPPrrrooobbbllleeemmm“
#Ulaz i izlaz: string
#Podproblemi
#Kako uzimati znak po znak iz zadanog stringa?
#Kako utrostručiti znak?
#Kako nadopunjavati izlazni string utrostručenim znakom originalnog stringa?

s = 'Problem'
s2 = ''
i=0

for i in s:
    s2 = s2 + i*3


print(s2)