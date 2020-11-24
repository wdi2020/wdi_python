def rekur(tab,masa_szukana,suma,index,tryb):
    #tryb 1 na 1 szalke +
    #tryb 2 na 2 szalke -
    #tryb 0 to wyjebane
    if index == len(tab):
        if suma == masa_szukana:
            return True
        return False
    if suma == masa_szukana:
        return True
    if tryb ==1:
        suma += tab[index]
    elif tryb ==2:
        suma -= tab[index]
    return rekur(tab,masa_szukana,suma,index+1,0) or rekur(tab,masa_szukana,suma,index+1,1) or rekur(tab,masa_szukana,suma,index+1,2)
    

def func(tab,masa_szukana):
    return rekur(tab,masa_szukana,0,0,0) or rekur(tab,masa_szukana,0,0,1) or rekur(tab,masa_szukana,0,0,2)


print(func([20,20],10))