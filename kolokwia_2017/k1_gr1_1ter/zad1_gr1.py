def czy_roznocyfrowe(num1,num2):
    for i in num1:
        for j in num2:
            if i == j:
                return False
    return True

num1 = int(input("num1 :"))
num2 = int(input("num2 :"))
i = 2
while i<=16:
    ne1 = []
    copy1 = num1
    while copy1>0:
        temp = copy1 %i
        if temp >=10:
            temp = chr(55+temp)
        ne1.append(str(temp))
        copy1//=i

    ne2 = []
    copy2= num2
    while copy2>0:
        temp = copy2 %i
        if temp >=10:
            temp = chr(55+temp)
        ne2.append(str(temp))
        copy2//=i

    if czy_roznocyfrowe(ne1,ne2):
        print(i)
        exit(0)
    i+=1

print("nie da sie")
