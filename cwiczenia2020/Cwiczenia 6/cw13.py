def wypisz(tab):
def zmniejsz(num):
def reku(num,curr_num,tab_curr):
    if curr_num == 2:
        return [1,1]
    if tab_curr == []:
        for i in range(1,curr_num):
            tab_curr[0] = num-i
            tab_curr[1] = i
            if tab_curr[1] != 1:
                reku(num,)
    while tab_curr[0] >= tab_curr[1]:

def func(num):
    print(num)
    reku(num,num,[0 for _ in range(num)])