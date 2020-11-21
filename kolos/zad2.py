#Łukasz Pawlak
#algorytm szuka maxymalnego elementu patrzac po indexach od 0 jezeli jakas liczba w systemie 2 ma 1 a druga jej nie ma to jest wieksza
#nastepnie szuka elementu najmniejszego zapamietujac indeks w ktirym wierszu byla i oblicza odlegosc od wierszy elem najwiekszego i najmniejszego
def comparemax(a,b,n):
    for i in range(n):
        if a[0][i] == 1 and b[0][i] ==0 :
            return a
        elif a[0][i] == 0 and b[0][i] == 1:
            return b
        #end if
    #end for
    return a
def comparemin(a,b,n):
    for i in range(n):
        print(i)
        if a[0][i] == 1 and b[0][i] ==0 :
            return b
        elif a[0][i] == 0 and b[0][i] == 1:
            return a
        #end if
    #end for
    return a

def distance(T):
    n = len(T)
    safe_max = n
    a = []
    for i in range(n):
        j = 0
        while j < n:
            if T[i][j] == 1 and j < safe_max:
                safe_max = j 
                a = [T[i],i]
                break
            elif T[i][j] == 1 and j == safe_max:
                a = comparemax(a,[T[i],i],n)
            #end if
            j+=1
        #end while
    #end for
    min_safe = -1 
    b = []
    for i in range(n):
        j = 0
        while j < n:
            if T[i][j] == 1 and j > min_safe:
                min_safe = j
                b = [T[i],i]
                break
            elif T[i][j] ==1 and j == min_safe:
                print(T[i])
                b = comparemin(b,[T[i],i],n)
            j+=1
            #end if
    #end for
    return abs(b[1]-a[1])
#end def


t = [[1,0,0],[0,1,1],[0,0,1]]
print(distance(t))