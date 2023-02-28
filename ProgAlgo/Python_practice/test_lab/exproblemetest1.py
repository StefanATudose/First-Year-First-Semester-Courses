path = input("dati locatia si numele fisierului: ")

def min_max(lista):
    return min(lista), max(lista)

def incarca_fisier(path):
    f = open(path)
    linie = f.readline()
    lfinala = []
    while linie != "":
        lfinala.append([int(x) for x in linie.split()])
        linie = f.readline()
    f.close()
    return lfinala

ltotala = incarca_fisier(path)
indici = []
minglobal = min(ltotala[0])
maxglobal = max(ltotala[1])
for i in range(len(ltotala)):
    mini, maxi = min_max(ltotala[i])
    if mini < minglobal:
        minglobal = mini
    if maxi > maxglobal:
        maxglobal = maxi
    if mini == maxi:
        indici.append(i)

f = open("test_lab/egale.txt", "w")
if indici == []:
    f.write("Nu exista!")
else:
    for i in indici:
        f.write(f"{str(i)}\n")
f.close()
print(minglobal, maxglobal)
