def dlug(a):
    copy = a
    dl = 0
    while copy != 0:
        dl+=1
        copy//=10
    return dl

def rek_a(x,y,n,ciag):
    if x == y:
        return ciag 
    if n == 0:
        return False
    dl = dlug(x)
    if dl >= 2:
        a = x%10
        x//=10
        b = x%10
        x//=10
        x = x + (a*10) + b
    ciag = ciag + "A"
    b = rek_b(x,y,n-1,ciag)
    c = rek_c(x,y,n-1,ciag)
    if c != False:
        if b != False:
            if len(c) > len(b):
                return b
            return c
        else:
            return c
    return b

def rek_b(x,y,n,ciag):
    if x == y:
        return ciag 
    if n == 0:
        return False
    x *= 3
    ciag = ciag + "B"
    a = rek_a(x,y,n-1,ciag)
    c = rek_c(x,y,n-1,ciag)
    if c != False:
        if a != False:
            if len(c) > len(a):
                return a
            return c
        else:
            return c
    return a

def rek_c(x,y,n,ciag):
    if x == y:
        return ciag 
    if n == 0:
        return False
    dl = dlug(x)
    if dl >= 2:
        x = x%(10**(dl-1))
    ciag = ciag + "C"
    a = rek_a(x,y,n-1,ciag)
    b = rek_b(x,y,n-1,ciag)
    if b != False:
        if a != False:
            if len(b) > len(a):
                return a
            return b
        else:
            return b
    return a

def func(x,y,n):
    ciag = ""
    a = rek_a(x,y,n,ciag)
    c = rek_c(x,y,n,ciag)
    b = rek_b(x,y,n,ciag)
    i=1
    while i < n:
        if a != False:
            if len(a) == i:
                return a
        if b!= False:
            if len(b) == i:
                return b
        if c != False:
            if len(c) == i:
                return c
        i+=1
    return ""

print(func(6,3,7))