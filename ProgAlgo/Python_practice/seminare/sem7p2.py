f = open("seminare/sem7p1.txt")
sirinit = [int(x) for x in f.readline().split()]
f.close()

suma = sum(sirinit) // 2

nrelem = len(sirinit)
matrice = []

for i in range(nrelem+1):
    matricecurenta = [0] * suma
    matricecurenta.insert(0, 1)
    matrice.append(matricecurenta)

for i in range(1, nrelem+1):
    for j in range(1, suma+1):
        if (matrice[i-1][j] or (sirinit[i-1] <= j and matrice[i-1][j-sirinit[i-1]])):
            matrice[i][j] = 1
        print(matrice[i][j], end = ' ')
    print("")

for i in range(suma, -1, -1):
    if matrice[nrelem][i]:
        break


print(f"suma minima ceruta este {sum(sirinit) - 2 * i}")
elemx = []
elemy = []
while nrelem > 0:
    if matrice[nrelem][i] == matrice[nrelem-1][i]:
        elemy.append(sirinit[nrelem-1])
        nrelem -= 1
    else:
        elemx.append(sirinit[nrelem-1])
        nrelem -= 1
        i = i - sirinit[nrelem]
elemx = " ".join([str(x) for x in elemx])
elemy = " ".join([str(y) for y in elemy])

print("multimea x este {}".format(elemx))
print(f"multimea y este {elemy}")