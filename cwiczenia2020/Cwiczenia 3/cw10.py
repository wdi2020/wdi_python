from random import randint
MAX = 10000
t = [randint(1,1000) for _ in range(MAX)]
dl_max = 0
count = 2
a1 = t[0]
r = t[1] - t[0]

i = 2
while i < len(t):
    if t[i-1] + r == t[i]:
        count += 1
    else:
        if count > dl_max:
            dl_max = count
        count = 2
        a1 = t[i-1]
        r = t[i] - t[i-1]
    i+=1

if count > dl_max:
    dl_max = count
print(dl_max)