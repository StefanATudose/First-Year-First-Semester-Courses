fraza = input("dati fraza: ")

pct = "<>?,./:;'!"

for i in pct:
    fraza = fraza.replace(i, " ")

print(f" propozitia citata are fix {len(set(fraza.split()))} cuvinte distincte")

