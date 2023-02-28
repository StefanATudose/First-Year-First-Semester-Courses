path = "matrice.txt"

def citirematrice(path):
    f = open(path)
    linie = f.readline()
    matrice = []
    elemliniei = linie.split()
    linie = f.readline()
    lung = len(elemliniei)
    while linie != "":
        elemliniei = linie.split()
        if len(elemliniei) != lung:
            return None
        matrice.append([int(x) for x in elemliniei])
        linie = f.readline()

    f.close()
    return matrice
matrice = citirematrice(path)


def multimi(matrice, *indici):
    negative = set(x for x in matrice[indici[0]] if x < 0)
    primult = set(x for x in matrice[indici[0]] if x % 10 == int(str(x)[0]))
    for i in indici[1:]:
        negativecurent = set(x for x in matrice[i] if x < 0)
        primultcurent = set(x for x in matrice[i] if x % 10 == int(str(x).strip("-")[0]))
        negative.intersection_update(negativecurent)
        primult = primult.union(primultcurent)
    return negative, primult

print(multimi(matrice, 0, 1, 2))