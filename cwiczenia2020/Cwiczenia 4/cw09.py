def cw09(t,k,MAX):
    i = 0
    while i<MAX-2:
        j = 0
        while j <MAX-2:
            a = 2
            while a+j < MAX and i+a < MAX:
                if t[i][j] * t[i][j+a] * t[i+a][j] * t[i+a][j+a] == k:
                    return True,(i+a)//2, (j+a)//2
                a+=2
            j+=1
        i+=1

if __name__ == "__main__":
    print(cw09([[2,0,0,0,2,0,0],[2,0,0,0,2,0,0],[2,0,0,0,2,0,0],[2,0,0,0,2,0,0],[2,0,0,0,2,0,0],[2,0,0,0,2,0,0],[2,0,0,0,2,0,0]],16,7))
