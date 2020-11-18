def cw05(dane):
#!    brudfors powinno dzialac ale hard to tell czy tak jest pzdr
    for i in dane:
        for e in dane:
            #tylko w prawo
            if i[1] == e[1] and i[0] < e[0]:
                dlugosc = e[0]-i[0]
                #tylko w gore
                poziomA = i[1] + dlugosc
                countA = 0
                for f in dane:
                    if ( f[0] > i[0] and f[0] < e[0] ) and ( f[1] > i[1] and f[1] < poziomA):
                        break
                    elif f[1] == poziomA:
                        if f[0] == i[0] or f[0] == e[0]:
                            countA+=1
                            if countA == 2:
                                return True
    return False