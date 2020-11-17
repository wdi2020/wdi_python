def szachuj_(danee):
    i = 0
    while i<len(danee):
        j = i+1
        while j<len(danee):
            #wiersz
            if danee[j][0] == danee[i][0]:
                return False
            #kolumna
            if danee[j][1] == danee[i][1]:
                return False
            #na skos
            x = abs(danee[i][0] - danee[j][0])
            y = abs(danee[i][1] - danee[j][1])
            if x // y == 1.0 or x//y == -1:
                return False
            j+=1
        i+=1
    return True
