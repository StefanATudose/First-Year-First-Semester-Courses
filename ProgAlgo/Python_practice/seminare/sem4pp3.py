carti = [("Idiotul", ("Fiodor Dostoievski"), 1700, 60), ("Principele", ("Nicollo Machiavelli"), 1400, 50), ("Homo Deus", ("Yuval Harari"), 2016, 80)]

def ieftinire(carti):
    for i in range(len(carti)):
        if carti[i][2] < 2000:
            carti[i] = (carti[i][0], carti[i][1], carti[i][2], carti[i][3] * 0.8)
    return carti

print(ieftinire(carti))

def sort1(elem):
    return -elem[2], elem[0]

def sort2(elem):
    return len(elem[1]), -elem[3]

def sort3(elem):
    autor1 = elem[1].split()
    return autor1[1], autor1[0], elem[2]
