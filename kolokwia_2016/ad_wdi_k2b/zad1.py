def wyisz(t,idx_pom):
    for i in range(idx_pom):
        print(t[i],end=" ")
    print()
def reku(t1,t2,idx,t,idx_pom):
    if idx == len(t1):
        wypisz(t,idx_pom)
        return "s"
    t[idx_pom] = t1[idx]
    reku(t1,t2,idx+1,t,idx_pom+1)
    t[idx_pom] = t2[idx]
    reku(t1,t2,idx+1,t,idx_pom+1)
    t[idx_pom] = t1[idx]
    idx_pom += 1
    t[idx_pom] = t2[idx]
    reku(t1,t2,idx+1,t,idx_pom+1)
def strt(t1,t2):
    n = len(t1)
    reku(t1,t2,0,[0 for _ in range(2*n)],0)

t1 = [1,2]
t2=[1,2]
strt(t1,t2)
