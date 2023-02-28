prop = input("dati propozitie: ")
cheie = int(input("dati o cheie pentru cifru"))

for i in range(len(prop)):
    if prop[i].isalpha():
        ordi = ord(prop[i])
        ordi += cheie
        prop = prop[:i] + chr(ordi) + prop[i+1:]

print(prop)