def get_nb(num):
    t = []
    while num >0:
        rest = num%10
        for i in t:
            if i == rest:
                break
        else:
            t.append(rest)
        num//=10 
    return t
def cw11(t):
    ret = 0
    MAX = len(t)
    cop = [[[] for _ in range(MAX)] for _ in range(MAX)]

    i = 0
    while i<MAX:
        j = 0
        while j<MAX:
            cop[i][j] = get_nb(t[i][j])
            j+=1
        i+=1
    
    i = 0
    while i<MAX:
        j = 0
        while j<MAX:
            is_friend = 0
            if j != MAX-1:
                #prawo
                if len(cop[i][j]) == len(cop[i][j+1]):
                    for e in cop[i][j]:
                        git = False
                        for f in cop[i][j+1]:
                            if e==f:
                                git = True
                                break
                        if not git:
                            break
                    else:
                        is_friend +=1
                else:
                    continue
            else:
                is_friend+=1

            if j!=0:
                #lewo
                if len(cop[i][j]) == len(cop[i][j-1]):
                    for e in cop[i][j]:
                        git = False
                        for f in cop[i][j-1]:
                            if e==f:
                                git = True
                                break
                        if not git:
                            break
                    else:
                        is_friend +=1
                else:
                    continue
            else:
                is_friend+=1


            if i != MAX-1:
                #dol
                if len(cop[i][j]) == len(cop[i+1][j]):
                    for e in cop[i][j]:
                        git = False
                        for f in cop[i+1][j]:
                            if e==f:
                                git = True
                                break
                        if not git:
                            break
                    else:
                        is_friend +=1
                else:
                    continue
            else:
                is_friend+=1
            if i!=0:
                #gora
                if len(cop[i][j]) == len(cop[i-1][j]):
                    for e in cop[i][j]:
                        git = False
                        for f in cop[i-1][j]:
                            if e==f:
                                git = True
                                break
                        if not git:
                            break
                    else:
                        is_friend +=1
                else:
                    continue
            else:
                is_friend+=1
            
            if is_friend == 4:
                print(i,j)
                ret+=1
            j+=1
        i+=1

    return ret

if __name__ == "__main__":
    print(cw11([[123 for _ in range(10)]for _ in range(10)]))