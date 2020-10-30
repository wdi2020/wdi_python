def cw03(MAX,t):
    for i in range(MAX):
        git = False
        for j in range(MAX):
            copy = t[i][j]
            while copy>0:
                if (copy%10)%2 != 0:
                    git = True
                    break
                copy//=10
            if git:
                break
        if not git:
            return True
    return False