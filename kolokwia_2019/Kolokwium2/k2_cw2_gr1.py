def operacja1(x,y,n):
    count=0
    x = x+3
    n-=1
    if n <0:
        return count
    if x == y:
        count+=1
    else:
        count+=operacja2(x,y,n)
        count+=operacja3(x,y,n)
    return count

def operacja2(x,y,n):
    count=0
    x = x*2
    n-=1
    if n <0:
        return count
    if x == y:
        count+=1
    else:
        count+=operacja1(x,y,n)
        count+=operacja3(x,y,n)
    return count

def operacja3(x,y,n):
    count=0
    copy = x
    ret = 0
    l = 0
    while copy >0:
        o = copy%10
        if (o)%2 == 0:
            o+=1
        ret += (o)*(10**l)
        copy//=10
        l+=1
    x = ret
    n-=1
    if n <0:
        return count
    if x == y:
        count+=1
    else:
        count+=operacja1(x,y,n)
        count+=operacja2(x,y,n)
    return count
def func(x,y,n):
    count = 0
    count+=operacja1(x,y,n)
    count+=operacja2(x,y,n)
    count+=operacja3(x,y,n)
    return count

print(func(11,31,4))
print(func(11,32,4))

