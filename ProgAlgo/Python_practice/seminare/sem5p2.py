sir = input("da un sir da intregi: ")
L = [int(x) for x in sir.split()]

L2 = []
s = 20
st = 0
dr = len(L) - 1
looplimit = 0
while st < dr and looplimit < 1000:
    if L[st] + L[dr] == 20:
        L2.append((L[st], L[dr]))
        st += 1
    elif L[st] + L[dr] > 20:
        dr -= 1
    else:
        st += 1
    looplimit += 1
print(L2)