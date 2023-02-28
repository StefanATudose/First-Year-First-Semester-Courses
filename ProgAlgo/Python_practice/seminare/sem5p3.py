
def citire(path):
    f = open(path)
    intervale = []
    linie = f.readline()
    while linie != "":
        intervale.append(tuple(int(x) for x in linie.split()))
        linie = f.readline()
    f.close()
    return intervale

intervale = citire("intervale.txt")


def intervalenou(intervale):
    intervalenou = []
    def OK(st, dr, intervalenou):
        for i in intervalenou:
            if dr >= i[0] and st <= i[1]:
                return i
        return False

    for i in intervale:
        indicator = OK(i[0], i[1], intervalenou)
        if indicator != 0:
            indicator[0] = max(i[0], indicator[0])
            indicator[1] = min(i[1], indicator[1])
        else:
            intervalenou.append([i[0], i[1]])
    return intervalenou

f = open("acoperire.txt", "w")
intervalenou = intervalenou(intervale)
for i in intervalenou:
    f.write(f"{str(i[1])}\n")

f.close()
