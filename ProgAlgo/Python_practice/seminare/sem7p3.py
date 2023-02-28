f = open("seminare/sem7p1.txt")
date = []
for linie in f:
    tuplu = linie.split()
    date.append((tuplu[0], int(tuplu[1]), int(tuplu[2]), int(tuplu[3])))

f.close()
date.sort(key = lambda x: x[2])
nrelem = len(date)
date.insert(0, ("", 0, 0, 0))
ult = [0] * (nrelem+1)
cmax = [0] * (nrelem+1)

for i in range(1, nrelem+1):
    for j in range(i-1, 0, -1):
        if date[i][1] >= date[j][2]:
            ult[i] = j
            break
    cmax[i] = max(cmax[i-1], date[i][3] + cmax[ult[i]])

imax = cmax.index(max(cmax))

print("castigul maxim este {}".format(cmax[imax]))

while imax != 0:
    if cmax[imax] == cmax[imax-1]:
        imax -= 1
    else:
        print(date[imax])
        imax = ult[imax]