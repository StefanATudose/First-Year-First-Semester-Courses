import copy

f = open("ModelEx/matrice.txt")
linie = f.readline().split()
n, m = int(linie[0]), int(linie[1])
linie = f.readline()
matrice = [[0] * (m+2)]
i = 1
while linie != "":
    matrice.append([0])
    matrice[i].extend([int(x) for x in linie.split()])
    matrice[i].append(0)
    i += 1
    linie = f.readline()
matrice.append([0] * (m+2))
f.close()


drummax = copy.deepcopy(matrice)

maxu = 0
imax = 0
jmax = 0
for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        max1 = 0
        max2 = 0
        if matrice[i][j] == matrice[i+1][j] + 1 or matrice[i][j] == matrice[i+1][j] - 1:
            max1 = drummax[i+1][j]
        if matrice[i][j] == matrice[i][j+1] + 1 or matrice[i][j] == matrice[i][j+1] - 1:
            max2 = drummax[i][j+1]
        drummax[i][j] = max(1, max1+1, max2+1)
        if drummax[i][j] > maxu:
            maxu = drummax[i][j]
            imax = i
            jmax = j
aici = 0
while True:
    print(imax, jmax)
    if drummax[imax][jmax] == 1:
        break
    elif drummax[imax+1][jmax] == drummax[imax][jmax] - 1:
        imax += 1
    elif drummax[imax][jmax+1] == drummax[imax][jmax] - 1:
        jmax += 1
