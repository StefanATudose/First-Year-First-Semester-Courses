lsb = [0, 0, 0, 1, 1, 1, 1]

def dei(st, dr):
    global lsb

    mijl = st + (dr-st) // 2

    if lsb[mijl] == 0:
        if lsb[mijl+1] == 0:
            final = dei(mijl+1, dr)
        else:
            return mijl+1

    elif lsb[mijl] == 1:
        if lsb[mijl-1] == 1:
            final = dei(st, mijl-1)
        else:
            return mijl
    return final

if lsb == [0] * len(lsb):
    print(f"Pozitia la care 1 va aparea in sir este -1")
elif lsb == [1] * len(lsb):
    print(f"Pozitia la care 1 va aparea in sir este 0")
else:
    print(f"Pozitia la care 1 va aparea in sir este {dei(0, len(lsb)-1)}")