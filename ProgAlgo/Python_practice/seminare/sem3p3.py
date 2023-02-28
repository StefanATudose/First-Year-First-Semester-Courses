f = open("exemplu.txt", "r")
text = f.read().lower()
f.close()
semnepct = ".,:?!;"
litere = "abcdefghijklmnopqrstuvwxyz"
listafinala = {}
for i in range(len(text)):
    if text[i] in semnepct:
        if i != len(text)-1:
            text = text[:i] + " " + text[i+1:]
        else:
            text = text[:i]
text = text.split()
for cuvant in text:
    cheie = ""
    for i in range(26):
        if litere[i] in cuvant:
            cheie += litere[i]
    if cheie not in listafinala:
        listafinala[cheie] = [cuvant]
    elif cuvant not in listafinala[cheie]:
        listafinala[cheie].append(cuvant)

# print(listafinala)
# for cheie in sorted(listafinala, reverse = True):


# for cheie in listafinala:
#     print(f"Literele {cheie}: {listafinala[cheie]}")

for cheie in sorted(listafinala, key = lambda n: (-len(n), n)):
    print(f"Literele {cheie}:", end = "")
    for cuvant in sorted(listafinala[cheie]):
        print(f" {cuvant},", end = "")
    print("\n")
