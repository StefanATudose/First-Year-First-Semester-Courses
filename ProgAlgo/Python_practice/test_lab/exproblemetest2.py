f = open("test_lab/intrare.in")
listacuv = []
linie = f.readline()
while linie != "":
    listacuv.append(linie.strip())
    linie = f.readline()
f.close()
def deviruseaza(prop):
    prop = prop.split()
    lung = len(prop)-1
    for i in range(lung, -1, -1):
        cuvant = prop[i]
        cuvant = cuvant[len(cuvant)-1] + cuvant[1:len(cuvant)-1] + cuvant[0]
        prop.append(cuvant)

    for i in range(lung+1):
        prop.pop(0)
    return " ".join(prop)

def prime(n, numar_maxim):
    #nu fac ciur ca nu stiu cat de mare e n si nu vreau stack overflow
    nrprime = []
    prim = 2
    while prim < n:
        d = 2
        while (d * d <= prim and prim % d != 0):
            d += 1
        if d * d > prim:
            nrprime.append(prim)
        prim += 1
        if len(nrprime) == numar_maxim and numar_maxim != 0:
            break
    return nrprime

nrprime = prime(len(listacuv), 0)

for i in nrprime:
    listacuv[i] = deviruseaza(listacuv[i])

f = open("test_lab/intrare_devirusata.out","w")
for i in listacuv:
    prop = i + "\n"
    f.write(prop)

f.close()