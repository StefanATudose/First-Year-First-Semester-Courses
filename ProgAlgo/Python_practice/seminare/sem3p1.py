f = open("numarlipsa.txt", "r")
contor = False
lista = [int(x) for x in f.read().split()]
f.close()

for i in range(1, len(lista)+1):
    if i not in lista:
        print(f"numarul care a fost omis este {i}")
        contor = True
        break
if contor == False:
    print(f"numarul omis este {len(lista)+1}")