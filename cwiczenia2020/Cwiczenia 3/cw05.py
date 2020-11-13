temp = int(input("10 wartosc co do wartosci wartiscisdafn, zakoncz zerem"))
t = [0 for _ in range(100)]
k = 0
while temp != 0:
    t[k] = temp
    temp = int(input("10 wartosc co do wartosci wartiscisdafn, zakoncz zerem"))
    k+=1
#end while

t_10 = [0 for _ in range(10)]
i = 0
while i < k:
    if t[i] > t_10[9]:
        for j in range(k):
            if t[i] > t_10[j]:
                #alter all and insert in
                m = j
                temp = t_10[m]
                t_10[m] = t[i]
                while m < 10-1:
                    temp,t_10[m+1] = t_10[m+1],temp
                    m+=1
                break
    i+=1
print(t_10[9])