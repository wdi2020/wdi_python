#full legit z https://github.com/Viciooo/WDI_zestawy
def GenTabOfRndGrowingInts(N,start,end):
    from random import randint
    t = [0]*N
    tmp = start
    for i in range(N):
        start = tmp
        t[i] = [0]*N
        for j in range(N):
            t[i][j] = randint(start,end)
            start = t[i][j] + 1
    return t
#Tu moje 
MAX =4
t1 = [[(j*MAX + i + 5) for i in range(MAX)] for j in range(MAX)] 
t1 = GenTabOfRndGrowingInts(MAX,0,1000)
for i in t1:
    print(i)
t2 = [0 for _ in range(MAX*MAX)]


for i in range(MAX):
    for j in range(MAX):
        cop = t1[i][j]
        for a in range(MAX):
            brek = False
            for b in range(MAX):
                if cop < t1[a][b]:
                    break
                if t1[a][b] == cop and not ((a == i) and (b == j)):
                    brek = True
                    break
            if brek:
                break
        else:
            # insert and alter all
            for a in range(MAX*MAX):
                if not (cop > t2[a] and t2[a] != 0):
                    h = a
                    temp = t2[h]
                    t2[h] = cop
                    h+=1
                    while True:
                        if h >= (MAX*MAX)-2:
                            break
                        t2[h],temp = temp,t2[h]
                        if (temp == 0 and t2[h+1] == 0) or h == (MAX*MAX)-2:
                            break
                        h+=1
                    break
print(t2)
#test duplikatow
for i in range(MAX*MAX):
    for j in range(MAX*MAX):
        if t2[i] == t2[j] and i != j and t2[i] != 0:
            print("JAPIERDOLE, ", i,j,t2[j])
