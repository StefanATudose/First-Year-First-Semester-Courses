w = input("oferiti o rima: ")
p = int(input("acum un numar de litere dupa care doriti sa rimeze: "))
n = int(input("in final, un numar de cuvinte: "))

cuvinte = input("avem nevoie de lista de cuvinte, doamnelor: ").split()

for i in range(n):
    cuvant = cuvinte[i]
    if cuvant.endswith(w[-p:]):
        print(f"un astfel de cuvant este {cuvant}")

