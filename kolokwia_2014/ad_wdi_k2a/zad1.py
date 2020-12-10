def odl_krola(row,col):
    return max(abs(100-row),abs(100-col))

def check(tab):
    new_tab = [0 for _ in range(100)]
    for i in tab:
        odl = odl_krola(i[0],i[1])
        if new_tab[odl] != 0:
            print(new_tab[odl])
            print(i)
        else:
            new_tab[odl] = i


t = []
check(t)
#z klawiatury nie bede ale tablicka w funckji
#w glowie dziala