def silnia(num : int):
    a= [0 for _ in range(10000)]
    a[0] = 1
    k = 0
    for i in range(2,num+1):
        while a[k] == 0:
            k+=1
        copy = k
        while a[copy] != 0:
            a[copy] = a[copy] * i
            copy+=1
        j = k
        while True:
            if a[j] >= 10:
                a[j+1] = a[j+1] + a[j]//10 
                a[j] = a[j] % 10
            elif a[j+1] < 10:
                break
            else:
                j+=1
    #reverse and delete 0's
    i = k
    while True:
        flag = False
        if a[i] != 0 and a[i+1] == 0:
            j = i + 1
            while j < len(a):
                if a[j] != 0:
                    i =j 
                    flag = True
                    break
                j+=1
            #end while
            if flag:
                continue
            break
        i+=1
    return a[i::-1]
if __name__ == "__main__":
    for i in silnia(1500):
        print(i,end="")
