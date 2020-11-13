def func(tab):
    # rosnaco
    odp = [0]*10
    N = len(tab)
    i = 0
    while i < N:
        if tab[i] > odp[0]:
            j = 0
            while j < 10:
                if tab[i] <= odp[j]:
                    odp.insert(j,tab[i])
                    break
                j+=1
            else:
                odp.append(tab[i])
            if len(odp) > 10:
                odp.pop(0)
        i+=1
    return odp

if __name__ == "__main__":
    from random import randint
    N = 123
    tab = [randint(1,1000) for _ in range(N)]
    print(func(tab))
    tab.sort(reverse=True)
    print(tab[9::-1])
