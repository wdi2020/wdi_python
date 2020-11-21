def funcA(x,y,n,n_of_moves):
    x+=3
    n_of_moves+=1
    n-=1
    if n<0:
        return -1
    if x == y:
        return n_of_moves
    a =  funcB(x,y,n,n_of_moves)
    b = funcC(x,y,n,n_of_moves)
    if a==-1:
        return b
    if b == -1:
        return a
    if a<b:
        return a
    else:
        return b

def funcB(x,y,n,n_of_moves):
    x*=2
    n_of_moves+=1
    n-=1
    if n<0:
        return -1
    if x == y:
        return n_of_moves
    a =  funcA(x,y,n,n_of_moves)
    b = funcC(x,y,n,n_of_moves)
    if a==-1:
        return b
    if b == -1:
        return a
    if a<b:
        return a
    else:
        return b
def funcC(x,y,n,n_of_moves):
    copy = 0
    l = 0
    while x>0:
        re = x%10
        if re %2 ==1:
            re-=1
        copy *= (10**l)
        copy +=re
        x//=10
        l+=1
    x = copy
    n_of_moves+=1
    n-=1
    if n<0:
        return -1
    if x == y:
        return n_of_moves
    a =  funcA(x,y,n,n_of_moves)
    b = funcB(x,y,n,n_of_moves)
    if a==-1:
        return b
    if b == -1:
        return a
    if a<b:
        return a
    else:
        return b
def funck(x,y,n):
    n_of_moves = 0
    a = funcA(x,y,n,n_of_moves)
    b = funcB(x,y,n,n_of_moves)
    c = funcC(x,y,n,n_of_moves)
    if a==-1 and b==-1:
        return c

    if a==-1 and c==-1:
        return b

    if c==-1 and b==-1:
        return a
    if a != -1 and b!=-1 and c!=-1:
        return max(a,b,c)
    return max(min(a,b),min(a,c),min(b,c))

if __name__ == "__main__":
    print(funck(23,27,5))
    print(funck(23,39,4))
