f = open("numere.txt", "r")

primalinie = set(f.readline().split())
linie = f.readline()
while linie != "":
    primalinie.intersection_update(linie)
    linie = f.readline()
f.close()

r = open("numere_comune.txt", "w")

for i in primalinie:
    r.write(i + " ")

r.close()
