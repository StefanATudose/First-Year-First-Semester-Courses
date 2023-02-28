# Nume si prenume: Tudose Alexandru-Stefan
# Grupa: 131
# Enunt:
# Fișierul "date.in" are n linii cu următoarea structură: pe linia i sunt prezente, separate prin câte
# un spațiu, n numere naturale reprezentând elementele de pe linia i dintr-o matrice, ca în
# exemplul de mai jos.
# Liniile și coloanele unei matrice se presupun numerotate de la 0.
# a) [0,25p] Scrieți o funcție citire_matrice care citește numerele din fișierul "date.in" și returnează
# o matrice de dimensiuni n x n formată din aceste numere.
# b) [1,5p] Scrieți o funcție care primește ca parametri: o matrice (listă de liste), un caracter ch care
# poate primi valoarea "c" sau "d" și doi parametri x și y cu valoare implicită 0 .
# Funcția va modifica matricea primită ca parametru astfel:
# ● Dacă al doilea parametru - caracterul ch - primește la apel valoarea "c", funcția
# interschimbă coloana x cu coloana y.
# ● Dacă al doilea parametru - caracterul ch - primește la apel valoarea "d", funcția nu va
# primi la apel decât 2 parametri și trebuie să interschimbe elementele de pe diagonala
# principală cu elementele de pe diagonala secundară.
# c) [1,25p] Folosind apeluri ale funcției definite la punctul b), oglindiți matricea returnată de
# funcția de la punctul a) după coloana de pe poziția [n / 2] și apoi interschimbați elementele de
# pe diagonala principală cu cele de pe diagonala secundară. După oglindire și interschimbare, să
# se parcurgă matricea în zig-zag pe linii și să se afișeze șirul obținut în fișierul "date.out" ca în
# exemplu. Se cunoaște faptul că n este impar.
# Explicație suplimentară : Parcurgerea în zig-zag pe linii se va face de sus în jos, astfel:
# ● prima linie se parcurge de la stânga la dreapta,
# ● a doua linie se parcurge de la dreapta la stânga,
# ● a treia linie se parcurge de la stânga la dreapta etc.

def citire_matrice(path):
    f = open(path)
    linie = f.readline()
    matrice = []
    while linie != "":
        matrice.append([int(x) for x in linie.split()])
        linie = f.readline()
    f.close()
    return matrice
path = "date.in"
matrice = citire_matrice(path)


def schimbare(matrice, ch, *xy):
    if ch == "c":
        x, y = xy
        colx = []
        coly = []
        for i in range(len(matrice)):
            colx.append(matrice[i][x])
            coly.append(matrice[i][y])
        for i in range(len(matrice)):
            matrice[i][x] = coly[i]
            matrice[i][y] = colx[i]
    if ch == "d":
        diagprinc = []
        diagsec = []
        for i in range(len(matrice)):
            diagprinc.append(matrice[i][i])
            diagsec.append(matrice[i][len(matrice)-i-1])
        for i in range(len(matrice)):
            matrice[i][i] = diagsec[i]
            matrice[i][len(matrice)-i-1] = diagprinc[i]

def oglindire(matrice):
    for i in range(len(matrice)//2):
        schimbare(matrice, "c", i, len(matrice)-i-1)
    schimbare(matrice, "d")
    f = open("date.out", "w")
    for i in range(len(matrice)):
        if i % 2 == 0:
            for j in range(len(matrice[i])):
                f.write(f"{matrice[i][j]} ")
        else:
            for j in range(len(matrice[i])-1, -1, -1):
                f.write(f"{matrice[i][j]} ")
    f.close()
oglindire(matrice)