def check(t1,t2):
    if len(t1) == 0 or len(t2) == 0:
        return False
    if len(t1) != len(t2):
        return False
    suma = 0
    for elem in t1:
        suma += elem
    for elem in t2:
        suma -= elem
    if suma ==0:
        return True
    return False

def reku(tab1,tab2,t1,t2,curr_idx,max_par):
    if curr_idx == len(tab1):
        if check(t1,t2):
            return max(len(t1),max_par)
        return max_par
    max_par = reku(tab1,tab2,t1,t2,curr_idx+1,max_par)
    max_par = reku(tab1,tab2,t1+[tab1[curr_idx]],t2,curr_idx+1,max_par)
    max_par = reku(tab1,tab2,t1,t2+[tab2[curr_idx]],curr_idx+1,max_par)
    max_par = reku(tab1,tab2,t1+[tab1[curr_idx]],t2+[tab2[curr_idx]],curr_idx+1,max_par)
    return max_par

def strt(tab1,tab2):
    return reku(tab1,tab2,[],[],0,0)
print(strt([2,3,4,2],[1,1,6,3]))