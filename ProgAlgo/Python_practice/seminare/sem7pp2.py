multiset = [1, 5, 2, 6, 3, 2, 6, 7, 2, 4]

S = 10

matrice = [[0 for j in range(S+1)] for i in range(len(multiset)+1)]

for i in matrice:
    i[0] = 1

for i in range(1, len(multiset)+1):
    for j in range(1, S+1):
        if matrice[i-1][j] or (multiset[i-1] <= j and matrice[i-1][j-multiset[i-1]]):
            matrice[i][j] = 1

sol = []

for i in range(S, 0, -1):
    if matrice[len(multiset)-1][i]:
        break

lung = len(multiset)-1

while lung!= 0:
    if matrice[lung][i] == matrice[lung-1][i]:
        lung -= 1
    else:
        sol.append(multiset[lung-1])
        i = i - multiset[lung-1]
        lung -= 1

sol.reverse()
print(sol)
# # afismatrice
# for i in range(len(multiset)+1):
#     for j in range(S+1):
#         print(matrice[i][j], end = ' ')
#     print()
