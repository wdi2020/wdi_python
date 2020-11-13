def cw18(tab1):
    m = 0
    for i in range(len(tab1)):
        if tab1[i] %2 == 1:
            j = len(tab1)-1
            while j>0:
                if tab1[i] == tab1[j]:
                    copyi = i+1
                    copyj = j-1
                    count = 0
                    while copyi < len(tab1) and copyj > 0:
                        if tab1[copyi] == tab1[copyj] and tab1[copyi] %2 == 1 and tab1[copyj] %2 == 1:
                            count+=1
                            copyi-=1
                            copyj+=1
                        else:
                            break
                    if count > m :
                        m = count
                j-=1
    print(m)
if __name__ == "__main__":
    cw18([1,1,3,5,3,4,7,5,3,5,3,1,1,4,3,6,9,8,6,75,34,1,2])