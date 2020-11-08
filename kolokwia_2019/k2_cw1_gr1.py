def piatkowa(num):
    copy = num
    count = 0
    while copy >0:
        if (copy%5)%2==0:
            count+=1
        copy//=5
    return count
def func(tab1,tab2):
    MAX1 = len(tab1)
    MAX2 = len(tab2)
    i = 0
    while i < MAX1:
        j = 0
        while j<MAX1:
            count = 0
            k = 0
            while k <MAX2:
                l = 0
                while l<MAX2:
                    if i+k < MAX1 and j+l < MAX2:
                        if piatkowa(tab1[i+k][j+l]) == piatkowa(tab2[k][l]):
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
    print(func([[3 for _ in range(MAX1)] for _ in range(MAX1)],[[10 for _ in range(MAX2)] for _ in range(MAX2)]))

