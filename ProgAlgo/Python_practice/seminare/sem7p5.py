def back(k):
    global n, sol

    for i in range(1 if k == 1 else 0, 10):
        sol[k] = i
        sumcurenta = sum(sol[:k+1])
        if sumcurenta <= n and i not in sol[1:k]:
            if sumcurenta == n:
                print("".join([str(x) for x in sol[1:k+1]]), end = " ")
            back(k+1)

n = int(input("dati un n: "))

sol = [0] * 10

back(1)
