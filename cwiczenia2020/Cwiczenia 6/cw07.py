def rekur(tab,masa_szukana,index,tryb,suma):
    if index == len(tab):
        if masa_szukana == suma :
            return True
        return False
    if suma > masa_szukana:
        return False
    if tryb ==1:
        suma += tab[index]
    return rekur(tab,masa_szukana,index+1,0,suma) or rekur(tab,masa_szukana,index+1,1,suma)
def func(tab,masa_szukana):
    return rekur(tab,masa_szukana,0,0,0) or rekur(tab,masa_szukana,0,1,0)

print(func([5,4,2],10))



