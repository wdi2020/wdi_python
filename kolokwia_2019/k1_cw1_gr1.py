from random import randint
t1= [randint(0,600) for _ in range(50)]
t2 = [randint(0,600) for _ in range(50)]
for i in range(50):
    for j in range(50):
        for k in range(0,25):
            if len(t1) - i - k < 0:
                continue
            if len(t2) - 24 - j + k < 0:
                continue
            temp1 = t1[i:k]
            temp2 = t2[j:24-k]
            sum1 = 0
            sum2 = 0
            for i in temp1:
                sum1 += i
            for i in temp2:
                sum2 += i

            podstawa = 2
            while True:
                suma = podstawa * podstawa
                if suma > (sum1+sum2):
                    break 
                while suma <= (sum1+sum2):
                    if suma == (sum1+sum2):
                        print(f"ta {sum1 + sum2}")
                        exit(0) 
                    suma *= podstawa
                podstawa += 1
print("nie")
