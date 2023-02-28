multiset = [1, 5, 2, 6, 3, 2, 6, 7, 2, 4, 5, 7, 4, 2, 6, 1, 1, 1, 1, 10]
sol = [0] * (len(multiset) + 1)

S = 10
multiset.insert(0, 0)
def back(k):
    global S, sol, multiset
    for i in range(1 if k == 1 else sol[k-1]+1, len(multiset)):
        sol[k] = i
        sumcur = 0
        for i in sol[1:k+1]:
            sumcur += multiset[i]
        if sumcur <= S:
            if sumcur == S:
                for i in sol[1:k+1]:
                    print(multiset[i], end = ' ')
                print()
            else:
                back(k+1)

back(1)