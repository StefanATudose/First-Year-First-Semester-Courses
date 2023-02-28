# a)
n = int(input("dati un n: "))
def matrice(n):
    lista = []
    for i in range(n-1):
        lista.append([i+1])
    lista.append([n-i for i in range(n)])
    for i in range(n-2):
        for j in range(lista[n-2-i][0]-1):
            lista[n-2-i].append(lista[n-1-i][j] + lista[n-1-i][j+1] + lista[n-2-i][j])

    def afisare(M):
        ncmax = max([len(str(max(linie))) for linie in M])
        for linie in M:
            for elem in linie:
                print(str(elem).ljust(ncmax,), end=' ')
            print()
    afisare(lista)

matrice(n)