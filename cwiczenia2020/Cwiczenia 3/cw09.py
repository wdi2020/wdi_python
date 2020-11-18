MAX = 100
from random import randint
t = [randint(2,10) for _ in range(MAX)]

dl_max = 0
count = 1
i = 1
while i < len(t):
    if t[i] > t[i-1]:
        count += 1
    else:
        if count > dl_max:
            dl_max = count
        count = 0
    i+= 1

if count > dl_max:
    dl_max = count

print(dl_max)