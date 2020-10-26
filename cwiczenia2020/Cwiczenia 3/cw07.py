from random import randint
def cw7():
    MAX = 150
    tab = [randint(0,1000) for _ in range(MAX)]
    i = 0
    while i < len(tab):
        copy = tab[i]
        while copy > 0:
            if copy%2 == 0:
                return False 
            copy //=10
        i+=1
    return True