#x1,x2,y1,y2
def check(t):
    suma = 0
    for i in range(13):
        #suma
        suma += abs((t[i][0] - t[i][1]) * (t[i][2]-t[i][3]))
        for j in range(i+1,13):
            #czy nachodza
            if t[j][0] > t[i][0] and t[j][0] < t[i][1] and ((t[j][2] > t[i][2] and t[j][2] < t[i][3]) or(t[j][3] > t[i][2] and t[j][3]<t[i][3])):
                return False
            elif t[j][1] > t[i][0] and t[j][1] < t[i][1] and ((t[j][2] > t[i][2] and t[j][2] < t[i][3]) or(t[j][3] > t[i][2] and t[j][3]<t[i][3])):
                return False
    if suma == 2012:
        return True
    return False

def reku(tab,pomc,index):
    if len(pomc) == 13:
        return check(pomc)
    if index == len(tab):
        return False
    a = reku(tab,pomc,index+1)
    pomc.append(tab[index])
    b = reku(tab,pomc,index+1)
    pomc.pop()
    return a or b

def fun(tab):
    return reku(tab,[],0)