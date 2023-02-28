sir = input("ia zi ana ce ai cumparat azi: ")
cantitate = pret = None
sir = sir.split()
suma = 0
for cuvant in sir:
    try:
        if cantitate == None:
            cantitate = float(cuvant)
        else:
            pret = float(cuvant)
            suma = suma + pret * cantitate
            cantitate = None
    except:
        continue

print(suma)