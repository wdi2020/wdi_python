# 286,143
#a = int(input("pdoaja liczbeadfa: "))
num =143
dl_ciagu = 0
a0 = -1
for podstawa in range(2,8+1):
    a = num
    while a > 0:
        temp = a % podstawa
        print(temp,end=" ")
        if a0 == -1:
            a0 = temp
            dl_ciagu = 1
        else:
            if temp <= a0:
                a0 = temp
                dl_ciagu+=1
            else:
                if dl_ciagu == 4:
                    print(podstawa)
                    print("Tak")
                    break
                a0 = temp
                dl_ciagu = 1 
        a //= podstawa
    else:
        if dl_ciagu == 4:
            print(podstawa)
            print("Tak")
            break
        a0 =-1 
        dl_ciagu = 0 
        print()
        continue
    break