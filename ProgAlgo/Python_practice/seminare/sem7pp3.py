multiset = [1, 5, 2, 6, 3, 2, 6, 7, 2, 4]
sol = [0] * (len(multiset) + 1)
multiset.insert(0, 0)

maxim = 0
def back1(k):
    global sol, multiset, maxim
    for i in range(1 if k == 1 else sol[k-1]+1, len(multiset)):
        sol[k] = i
        if multiset[sol[k]] >= multiset[sol[k-1]] and k <=len(multiset):
            if maxim < k:
                maxim = k
            back1(k+1)

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

back1(1)

back2(1)