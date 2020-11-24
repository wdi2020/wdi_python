def rekur(tab,masa_szukana,suma,index):
    #tryb 1 na 1 szalke +
    #tryb 2 na 2 szalke -
    #tryb 0 to wyjebane
    if index == len(tab):
        if suma == masa_szukana:
            return True
        return False
    if suma == masa_szukana:
        return True
    #tryb 0
    if rekur(tab,masa_szukana,suma,index+1):
        return True
    #tryb 1
    suma += tab[index]
    if rekur(tab,masa_szukana,suma,index+1):
        print(f"< {tab[index]}")
        return True
    suma -= tab[index]
    #tryb 2
    suma -=tab[index]
    if rekur(tab,masa_szukana,suma,index+1):
        print(f"> {tab[index]}")
        return True
    suma += tab[index]

    return False

def func(tab,masa_szukana):
    return rekur(tab,masa_szukana,0,0)


print(func([20,30],10))