cnt = 0
t=[]
T = [2,4,6,1,3]
def func(il,T,nki,i=0,tab=[]):
    global cnt
    global t
    if il==1 and nki==0:
        if tab not in t:
            t=t+[tab]
            cnt+=1
    if i==len(T):
        return False
    if il%T[i]==0:
        return func(il//T[i],T,nki-1,i+1,tab+[T[i]]) or func(il,T,nki,i+1,tab)
    if il%T[i] != 0:
        return func(il,T,nki,i+1,tab)
func(12,T,3,)
print(cnt,t)
