n = int(input(">"))

count = 0
i = n
flag = False
while i>4:
    if i%5 ==0:
        flag = True
        c = i
        while c%5==0:
            count+=1
            c//=5
        #end while
    #end if
    if flag==True:
        i-=5
    else:
        i-=1
#end while

ilosc_5,ilosc_2 = count,count
wynik = 1
while n>0:
    copy = n

    while copy%5 ==0 and ilosc_5>0:
        copy //= 5
        ilosc_5-=1
    #end while

    while copy%2==0 and ilosc_2>0:
        copy//=2
        ilosc_2-=1
    #end while
    if(wynik > 32657):
        print("JAPIERDOLE")

    wynik *= copy

    if wynik>10:
        wynik = wynik%10
    #end if

    n-=1
#end while

print(wynik)