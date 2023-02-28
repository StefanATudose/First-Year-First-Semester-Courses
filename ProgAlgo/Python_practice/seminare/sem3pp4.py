f = open("numere.txt")
text = f.read()
f.close()

cifre = [0] * 10
for i in text:
    if i.isnumeric():
        cifre[int(i)] += 1
print(cifre)

minu = ""
maxu = ""

cifre2 = cifre + [0]

for i in range(len(cifre)):
    if i != 0:
        cifre[i] -=1
        minu += str(i)
        break
for i in range(len(cifre)):
    while cifre[i]:
        cifre[i] -= 1
        minu += str(i)
    while cifre2[9-i]:
        cifre2[9-i] -=1
        maxu += str(9-i)
print(f"Minim: {minu}\nMaxim: {maxu}")
print(hex(20))
