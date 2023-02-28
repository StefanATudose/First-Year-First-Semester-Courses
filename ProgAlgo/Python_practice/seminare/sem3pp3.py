f = open("exemplu.txt")
text = f.read()
f.close()
pct = ".,?/;:'!"
for i in pct:
    text = text.replace(i, " ")

text = text.split()
d = {}
for cuvant in text:
    if len(cuvant) not in d:
        d[len(cuvant)] = [cuvant]
    elif cuvant not in d[len(cuvant)]:
        d[len(cuvant)].append(cuvant)

for cheie in sorted(d, reverse = True):
    print(f"Lungime {cheie}:", end = "")
    for cuvant in sorted(d[cheie]):
        print(" " + cuvant + ",", end = '')
    print("\n")
