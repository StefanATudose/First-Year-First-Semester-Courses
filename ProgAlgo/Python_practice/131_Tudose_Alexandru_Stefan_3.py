# Nume si prenume: Tudose Alexandru-Stefan
# Grupa: 131
# Enunt:
# Se consideră fișierul text catalog.in cu următoarea structură:
# • pe prima linie apare numărul n reprezentând numărul de elevi dintr-o clasă a unui liceu
# • pe următoarele linii avem informații despre cei n elevi, respectiv pentru fiecare elev
# informațiile sunt structurate astfel:
# ▪ linie de forma <șir de caractere> <m>, unde șirul de caractere este numele elevului (acesta
# este unic), iar m este un număr natural reprezentând numărul de materii
# ▪ urmată de m linii care conțin notele elevului (numere naturale) la m materii, fiecare având
# următoarea structură:
# <nume_materie>,<nota_1>,<nota_2>,...,<nota_k>
# Observație: Orice elev are la fiecare materie cel puțin o notă, iar denumirile materiilor nu conțin
# caracterul ',' (virgula).
# Exemplu de fișier de intrare:
# 5
# Ana Maria Pop 3
# Matematica,10,9,9,10,10
# Limba romana,8,9,9,8
# Fizica,10,9,7,10,10
# Mihai Popescu 3
# Matematica,9,7,10,10
# Limba romana,8,3,5,10
# Fizica,10,10
# Andrei Mincu 2
# Matematica,10,9,2
# Fizica,3,7,9
# Ioana Matei 3
# Fizica,10,10
# Matematica,10,10,10,9
# Limba romana,9,9,10,10
# Alin Enache 3
# Limba romana,10,10,10
# Matematica,10,10,10,10
# Fizica,10
# Cerințe:
# a) [2 p.] Scrieți o funcție care citește datele din fișierul catalog.in și returnează o structură de
# date cu informațiile din fișier. Folosiți o structură de date convenabilă pentru a rezolva
# eficient subpunctele următoare.
# b) [1 p.] Scrieți o funcție detalii_elev care primește ca parametri structura în care s-au memorat
# datele la cerința a) și un șir de caractere reprezentând numele unui elev și returnează mediile
# la toate materiile elevului cu numele primit ca parametru, memorate sub formă de listă de
# tupluri de tipul (nume_materie, medie). Dacă un elev are o singură notă la o materie sau
# media este mai mică strict decât 5, acesta va avea media egală cu 0 și va rămâne corigent. Să
# se citească de la tastatură numele unui elev și să se afișeze pe ecran mediile acestuia
# (rotunjite cu două zecimale) la fiecare materie (sortate lexicografic) folosind această funcție.
# Exemplu:
# Intrare tastatură: Afișare pe ecran:
# Ana Maria Pop Fizica 9.20
# Limba romana 8.50
# Matematica 9.60
# c) [1 p.] Scrieți o funcție clasament care primește structura de date în care s-au memorat datele
# la cerința a) și un număr variabil de parametri de tip șir de caractere reprezentând nume de
# elevi. Funcția returnează o listă de tupluri de tipul (nume_elev, medie_generala) cu mediile
# generale ale elevilor ale căror nume au fost primite ca parametru ordonată descrescător după
# medii. Media generală a unui elev este egală cu media aritmetică a mediilor de la fiecare
# materie, dacă acesta nu este corigent, altfel media este 0.
# Exemplu: Dacă se apelează funcția pentru elevii Alin Enache și Ioana Matei se va returna lista
# [(Ioana Matei,9.75), (Alin Enache,0)], deoarece Alin Enache are o singură notă la
# fizică, deci este corigent.

path = "catalog.in"

def citire_date(path):
    date_elevi = {}
    f = open(path)
    nrelevi = int(f.readline())
    for i in range(nrelevi):
        linie = f.readline().split()
        nrmateriielevcurent = linie[len(linie)-1]
        linie.remove(nrmateriielevcurent)
        elevcurent = " ".join(linie)
        for j in range(int(nrmateriielevcurent)):
            linie = f.readline().split(",")
            materiecurenta = linie[0]
            note = tuple(int(x) for x in linie[1:])
            if elevcurent not in date_elevi:
                date_elevi[elevcurent] = {materiecurenta: note}
            else:
                date_elevi[elevcurent][materiecurenta] = note

    return date_elevi

date_elevi = citire_date(path)

nume = input("Introduceti, va rog, numele unui elev: ")
def detalii_elev(date_elevi, nume):
    medii = []
    for i in date_elevi[nume]:
        if len(date_elevi[nume][i]) == 1:
            medii.append((i, 0))
        else:
            mediecurenta = sum(date_elevi[nume][i])/len(date_elevi[nume][i])
            mediecurenta = "{:.2f}".format(mediecurenta)
            medii.append((i, mediecurenta))
    medii.sort()
    return medii

mediielev = detalii_elev(date_elevi, nume)

for i in mediielev:
    print(f"{i[0]} {i[1]}")