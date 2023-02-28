lista = [-10, -1, -10, -7, -10, -2, -4, -1, -3]


lista.sort()
negativdatorie = False
produs = 1
finale = []
for i in range(len(lista)-1):
    if lista[i] < 0:
        if negativdatorie == False and lista[i+1] < 0:
            produs *= lista[i]
            negativdatorie = True
            finale.append(lista[i])
        elif negativdatorie:
            negativdatorie = False
            produs *= lista[i]
            finale.append(lista[i])
    elif lista[i] > 1:
        produs *= lista[i]
        finale.append(lista[i])
if lista[len(lista)-1] > 1 or (lista[len(lista)-1] < 0 and negativdatorie == True):
    finale.append(lista[len(lista)-1])
    produs *= lista[len(lista)-1]
print(produs, "\n", finale)