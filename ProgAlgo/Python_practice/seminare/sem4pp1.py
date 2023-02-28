def generarematrice(n):
    lista = []
    for i in range(n-1):
        lista.append([0] * n)
    lista.append([1] * n)
    for i in range(n):
        lista[i][n-1] = 1
    for i in range (n-2, -1, -1):
        for j in range(n-2, -1, -1):
            lista[i][j] = lista[i+1][j] + lista[i][j+1]
    return lista
