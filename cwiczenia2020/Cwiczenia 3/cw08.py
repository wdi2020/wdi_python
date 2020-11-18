from random import randint
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
def rekurencja(t,n,index):
    copy = int(t[index]**.5)
    if czy_pierwsza(t[index]):
        index += t[index] 
        if index < n-1 :
            if rekurencja(t,n,index) :
                return True
        elif index == n-1:
            return True 
        else:
            return False 
    while copy > 1:
        if t[index]%copy == 0:
            if czy_pierwsza(copy):
                if(index+copy < n-1):
                    if rekurencja(t,n,index+copy):
                        return True
                elif index+copy == n-1:
                    return True
        copy -=1
    return False

if __name__ == "__main__":
    n = 100
    t = [randint(2,123) for _ in range(n)]
    print(rekurencja(t,n,0) )