def wypisz(tab):
    for x in tab:
        if x != 0:
            print(x,end=" ")
        else:
            break
    print()

def odejmij(tab,index):
    if index+1 < len(tab):
        while tab[index] != 1 and tab[index] > tab[index+1]:
            tab[index]-=1
            tab[index+1]+=1
            if tab[index+1] <= tab[index]:
                wypisz(tab)
            odejmij(tab,index+1)

def strt(num):
    tab = [0 for _ in range(num)]
    tab[0] = num
    print(num)
    odejmij(tab,0)

num = 8
strt(num)
