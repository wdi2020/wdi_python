def check(tab,indexy):
    if len(indexy) == 0:
        return False
    suma = 0
    i = 0 
    for j in range(len(indexy)):
        suma_curr = 0
        while i < indexy[j]:
            suma_curr += tab[i]
            i+=1
        if suma == 0:
            suma = suma_curr
        elif suma != suma_curr:
            return False
    return True
def reku(tab,indexy,max_dl,curr_idx):
    if curr_idx == len(tab):
        if check(tab,indexy) and max_dl < len(indexy):
            return len(indexy)
        return max_dl
    max_dl = reku(tab,indexy,max_dl,curr_idx+1)
    max_dl = reku(tab,indexy+[curr_idx],max_dl,curr_idx+1)
    return max_dl

def strt(tab):
    return reku(tab,[],0,0)

tab = [1,2,3,1,5,2,2,2,6]
print(strt(tab))