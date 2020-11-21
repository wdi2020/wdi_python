#Łukasz Pawlak
#Działanie
#algorytm dodaje do zmiiennej pomocniczej szukay ciag a nastepnie go szuka w tablicy

def multi(T):
    max_ = 0
    i = 0
    while i <len(T):
        napis = T[i][0]
        napiss_ = T[i]
        max_curr = 0
        curr_napis = ""
        for j in range(1,len(napiss_)):
            curr_napis += T[i][j]
            if curr_napis == napis:
                max_curr +=1
                curr_napis = ""
            elif len(curr_napis) < len(napis):
                continue
            else:
                napis+=T[i][j]
                curr_napis = ""
        else:
            if max_curr != 0:
                max_curr += 1
            if max_curr > max_:
                max_ = max_curr
        i+=1
    return max_
def multi2(T):
    longest = 0
    for j in T:
        n = len(j)
        idx =1
        while idx <= (n//2) +1:
            if n%idx == 0:
                s = ""
                i = 0
                while len(s) != idx:
                    s+= j[i]
                    i+=1
                # i = 0
                # while i < n//idx:
                    # s += s
                    # i+=1
                s = s * (n//idx)
                if s == j:
                    if n//idx > longest:
                        longest = n//idx
            idx+=1
    if longest == 1:
        return 0
    return longest

print(multi2(["ABCABCABC","AA","ABAABA"]))