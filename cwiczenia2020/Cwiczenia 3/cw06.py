def cw06(tab):
    i = 0
    while i < len(tab):
        copy = tab[i]
        while copy >0:
            if (copy%10)%2 == 1 :
                break
            copy //= 10
        else:
            return False
        i+=1
    return True