def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2 == 0 or num %3 == 0:
        return False
    i = 6
    while (i-1)**2 < num:
        if num%(i-1) == 0 or num %(i+1) == 0:
            return False
        i+= 6
    return True

def pojebana_funkcja(t):
    a1,a2 = 1,1
    last_index = 0
    flag = False
    while a2 < len(t):
        if not flag:
            while last_index != a2:
                if last_index != a1:
                    if czy_pierwsza(t[last_index]):
                        flag = True 
                last_index += 1
        if czy_pierwsza(t[a2]):
            return False
        a1,a2 = a2,a1+a2
    return flag