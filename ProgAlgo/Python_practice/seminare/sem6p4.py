f = open("seminare/placa.in")

linie = f.readline().split()
xst, yst = int(linie[0]), int(linie[1])

linie = f.readline().split()
xdr, ydr = int(linie[0]), int(linie[1])
gauri = []
linie = f.readline()
while linie != "":
    linie = linie.split()
    gauri.append((int(linie[0]), int(linie[1])))
    linie = f.readline()

f.close()
ariemax = 0
xstmax = 0
ystmax = 0
xdrmax = 0
ydrmax = 0

def divetimpera(xst, yst, xdr, ydr):
    global ariemax, xstmax, ystmax, xdrmax, ydrmax, gauri
    estegaura = False
    for i in range(len(gauri)):
        if xdr > gauri[i][0] > xst and ydr > gauri[i][1] > yst:
            divetimpera(xst, yst, xdr, gauri[i][1])
            divetimpera(xst, gauri[i][1], xdr, ydr)
            divetimpera(xst, yst, gauri[i][0], ydr)
            divetimpera(gauri[i][0], yst, xdr, ydr)
            estegaura = True
    if estegaura == False:
        arie = (xdr - xst) * (ydr - yst)
        if arie > ariemax:
            ariemax = arie
            xstmax = xst
            ydrmax = ydr
            ystmax = yst
            xdrmax = xdr

divetimpera(xst, yst, xdr, ydr)

print(ariemax)
print(xstmax, ystmax, xdrmax, ydrmax)