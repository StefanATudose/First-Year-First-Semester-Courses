import queue

f = open("seminare/proiecte.in")
r = f.readlines()
lung = len(r)
proiecte = []
for linie in r:
    linie = linie.split()
    proiecte.append((-int(linie[2]), min(int(linie[1]), lung),linie[0]))

f.close()
proiecte.sort(key = lambda x: -x[1])

coada = queue.PriorityQueue()
plan = [None] * lung
k = 0
bani = 0
for zicurenta in range(lung, 0, -1):
    while k <= lung-1 and proiecte[k][1] == zicurenta:
        coada.put(proiecte[k])
        k += 1
    if coada.qsize() > 0:
        plan[zicurenta] = coada.get()
        bani -= plan[zicurenta][0]
print(plan, "\n", bani)