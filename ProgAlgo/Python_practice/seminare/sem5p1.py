v = []
numar = input("vreau vot: ")

while numar != "":
    int(numar)
    v.append(numar)
    numar = input("vreau vot: ")

v.sort()
maxcurent = maxu = lung = 1

candidat = 0
for i in range(1, len(v)):
    if v[i] == v[i-1]:
        maxcurent += 1
    else:
        if maxcurent > maxu:
            candidat = v[i]
            maxu = maxcurent

        maxcurent = 1
    lung += 1

if maxcurent > maxu:
    maxu = maxcurent
    candidat = v[i]
if maxu > lung // 2:
    print(f"candidatul majoritar este {candidat}")
else:
    print("din pacate n a castigat nimenea")