#opis
#funkcja rekurencyjna która dodaje do tablicy indeksy podzialu liczby liczac od prawej(0) indeks 0 w a tablicy oznacza podzial przed 1 elementem
# wy wykonaniu dzielen potrzebne jest dodatkowe sprawdzenie ostatniego elementu bo on dzieli pierwsze cyfry ktore nie sa sprawdzane w petli
# nastepnei wyrzucane jest False przy pierwszej nie pierwszej liczby
# gdy program natrafi na True nie idzie dalej tylko konczy dzialanie zwracajac wartosc logiczna 
# wartunkiem konca rekurencji jest dojscie do indeksu dlugosc-1 bo to ostatni mozliwy podzial
def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2==0 or num%3==0:
        return False
    i = 6
    while (i-1)**2<=num:
        if num %(i-1) == 0:
            return False
        if num%(i+1) == 0:
            return False
        i+=6
    return True

def check(t,num):
    if len(t)==0:
        return False
    licznik=0
    for elem in t:
        nnumer = (num%(10**(elem+1)))//(10**(licznik))
        licznik+=1
        if not czy_pierwsza(nnumer):
            return False
    nnumer = (num)//(10**(t[-1]+1))
    if not czy_pierwsza(nnumer):
        return False
    if not czy_pierwsza(len(t)+1):
        return False
    return True

def reku(t,num,idx,dl):
    if idx == dl-1:
        return check(t,num)
    return reku(t,num,idx+1,dl) or reku(t+[idx],num,idx+1,dl)
def divide(N):
    dl=0
    cp = N
    while cp!=0:
        dl+=1
        cp//=10
    t=[]
    return reku(t,N,0,dl)