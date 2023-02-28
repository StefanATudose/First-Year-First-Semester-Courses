def back(k):
    global n, tipar, L, S
    if tipar[k-1] == 'l':
        for i in L:
            sol[k] = i
            if i not in sol[1:k] and str(sol[1]) in "aeiouAEIOU":
                if k == n:
                    print("".join([str(x) for x in sol[1:k+1]]))
                else:
                    back(k+1)
    else:
        for i in S:
            sol[k] = i
            if i not in sol[1:k] and str(sol[1]) in "aeiouAEIOU":
                if k == n:
                    print("".join([str(x) for x in sol[1:k+1]]))
                else:
                    back(k+1)

n = int(input("scrieti un n: "))
tipar = list(input("scrieti un tipar: "))
L = list(input("scrieti multimea L: "))
S = list(input("scrieti multimea S: "))

sol = [0] * (n+1)

back(1)

