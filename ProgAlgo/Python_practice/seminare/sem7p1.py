f = open("seminare/sem7p1.txt")

nrperechi = int(f.readline())
perechi = []
for i in range(nrperechi):
    linie = f.readline().split()
    perechi.append((int(linie[0]), int(linie[1])))

f.close()

perechi.sort(key = lambda x: x[1])
ult = [-1] * (nrperechi+1)
lantmax = [1] * (nrperechi+1)


for i in range(1, nrperechi):
    for j in range (0, i):
        if perechi[j][1] < perechi[i][0] and lantmax[i] < lantmax[j] + 1:
            ult[i] = j
            lantmax[i] = lantmax[j] + 1


maxlocal = 0
finallant = 0
for i in range(nrperechi):
    if lantmax[i] > maxlocal:
        maxlocal = lantmax[i]
        finallant = i

print(f"Lung max: {maxlocal}")
while finallant != -1:
    print(perechi[finallant])
    finallant = ult[finallant]