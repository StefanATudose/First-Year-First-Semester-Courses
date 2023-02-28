n = 14

sol = [0] * 7

def ok(k):
    global sol
    par = False
    impar = False
    for i in range(1, k+1):
        if par == False:
            par = (sol[i] % 2 == 0)
        if impar == False:
            impar = (sol[i] % 2 == 1)
        if par and impar:
            return True
    return False


def back(k):
    global n, sol

    for i in range(1 if k == 1 else sol[k-1]+1, n+1):
        sol[k] = i
        if (k == 1 or sol[k] != sol[k-1] + 1):
            if k == 6:
                if ok(k) and 13 not in sol:
                    print(sol[1:7])
            else:
                back(k+1)

back(1)