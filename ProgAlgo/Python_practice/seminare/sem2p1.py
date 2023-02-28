s = input("da un s: ")
t = input("si un t: ")

k = 0

while (s.find(t, k)) >= 0:
    print(s.find(t, k))

    k = len(t) + s.find(t, k)

