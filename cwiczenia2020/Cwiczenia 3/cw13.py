from random import randint

if __name__ == "__main__":
    MAX = 100
    # t = [randint(1,2) for _ in range(MAX)]

    #przyklad
    t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]

    dl_max = 0
    count = 0
    i = 0
    j = len(t)-1
    while i < len(t):
        j = len(t)-1
        while j>=0:
            if t[i] == t[j]:
                ci = i
                cj = j
                count = 0
                while ci < len(t) and cj >= 0:
                    if t[ci] == t[cj]:
                        count += 1
                    else:
                        break
                    ci+= 1 
                    cj-=1
                if count > dl_max:
                    dl_max = count
                
            j-=1
        i+=1
    print(dl_max)