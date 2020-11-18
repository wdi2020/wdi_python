def czy_zlozona(num):
    if num <=1:
        return False
    if num  ==2 or num ==3:
        return  False 
    if num %2==0 or num%3 == 0:
        return True
    i = 6
    while i<num//2:
        if num%(i-1)==0 or num%(i+1) == 0:
            return True
        i+=6
    return False
def cw12(t):
    MAX = len(t)
    a = [0 for _ in range(MAX)]
    for z in range(MAX):
        conut = 0
        for y in range(MAX):
            for x in range(MAX):
                c_x =0
                #prawo
                if x!=MAX-1:
                    if czy_zlozona(t[z][y][x+1]):
                        c_x+=1
                        t[z][y][x+1] = 4
                #góra
                if y!=0:
                    if czy_zlozona(t[z][y-1][x]):
                        c_x+=1
                        t[z][y-1][x] = 4
                #lewo
                if x!=0:
                    if czy_zlozona(t[z][y][x-1]):
                        c_x+=1
                        t[z][y][x-1] = 4
                #dol
                if y!=MAX-1:
                    if czy_zlozona(t[z][y+1][x]):
                        c_x+=1
                        t[x][y+1][x] = 4
                #prawo gora
                if y!=0 and x!=MAX-1:
                    if czy_zlozona(t[z][y-1][x+1]):
                        c_x+=1
                        t[z][y-1][x+1] = 4
                #prawo dol
                if y!=MAX-1 and x!=MAX-1:
                    if czy_zlozona(t[z][y+1][x+1]):
                        c_x+=1
                        t[z][y+1][x+1] = 4
                #lewo dol
                if y!=MAX-1 and x!=0:
                    if czy_zlozona(t[z][y+1][x-1]):
                        c_x+=1
                        t[z][y+1][x-1] = 4
                #lewo gora
                if y!=0 and x!=MAX-1:
                    if czy_zlozona(t[z][y-1][x+1]):
                        c_x+=1
                        t[z][y-1][x+1]
                if c_x >=6:
                    conut+=1
        a[z] = conut
    
    i = 0
    while i<MAX-1:
        if a[i] == 0:
            return False
        if a[i] != a[i+1]:
            return False
        i+=1
    return True
            
if __name__ == "__main__":
    print(cw12([[[2 for _ in range(100)] for _ in range(100)] for _ in range(100)]))