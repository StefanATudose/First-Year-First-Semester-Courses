multiset = [1, 5, 2, 6, 3, 2, 6, 7, 2, 4]
lmax = [1] * (len(multiset))
ult = [0] * (len(multiset))

for i in range(1, len(multiset)):
    for j in range(0, i):
        if lmax[j] + 1 > lmax[i] and multiset[i] >= multiset[j]:
            lmax[i] = lmax[j] + 1
            ult[i] = j

maxim = max(lmax)
print(lmax, "\n")

sol = [0] * (len(multiset) + 1)
multiset.insert(0, 0)


def back2(k):
    global sol, multiset, maxim
    for i in range(1 if k == 1 else sol[k-1]+1, len(multiset)):
        sol[k] = i
        if multiset[sol[k]] >= multiset[sol[k-1]]:
            if k == maxim:
                for i in sol[1:k+1]:
                    print(multiset[i], end = ' ')
                print()
            else:
                back2(k+1)


back2(1)