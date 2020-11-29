def can_take(tab,wybrane,index):
    for i in wybrane:
        if i//len(tab) == index//len(tab) or i%len(tab) == index%len(tab):
            return False
    return True

def reku(tab,suma_curr,suma_zad,wybrane,index):
    if suma_curr == suma_zad:
        return True
    elif suma_curr > suma_zad:
        return False
    elif index == (len(tab)**2) -1:
        return False
    if reku(tab,suma_curr,suma_zad,wybrane,index+1):
        return True
    if can_take(tab,wybrane,index):
        wybrane.append(index)
        if reku(tab,suma_curr+tab[index//len(tab)][index%len(tab)],suma_zad,wybrane,(index//len(tab))+1):
            return True
        wybrane.pop()
    return False

def func(tab,suma):
    return reku(tab,0,suma,[],0)

tab = [[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
print(func(tab,4))
