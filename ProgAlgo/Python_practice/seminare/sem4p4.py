L = [15, 21, 700, 132, -8, 19, -10, 1, 10, 5, 133]

def elemok(colectie):
    nrelemok = 0
    k, y, t = 4, 4, 2
    def ispara(nr):
        if nr % 2 == 0:
            return True
        return False

    def isvocala(caract):
        vocale = "aeiouAEIOU"
        if caract in vocale:
            return True
        return False

    def iselemdublu(elem):
        if elem[0] == elem[1]:
            return True
        return False

    def arelungk(elem):
        if len(elem) == k:
            return True
        else:
            return False

    def iscmmdc(elem):
        while elem % y != 0:
            rest = elem % y
            elem = y
            y = rest
        if rest == t:
            return True
        return False

    for i in colectie:
        if iselemdublu(i):
            nrelemok += 1
    return nrelemok

n = 5
# L = {1, 2, ..., n} X {1, 2, ..., n}
L = [(i, j) for i in range(1, n+1) for j in range(1, n+1)]

print(elemok(L))