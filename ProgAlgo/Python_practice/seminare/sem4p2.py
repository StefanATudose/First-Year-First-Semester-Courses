#functie
x = int(input("da un x: "))
def functie(x, *liste):
    listafinala = []
    for i in liste:
        if x in i:
            listafinala.append(i)
    return listafinala

#generator

def generator(x, *liste):
    for i in liste:
        if x in i:
            yield i

print(functie(x, [5, 6, 7], [1, 5, 2, 7, 10], [6, 7, 10], [5], [1, 2, 3]))

for i in generator(x, [5, 6, 7], [1, 5, 2, 7, 10], [6, 7, 10], [5], [1, 2, 3]):
    print(i, end = ' ')