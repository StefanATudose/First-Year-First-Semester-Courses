prim = input ("primul: ")
secund = input("al doilea: ")

vfrecv = [0] * 26
for litera in prim:
    vfrecv[ord(litera)-ord("a")] += 1
for litera in secund:
    vfrecv[ord(litera)-ord("a")] -=1

if vfrecv == [0] * 26:
    print("sunt anagrame")
else:
    print("nu sunt anagrame")