def cw03(MAX,t):
    for i in range(MAX):
        for j in range(MAX):
            copy = t[i][j]
            while copy>0:
                if (copy%10)%2 == 0:
                    break
                copy//=10
            else:
                break
        else:
            return True
    return False