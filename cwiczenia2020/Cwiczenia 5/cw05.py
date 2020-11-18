def cw05(dane):
#!    brudfors
    for i in dane:
        for e in dane:
            if i[1] == e[1] and i!=e:
                dlugosc = abs(i[0]-e[0])
                poziomA = i[1] + dlugosc
                poziomB = i[1] - dlugosc
                countA = 0
                countB = 0
                for f in dane:
                    if f[1] == poziomA:
                        if f[0] == i[0] or f[0] == e[0]:
                            countA+=1
                            if countA == 2:
                                return True
                    if f[1] == poziomB:
                        if f[0] == i[0] or f[0] == e[0]:
                            countB+=1
                            if countB == 2:
                                return True
    return False