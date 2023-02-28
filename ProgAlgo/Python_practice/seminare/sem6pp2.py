lista = [1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5]


def divetimperaprim(lista, k, st, dr):
    mijl = st + (dr - st) // 2

    if lista[mijl] == k:
        if lista[mijl - 1] != k:
            return mijl
        else:
            return divetimperaprim(lista, k, st, mijl - 1)
    elif lista[mijl] < k:
        return divetimperaprim(lista, k, mijl + 1, dr)
    else:
        return divetimperaprim(lista, k, st, mijl - 1)


def divetimperaultim(lista, k, st, dr):
    mijl = st + (dr - st) + 1 // 2

    if lista[mijl] == k:
        if mijl == len(lista)-1:
            return mijl
        elif lista[mijl + 1] != k:
            return mijl
        else:
            return divetimperaultim(lista, k, st, mijl + 1)
    elif lista[mijl] < k:
        return divetimperaultim(lista, k, mijl + 1, dr)
    else:
        return divetimperaultim(lista, k, st, mijl - 1)


print(divetimperaultim(lista, 5, 0, len(lista) - 1) - divetimperaprim(lista, 5, 0, len(lista) - 1) + 1)
