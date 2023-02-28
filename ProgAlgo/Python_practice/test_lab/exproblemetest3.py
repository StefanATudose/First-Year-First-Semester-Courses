f = open("test_lab/numere.in")
r = f.read()
f.close()
z = [int(x) for x in r.split()]
f = open("test_lab/numere2.in")
r = f.read()
f.close()
y = [int(x) for x in r.split()]

def cifra_control(n):
    suma = 0
    while n:
        suma = suma + n % 10
        n //= 10
    sumacontrol = suma
    while suma > 9:
        sumacontrol = suma
        suma = 0
        while sumacontrol:
            suma += sumacontrol % 10
            sumacontrol //= 10
    return suma

def insereaza_cifra_control(x):
    y = len(x)*2
    for i in range(1, y, 2):
        x.insert(i, cifra_control(x[i-1]))

def egale(*liste):
    l1 = liste[0]
    contor = True
    for i in liste[1:]:
        if i != l1:
            contor = False
    return contor
x = z.copy()
insereaza_cifra_control(x)

# for i in range(0, len(x)-1, 2):
#     print(x[i], x[i+1])
z = list(set(z))
y = list(set(y))
z.sort()
y.sort()
insereaza_cifra_control(z)
insereaza_cifra_control(y)
if len(z) != len(y):
    print("nu")
else:
    contor = True
    for i in range(1, len(z), 2):
        if z[i] != y[i]:
            contor = False
    print(z, y)
    if contor:
        print("da")
    else:
        print("nu")