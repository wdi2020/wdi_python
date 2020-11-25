def rekur(tab,masa_szukana,index,suma):
    if index == len(tab):
        if masa_szukana == suma :
            return True
        return False
    if suma > masa_szukana:
        return False
    a = rekur(tab,masa_szukana,index+1,suma)
    if a:
        return True
    suma+= tab[index]
    if rekur(tab,masa_szukana,index+1,suma):
        return True
    return False
def func(tab,masa_szukana):
    return rekur(tab,masa_szukana,0,0)

print(func([5,4,2],10))



