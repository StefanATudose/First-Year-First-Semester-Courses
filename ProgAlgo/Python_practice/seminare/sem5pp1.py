import random
from math import floor

linii = int(input("dati un nr de linii: "))
coloane = int(input("si unul de coloane"))


def generare(linii, coloane):
    lista = [[random.randint(0, 100)]]
    for i in range(1, linii):
        lista.append([lista[i - 1][0] + floor(random.random() * 20) + 1])
    for i in range(1, coloane):
        lista[0].append(lista[0][i - 1] + floor(random.random() * 20) + 1)
    for i in range(1, linii):
        for j in range(1, coloane):
            skip = max(lista[i][j - 1], lista[i - 1][j])
            lista[i].append(skip + floor(random.random() * 20) + 1)
    return lista


def cautare_clasica(lista, cautat):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == cautat:
                return (i + 1, j + 1)
    return None


def cautare_binara(lista, cautat):
    for i in range(len(lista)):
        if cautat >= lista[i][0] and cautat <= lista[i][len(lista[i]) - 1] == False:
            continue
        else:
            st = 0
            dr = len(lista[i]) - 1
            while st != dr:
                mij = (st + dr) // 2
                if cautat <= lista[i][mij]:
                    dr = mij
                else:
                    st = mij + 1
            if lista[i][st] == cautat:
                return (i + 1, st + 1)
    return None

def greedy(lista, cautat):
    contor = 0
    i = 1
    j = 1
    if lista[i][j] == cautat:
        return (i+1, j+1)

    while contor < len(lista) + len(lista[0]):
        if min(abs(cautat -lista[i-1][j]), abs(cautat -lista[i+1][j]), abs(cautat -lista[i][j-1]), abs(cautat -lista[i][j+1])) == abs(cautat - lista[i+1][j]):
            i = i + 1
        elif min(abs(cautat -lista[i-1][j]), abs(cautat -lista[i+1][j]), abs(cautat -lista[i][j-1]), abs(cautat -lista[i][j+1])) == abs(cautat -lista[i-1][j]):
            i = i - 1
        elif min(abs(cautat - lista[i-1][j]), abs(cautat -lista[i+1][j]), abs(cautat -lista[i][j-1]), abs(cautat -lista[i][j+1])) == abs(cautat - lista[i][j-1]):
            j = j - 1
        elif min(abs(cautat -lista[i-1][j]), abs(cautat -lista[i+1][j]), abs(cautat -lista[i][j-1]), abs(cautat -lista[i][j+1])) == abs(cautat -lista[i][j+1]):
            j = j + 1
        contor += 1
        if lista[i][j] == cautat:
            return (i + 1, j + 1)
    return None
def afisare(lista):
    for i in lista:
        for j in i:
            print(j, end=" ")
        print("\n")


lista = generare(linii, coloane)
cautat = random.choice(random.choice(lista))
afisare(lista)
print(cautat)
print(greedy(lista, cautat))
