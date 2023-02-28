f = open("intervale.txt")


def citire(f):
    intervale = []
    linie = f.readline()
    while linie != "":
        intervale.append(tuple(int(x) for x in linie.split()))
        linie = f.readline()
    f.close()
    return intervale


intervale = citire(f)

intervale.sort(key=lambda x: (x[0], -x[1]))



def reuniunire(intervale):
    reuniune = [[intervale[0][0], intervale[0][1]]]
    contorreuniune = 0
    for i in intervale[1:]:
        if i[0] > reuniune[contorreuniune][1]:
            reuniune.append(list(i))
            contorreuniune += 1
        else:
            reuniune[contorreuniune] = [min(reuniune[contorreuniune][0], i[0]), max(reuniune[contorreuniune][1], i[1])]
    return reuniune

reuniune = reuniunire(intervale)
lungreun = 0
for i in reuniune:
    lungreun += i[1]-i[0]
print(f"Reuniunea este formata din intervalele: {reuniune}\n Lungimea totala a acestora este {lungreun}")