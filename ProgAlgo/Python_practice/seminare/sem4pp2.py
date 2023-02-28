L = ['cuanvt', 'tvancu', 'sarmale', 'sdfsa', 'dsiasdgoihsdg', 'cuvant']

def fgenerica(colectie):

    def ispozitiv(elem):
        if elem >= 0:
            return True
        return False

    def issemnpct(elem):
        semnepct = ".,/?;:'"
        if elem in semnepct:
            return True
        return False


    def isanagrama(elem):
        s = "cuvant"
        if len(elem) == len(s):
            elem = set(elem)
            s = set(s)
            if elem == s:
                return True
        return False

    def issumcif(elem):
        sum = 0
        while elem != 0:
            sum += elem % 10
            elem //= 10
        if sum == s:
            return True
        return False






    pozitii = []
    for i in range(len(colectie)):
        if (isanagrama(colectie[i])):
            pozitii.append(i)
    return pozitii

print(fgenerica(L))
