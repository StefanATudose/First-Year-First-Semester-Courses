semnepct = ".,?!"

sir = input("buna ziua va rog dati un sir: ")

for i in range(len(sir)):
    if sir[i] in semnepct:
        sir = sir[:i] + " " + sir[i + 1:]

sir = sir.split()

maxim = 0
print("cuvintele de lungime maxima sunt: ", end = "")
for cuvinte in sir:
    if len(cuvinte) == maxim and cuvinte not in rez:
        rez += " " + cuvinte
    if len(cuvinte) > maxim:
        maxim = len(cuvinte)
        rez = cuvinte
print(rez)