def cw2():
    a = int(input("podaj 1 liczbe:"))
    b = int(input("podaje 2 licbze: "))

    a_t = [-1 for _ in range(10)]
    i = 0
    while a>0:
        a_t[i] = (a%10)
        a//=10
        i+=1

    while b>0:
        temp = b%10
        b //=10
        i = 0
        while i < len(a_t):
            if temp == a_t[i]:
                a_t[i] = -1
                break
            i += 1
        else:
            return False
    
    for e in a_t:
        if e != -1:
            return False
    return True
