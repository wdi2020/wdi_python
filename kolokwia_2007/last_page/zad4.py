#IV kartkówka - REKURENCJA (obie grupy)
#- dana jest 2-wymiarowa kwadratowa tablica integer, 
#napisz funkcję rekurencyjną, która wypisze
#najkrótszą drogę i jej długość, 
#przy przechodzeniu z punktu (1,1) do (n,n) 
#i poruszaniu się jedynie w
#dół i prawo

def can_move(tab,i,j):
    if i <0 or j <0 or i>=len(tab) or j >= len(tab):
        return False
    return True

min_droga_tab = []
def reku(tab,i,j,curr_droga,curr_dl,min_droga):
    if i+1 == len(tab) and j+1 == len(tab):
        global min_droga_tab
        if min_droga == -1:
            min_droga_tab = tuple(curr_droga)
            return curr_dl
        elif curr_dl < min_droga:
            min_droga_tab = tuple(curr_droga)
            return curr_dl
        return min_droga
    if can_move(tab,i+1,j):
        curr_droga.append("S")
        min_droga = reku(tab,i+1,j,curr_droga,curr_dl+1,min_droga)
        curr_droga.pop()
    if can_move(tab,i,j+1):
        curr_droga.append("E")
        min_droga = reku(tab,i,j+1,curr_droga,curr_dl+1,min_droga)
        curr_droga.pop()
    return min_droga

def strt(tab):
    a = reku(tab,0,0,[],0,-1)
    return min_droga_tab