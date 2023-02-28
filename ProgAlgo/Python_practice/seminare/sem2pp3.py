prop = input("dati propozitie: ")

litmici = "qwertyuiopasdfghjklzxcvbnm"
litmari = "QWERTYUIOPASDFGHJKLZXCVBNM"

smnpct = "<>?,./:;'!"
nrpct = 0
nrlitmici = 0
nrlitmari = 0

for i in prop:
    if i in smnpct:
        nrpct += 1
    elif i in litmici:
        nrlitmici += 1
    elif i in litmari:
        nrlitmari += 1

print (f"Propozitia citata are {nrlitmari} litere mari, {nrlitmici} litere mici si {nrpct} semne de punctuatie")