f = open("test_lab/spiridusi.in")

linie = f.readline()
lista = []
while linie != "":
    l1 = linie.split()
    lista.append([l1[0], int(l1[1]), l1[2]])
    linie = f.readline()
f.close()

def despre_spiridus(lista, cod):
    lspiridus = []
    for i in lista:
        if i[0] == cod:
            lspiridus.append((i[2], i[1]))
    lspiridus.sort(key = lambda r: (-r[1], r[0]))
    return lspiridus
print(despre_spiridus(lista, "S1"))

def jucarii(lista):
    jucarele = set()
    for i in lista:
        jucarele.add(i[2])
    return jucarele

jucarele = jucarii(lista)
print(", ".join(jucarele))

def spiridusi(lista):
    multspiridusi = set()
    spiridusiharnici = []
    for i in lista:
        multspiridusi.add(i[0])
    for i in multspiridusi:
        multjucarelespiridus = set()
        nrjucarele = 0
        harnicie = 0
        datespiridus = despre_spiridus(lista, i)
        for j in datespiridus:
            if j[0] not in multjucarelespiridus:
                multjucarelespiridus.add(j[0])
                nrjucarele+= 1
            harnicie += j[1]
        spiridusiharnici.append((i, nrjucarele, harnicie))
    spiridusiharnici.sort(key = lambda i: (-i[1], -i[2], i[0]))
    return spiridusiharnici

spiridusiharnici = spiridusi(lista)
for i in spiridusiharnici:
    print(i)

def actualizare(lista, cod, jucarie):
    if len(despre_spiridus(lista, cod)) < 2:
        return False
    else:
        for i in lista:
            if i[0] == cod and i[2] == jucarie:
                lista.remove(i)
    return True
actualizare(lista, "S1", "trenulet")

print(despre_spiridus(lista, "S1"))