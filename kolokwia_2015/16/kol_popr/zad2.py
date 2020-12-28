def num_to_1_in_bin(num):
    suma = 0 
    while num != 0:
        if num %2 ==1:
            suma +=1
        num//=2
    return suma
def check(t1,t2,t3):
    suma = 0
    for elem in t1:
        suma += num_to_1_in_bin(elem)
    sum2 = 0
    for elem in t2:
        sum2 += num_to_1_in_bin(elem)
    if suma != sum2:
        return False
    sum3 = 0
    for elem in t3:
        sum3 += num_to_1_in_bin(elem)
    if sum3 != suma :
        return False
    return True

def reku(tab,t1,t2,t3,curr_idx):
    if curr_idx == len(tab):
        if check(t1,t2,t3):
            return True
        return False
    if reku(tab,t1+[tab[curr_idx]],t2,t3,curr_idx+1):
        return True
    if reku(tab,t1,t2+[tab[curr_idx]],t3,curr_idx+1):
        return True
    if reku(tab,t1,t2,t3+[tab[curr_idx]],curr_idx+1):
        return True
    return False

def fstrt(tab):
    return reku(tab,[],[],[],0)

t1 = [2,3,5,7,11,13,16]
print(fstrt(t1))