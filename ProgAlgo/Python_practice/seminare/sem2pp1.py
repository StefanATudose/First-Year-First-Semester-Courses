w = input("dati cuvant: ")

s = input("dati un sir de cuvinte: ").split()
afisare = []
for i in s:
    if len(i) == len(w):
        afisare.append(i)

print(" ".join(afisare))