#dinamica

nrtrepte = int(input("dati un numar de trepte: "))
taxe = input("dati taxele treptelor toate pe o linie: ")
costsar = input("dati costurile sariturilor toate pe o linie: ")
taxe = [int(x) for x in taxe.split()]
costsar = [int(x) for x in costsar.split()]

costsar.insert(0, 0)
taxe.insert(0, 0)
costmin = [10000] * (nrtrepte+1)
costmin[0] = 0
costmin[1] = taxe[1] + costsar[1]
ult = [0] * (nrtrepte+1)
ult[0] = -1

for i in range(2, nrtrepte+1):
    for j in range(1, i+1):
        if costmin[i] > costmin[i-j] + costsar[j] + taxe[i]:
            costmin[i] = costmin[i-j] + costsar[j] + taxe[i]
            ult[i] = i-j
sol = []
print(f"taxa totala {costmin[nrtrepte]} pentru traseul cu scarile")
while nrtrepte != -1:
    sol.append(nrtrepte)
    nrtrepte = ult[nrtrepte]

sol.reverse()
for i in sol:
    print(i, end = ' ')