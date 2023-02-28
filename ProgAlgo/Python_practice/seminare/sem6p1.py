import queue

siruri = queue.PriorityQueue()
total = []
f = open("seminare/sirurirandom.txt")
for linie in f:
    sircurent = [int(x) for x in linie.split()]
    sircurent.sort()
    siruri.put((len(sircurent), sircurent))
f.close()


def interclasare(sir1, sir2):
    j = 0
    i = 0
    rez = []
    while j < len(sir1) and i < len(sir2):
        if sir1[j] <= sir2[i]:
            rez.append(sir1[j])
            j += 1
        else:
            rez.append(sir2[i])
            i += 1
    rez.extend(sir1[j:])
    rez.extend(sir2[i:])
    return rez



while siruri.qsize() != 1:
    sir1 = siruri.get()
    sir2 = siruri.get()
    rez = interclasare(sir1[1], sir2[1])
    siruri.put((len(rez), rez))

rez = siruri.get()

print(rez[1])