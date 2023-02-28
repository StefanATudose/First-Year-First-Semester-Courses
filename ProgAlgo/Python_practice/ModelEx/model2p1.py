import random

# a)
# def note(*liste):
#     dictpromovare ={}
#     for i in liste:
#         nrpromovati = 0
#         for k in i:
#             if k >= 5:
#                 nrpromovati += 1
#         if nrpromovati not in dictpromovare:
#             dictpromovare[nrpromovati] = [i]
#         else:
#             dictpromovare[nrpromovati].append(i)
#     return dictpromovare
#
# print(note([5, 4, 2, 7, 10], [6, 7, 8, 10, 3], [10, 7, 4, 10, 9], [5, 6, 8, 4, 1], [5, 5, 6,
# 10, 7, 9]))

# b)
# lista_cuvinte = ["acasa", "masa", "este", "scaun", "perete", "dulap"]
# lista_sufixe=  ["sa", "te"]
#
# lista_rez = [x for x in lista_cuvinte if x.endswith(lista_sufixe[0]) or x.endswith(lista_sufixe[1])]
#
# print(lista_rez)

# c)
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# def f(lista, p, u):
#     if u - p <= 2:
#         return sum(lista[p:u + 1])
#     k = (u - p + 1) // 3
#     x = random.randint(0, 3)
#     if x == 1:
#         rez = f(lista, p, p + k)
#         print(rez, "alocare")
#     elif x == 2:
#         rez = f(lista, p + k + 1, p + 2 * k - 1)
#         print(rez, "alocare")
#     else:
#         rez = f(lista, p + 2 * k, u)
#         print(rez, "alocare")
#     for i in range(p,u+1):
#         rez += lista[i]
#     print(rez, "iesire fct")
#     return rez


print()
print(f(lista, 0, len(lista)-1))