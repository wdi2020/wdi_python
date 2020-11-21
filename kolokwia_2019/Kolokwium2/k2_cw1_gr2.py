def iloscNp(num):
    count=0
    while num >0:
        if (num %7)%2==1:
            count+=1
        num//=7
    return count
def func(tab1,tab2):
    MAX1 = len(tab1)
    MAX2 = len(tab2)
    i = 0
    while i < MAX1-MAX2:
        j = 0
        while j<MAX1-MAX2:
            count=0
            k = 0
            while k<MAX2:
                l = 0
                while l<MAX2:
                    if iloscNp(tab1[i+k][j+l]) == iloscNp(tab2[k][l]):
                        count+=1
                    l+=1
                k+=1
            if count/MAX2 >= 1/3:
                return True
            j+=1
        i+=1
    return False

if __name__ == "__main__":
    MAX1 = 10
    MAX2 = 5
    print(func([[14 for _ in range(MAX1)] for _ in range(MAX1)],[[8 for _ in range(MAX2)] for _ in range(MAX2)]))
