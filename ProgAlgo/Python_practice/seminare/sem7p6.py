def back(k):
    global spectacole, s, lung
    for i in range(1 if k == 1 else s[k-1]+1, len(spectacole)):
        s[k] = i
        if spectacole[i][0] >= spectacole[k-1][1]:
            if k == lung:
                for i in range(1, lung+1):
                    afisaj = "-".join(spectacole[s[i]][0:2]) + ' ' + spectacole[s[i]][2] + '\n'
                    f.write(afisaj)
                f.write("\n")
            else:
                back(k+1)


f = open("seminare/spectacole.in")
spectacole = [("", "", "")]
for linie in f:
    linie = linie.split()
    aux = linie[0].split("-")
    spectacole.append((aux[0], aux[1], " ".join(linie[1:])))
f.close()

spectacole.sort(key = lambda x: x[1])
ult = "0"
lung = 0
for i in range(1, len(spectacole)):
    if spectacole[i][0] >= ult:
        lung += 1
        ult = spectacole[i][0]

s = [0] * (len(spectacole) + 1)

f = open("seminare/spectacole.out", "w")
back(1)

f.close()