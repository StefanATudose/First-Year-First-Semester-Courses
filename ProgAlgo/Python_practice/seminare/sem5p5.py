f = open("proiecte.in")


def citire(f):
    proiecte = []
    linie = f.readline()
    zimax = 0
    while linie != "":
        proiecte.append((linie.split()[0],) +  tuple(int(i) for i in linie.split()[1:]))
        if proiecte[len(proiecte)-1][1] > zimax:
            zimax = proiecte[len(proiecte)-1][1]
        linie = f.readline()
    f.close()
    return proiecte, zimax
proiecte, zimax = citire(f)

proiecte.sort(key = lambda x: -x[2])
zile = [0] * zimax
profit = 0
for i in proiecte:
    for j in range(i[1]-1, -1, -1):
        if zile[j] == 0:
            zile[j] = [i[0], i[2]]
            profit += i[2]
            break

f = open("proiecte.out", "w")

def afisare(f, profit, zile):
    for i in range(len(zile)):
        if zile[i] != 0:
            f.write("Ziua {}: {} {}\n".format(i+1, zile[i][0], zile[i][1]))
    f.write("\nProfit maxim {}".format(profit))

afisare(f, profit, zile)
f.close()