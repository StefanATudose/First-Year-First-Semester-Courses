# Nume si prenume: Tudose Alexandru-Stefan
# Grupa: 131
# Enunt:
# [4 p.] Fișierul text numere.in conține, pe fiecare linie, câte un șir de numere întregi despărțite
# prin spații. Să se scrie în fișierul text numere.out șirurile din fișierul de intrare grupate în
# funcție de suma elementelor lor, conform modelului din exemplul de mai jos. Grupele de
# șiruri vor fi scrise în ordinea crescătoare a sumelor elementelor lor, iar în fiecare grupă șirurile
# se vor scrie în ordinea descrescătoare a numărului de elemente.

f = open("numere.in")
linie = f.readline()
date = []
while linie != "":
    date.append([int(x) for x in linie.split()])
    linie = f.readline()
f.close()

dupasume = {}
for i in date:
    suma = sum(i)
    if suma not in dupasume:
        dupasume[suma] = [i]
    else:
        dupasume[suma].append(i)
print(dupasume)

cheiinverse = sorted(dupasume)
for i in cheiinverse:
        dupasume[i] = sorted(dupasume[i], key = len, reverse = True)

f = open("numere.out", "w")
for i in cheiinverse:
    f.write(f"Suma {i}:\n")
    for j in dupasume[i]:
        for k in j:
            f.write(f"{str(k)} ")
        f.write("\n")


f.close()