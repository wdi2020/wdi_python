def cw14(t1,t2,n1,n2):
    # n2 > n1 wg mnie
    i = 0
    while i <= n2-n1:
        j = 0
        while j <= n2-n1:
            count = 0
            k = 0
            while k < n1:
                l = 0
                while l<n1:
                    u = t2[i+l][j+k]
                    cp2 = 0 
                    while u !=0:
                        if u%2 ==1:
                            cp2+=1 
                        u//=2                        
                    u = t1[l][k]
                    cp1 = 0 
                    while u !=0:
                        if u%2 ==1:
                            cp1+=1 
                        u//=2                        

                    if cp1 == cp2:
                        count +=1
                    l+=1
                k+=1
            if count/(n1*n1) >= 1/3:
                return True 
            j+=1
        i+=1
    return False

from random import randint
if __name__ == "__main__":
    #false
    print(cw14([[randint(1,100) for _ in range(6)] for _ in range(6)],[[randint(1,1) for _ in range(12)] for _ in range(12)],6,12))
