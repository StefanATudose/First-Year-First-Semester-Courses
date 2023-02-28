s = input("heloo un s pls: ")

nrlit = len(s)

d = 1
diviz = []

while d * d <= nrlit:
    if nrlit % d == 0:
        if nrlit != d * d and d != 1:
            diviz.append(d)
            diviz.append(nrlit//d)
        else:
            diviz.append(d)
    d += 1
diviz.sort()
print(diviz)
for i in diviz:
    if s.count(s[:i]) * len(s[:i]) == len(s):
        print(f"subsirul gasit este {s[:i]} si apare in sir de {s.count(s[:i])} ori")
        break
