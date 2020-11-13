def func(k):
    a_n,a_n_1= 0,1
    b_n,b_n_1= 0,2
    b_n = b_n_1+a_n_1
    a_n = a_n_1 + (b_n/3)
    min_odl=k
    min_index=0
    ciag=""

    index = 2
    while True:
        index+=1
        b_n,b_n_1 = b_n_1+a_n_1 ,b_n
        a_n,a_n_1 = a_n_1+(b_n/3) ,a_n
        if abs(a_n-k) < min_odl:
            min_odl = abs(a_n-k)
            ciag="a"
            min_index = index
            oddala = False

        if abs(b_n-k) < min_odl:
            min_odl = abs(b_n-k)
            ciag="b"
            min_index = index
            oddala = False

        if index > 100000:
            break

    return min_odl,min_index,ciag

if __name__ == "__main__":
    print(func(1099796))
