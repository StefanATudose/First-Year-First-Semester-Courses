import queue
coada = queue.PriorityQueue()
f = open("seminare/spectacole.in")
linie = f.readline()
spectacole = []
i = 0
while linie != "":
    linie = linie.split()
    aux = linie[0].split("-")
    spectacole.append((aux[0], aux[1], " ".join(linie[1:])))
    coada.put((spectacole[i][1], spectacole[i]))
    i += 1
    linie = f.readline()
f.close()

plan = [coada.get()[1]]
j = 0
for i in range(1, len(spectacole)):
    curent = coada.get()
    if curent[1][0] >= plan[j][1]:
        j += 1
        plan.append(curent[1])

print(plan)