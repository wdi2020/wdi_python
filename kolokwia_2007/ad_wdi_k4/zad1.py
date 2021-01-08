# 1. Dany jest typ tablicowy mapa = array [ 1..max,1..max ] of Boolean;
# reprezentujący mapę. Wartość true oznacza ląd, a wartość false ocean.
# Na
# oceanie znajdują się wyspy utworzone przez sąsiadujące pola (rysunek).
# Proszę
# napisać w Pascalu funkcję do której
# przekazujemy mapę i współrzędne x,y
# punktu na mapie. Jeżeli współrzędne oznaczają punkt na wyspie, funkcja
# powinna zatopić wyspę.
# Funkcja powinna zwrócić rozmiar zatopionego obszaru.
# Można założyć, że żadna wyspa na mapie nie styka się z jej krawędzią.

def can_take(i, j, tab):
    if i < 0 or j < 0 or i >= len(tab) or j >= len(tab):
        return False
    if tab[i][j] == True:
        tab[i][j] = False
        return True
    return False


def func(tab, row, col):
    if not can_take(row, col, tab):
        return 0
    cnt = 1

    def reku(tab, row, col):
        ruchy = ((0, 1), (0, -1), (1, 0), (-1, 0))
        nonlocal cnt
        for elem in ruchy:
            if can_take(row+elem[0],col+elem[1],tab):
                cnt+=1
                reku(tab,row+elem[0],col+elem[1])
        return

    reku(tab,row,col)
    return cnt