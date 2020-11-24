def rekur(tab,index,tryb,suma,suma_ind,pusty:bool):
    if index == len(tab): 
        if pusty:
            if suma == suma_ind:
                return suma 
        return False
    #1 to brac 0 to nie brac
    if tryb == 1:
        suma += tab[index]
        suma_ind += index
        pusty = True
    return rekur(tab,index+1,0,suma,suma_ind,pusty) or rekur(tab,index+1,1,suma,suma_ind,pusty)

def func(tab):
    return rekur(tab,0,0,0,0,False) or rekur(tab,0,1,0,0,False)



print(func([1,7,3,5,11,2]))