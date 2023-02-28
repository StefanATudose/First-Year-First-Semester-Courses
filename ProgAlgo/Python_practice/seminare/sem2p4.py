#1. citire

#2.parcurgerea sirului, la aparitia unui spatiu activam un boolean

#3. salvam prima litera de dupa spatiu, continuam parcurgerea

#4. la primul spatiu sau semn de punctuatie vedem daca subsirul apare in lista de semne de puctuatie, iar daca nu, capitalizam

sir = input("ia zi domle un sir: ")
semnepct = ".,?!"
prepozitii = ["a", "an", "by", "on", "in", "at", "to", "for", "ago", "the", "past", "over", "into", "onto"]
sir = sir[0].upper() + sir[1:].lower()
primalit = 0
amspatiu = False

for i in range(len(sir)):
    if primalit and (sir[i] == " " or sir[i] in semnepct or i == len(sir)-1):
        if i == len(sir)-1:
            sir = sir[:primalit] + sir[primalit].upper() + sir[primalit + 1:]
            print("intrat")
        elif sir[primalit:i] not in prepozitii:
            sir = sir[:primalit] + sir[primalit].upper() + sir[primalit+1:]
            primalit = 0
    if amspatiu:
        primalit = i
        amspatiu = False
    if sir[i] == " ":
        amspatiu = True
print(f"sirul prelucrat va fi {sir}")