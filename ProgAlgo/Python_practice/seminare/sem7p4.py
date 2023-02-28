def back_distincte(k):
    global n, sol
    for i in range(1 if k == 1 else sol[k-1], n-k+2):
        sol[k] = i
        if sum(sol[:k+1]) == n:
            print(*sol[1:k+1], sep = "+")
        else:
            back_distincte(k+1)

def back_termeni_distincti(k):
    global n, sol
    for i in range(1, n-k+2):
        sol[k] = i
        scrt = sum(sol[:k+1])
        if i not in sol[1:k] and scrt <= n:
            if scrt == n:
               print(*sol[1:k+1], sep = "+")
            else:
               back_termeni_distincti(k+1)

def back_distinct_term_dist(k):
    global n, sol
    for i in range(sol[k-1]+1, n-k+2):
        sol[k] = i
        if sum(sol[:k+1]) == n:
            print(*sol[1:k+1], sep = "+")
        else:
            back_distinct_term_dist(k+1)

def back_lung_fixa(k):
    global n, sol, lung
    for i in range(1, n-k+2):
        sol[k] = i
        scrt = sum(sol[:k+1])
        if scrt <= n and k <= lung:
            if scrt == n and k == lung:
                print(*sol[1:k+1], sep = "+")
            else:
                back_lung_fixa(k+1)


n = int(input("dati un n: "))
lung = 3
sol = [0] * (n + 1)

back_lung_fixa(1)







