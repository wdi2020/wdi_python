#kon
def rekur(tab,y,x):
    if tab[y][x] == True:
        return
    tab[y][x] = True
    #czy jest tak ze kon szachuje cos tam np ze to co pod koniem i suma jego szachownych jest rowna x
#            cop = (i,j)
    i = y
    j = x
    # prawo gora --^
    if i >= 1 and j <= len(tab)-3:
        rekur(tab,i-1,j+2)
    #prawo dol --v
    if i <= len(tab)-2 and j <= len(tab)-3:
        rekur(tab,i+1,j+2)
    #lewo gor --^
    if i >= 1 and j >= 2:
        rekur(tab,i-1,j-2)
    #lewo dol --v
    if i<=len(tab)-3 and j>=2:
        rekur(tab,i+1,j-2)
    #gora prawo ||>
    if i-2 >= 0 and j+1 <= len(tab)-1:
        rekur(tab,i-2,j+1)
    #gora lewo ||<
    if i-2 >= 0 and j-1 >= 0:
        rekur(tab,i-2,j-1)
    #dol prawo ||>
    if i+2 <= len(tab)-1 and j+1 <= len(tab)-1:
        rekur(tab,i+2,j+1)
    #dol lewo ||<
    if i+2 <= len(tab)-1 and j-1 >= 0:
        rekur(tab,i+2,j-1)
def func(n):
    for i in range(n):
        for j in range(n):
            tab = [[False for _ in range(n)]for _ in range(n)]
            rekur(tab,i,j)
            for elem in tab:
                for column in elem:
                    if column == False:
                        return False
    return True

print(func(4))

