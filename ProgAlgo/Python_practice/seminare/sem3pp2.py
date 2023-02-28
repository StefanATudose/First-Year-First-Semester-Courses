prim = input ("primul: ")
secund = input("al doilea: ")

vfrecv = [0] * 26
for litera in prim:
    vfrecv[ord(litera)-ord("a")] += 1
for litera in secund:
    vfrecv[ord(litera)-ord("a")] -=1
permut1 = []
permut2 = []
if vfrecv == [0] * 26:
    for i in range(len(prim)):
        indice = secund.find(prim[i])
        permut1.append(indice+1)
        permut2.append(i+1)
        secund = secund[:indice] + " " + secund[indice+1:]
    print(f"Permutarea obtinuta va fi:\n{permut2}\n{permut1}")
else:
    print("nu sunt anagrame")

