from random import randint
n = int(input(">"))

t = [0 for _ in range(n)]
i = 0
while i<n:
    cop = randint(1,100)
    if cop %2 == 1:
        t[i] = cop
        i+=1
#end

la_max,la_curr,r = 2,2,t[1]-t[0]
lg_max,lg_curr,q = 2,2,t[1]/t[0]
i = 2
while i <n:
    #ciag arytmetyczny
    if t[i-1] + r == t[i]:
        la_curr +=1
    else:
        if la_curr > la_max:
            la_max = la_curr
        la_curr = 2
        r = t[i]-t[i-1]
    #ciag geometryczny
    if t[i-1] * q == t[i]:
        lg_curr+=1
    else:
        if lg_curr > lg_max:
            lg_max = lg_curr
        la_curr = 2
        if t[i-1] == 0 :
            q = 0
        else:
            q = t[i]/t[i-1]
    i+=1
#end while
if la_curr > la_max:
    la_max = la_curr
if lg_curr > lg_max:
    lg_max = lg_curr
print(f"{abs(la_max-lg_max)} to roznica miedzy najdluzszymi ciagami aryt i geo")
