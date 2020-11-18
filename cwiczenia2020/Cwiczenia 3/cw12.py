from random import randint
N = 123
t = [randint(1,99) for _ in range(N)]



dl_max_r = 0
count_r = 2
r_r = 0

dl_max_m = 0
count_m = 0
r_m = 0

if t[1] - t[0] >0:
    a1_r = t[0]
    r_r = t[1] - t[0]
elif t[1] < t[0]:
    a1_m = t[0]
    r_m = t[1] - t[0]


i = 2
while i < len(t):
    if t[i-1] + r_r == t[i] and r_r != 0:
        count_r += 1
    else:
        if count_r > dl_max_r:
            dl_max_r = count_r
        if t[i] - t[i-1]>0:
            count_r = 2
            r_r = t[i]-t[i-1]
        else:
            count_r = 0
            r_r = 0
    #end if
    if t[i-1] +r_m == t[i] and r_m != 0:
        count_m += 1
    else:
        if count_m > dl_max_m:
            dl_max_m = count_m
        if t[i] - t[i-1]<0:
            count_m = 2
            r_m = t[i]-t[i-1]
        else:
            count_m = 0
            r_m = 0
    #end if
    i+=1

if count_r > dl_max_r:
    dl_max_r = count_r
if count_m > dl_max_m:
    dl_max_m = count_m
print(dl_max_m,dl_max_r)
print(abs(dl_max_m-dl_max_r))