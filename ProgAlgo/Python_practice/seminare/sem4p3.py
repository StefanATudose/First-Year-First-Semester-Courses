def parsare(path):
    studenti = []
    f = open(path, "r")
    linie = f.readline()
    while linie != "":
        linie = linie[:len(linie)-1]
        linie = linie.split(",")
        note = tuple(int(linie[x]) for x in range(2, len(linie), 1))
        studenti.append((linie[0], linie[1], note))
        linie = f.readline()
    return studenti

def examinare(studenti, crdminime):
    for stud in range(len(studenti)):
        crdtotale = 0
        restanta = False
        for i in range(len(studenti[stud][2])):
            crdtotale += studenti[stud][2][i]
            if studenti[stud][2][i] == 0:
                restanta = True
        if (restanta == False and crdminime <= crdtotale):
            studenti[stud] = studenti[stud] + ("True",)
        else:
            studenti[stud] = studenti[stud] + ("False",)

def dupagrupa(student):
    return student[1], student[0]
def dupapromovati(student):
    if student[3] == "True":
        return 0, student[0]
    else:
        return 1, student[0]

def descrescatorcredite(student):
    sumcred = 0
    for i in range(len(student[2])):
        sumcred += student[2][i]
    return -sumcred, student[1], student[0]

def combinate(student):
    sumcred = 0
    for i in range(len(student[2])):
        sumcred += student[2][i]
    return student[1], -student[3], -sumcred, student[0]

studenti = parsare("studenti.csv")
examinare(studenti, 19)
studenti.sort(key = descrescatorcredite)

print(studenti)
