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
            if x // y == 1 or x//y == -1:
                return False
            j+=1
        i+=1
    return True
    #? false to sie szachuja a true to sie nie szachuja 


dane = [(i,i%10) for i in range(100)]
dane = [(1,4),(0,5)]
print(szachuj_(dane))