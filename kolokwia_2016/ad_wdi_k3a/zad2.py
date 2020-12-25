null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        cp2 = self.first.next
        if cp == null:
            return "List is empty!"
        ret = str(cp)
        while cp != cp2:
            ret = ret + str(cp2)
            cp2 = cp2.next
        return ret


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"


# Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej
# rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
# Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
# występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.
def zmien_na_najmniejszy(first):
    cp = first.next
    min = first.val
    while cp != first:
        if cp.val < min:
            return cp
        cp = cp.next
    return first

def func(first, second):
    first = zmien_na_najmniejszy(first)
    second = zmien_na_najmniejszy(second)
    f1, f2 = first, first.next
    s1, s2 = second, second.next
    cnt = 0
    while True:

        if f2.val < s2.val:
            f1, f2 = f2, f2.next
        elif f2.val > s2.val:
            s1, s2 = s2, s2.next
        else:
            s1.next = s2.next
            del s2
            s2 = s1.next
            f1.next = f2.next
            del f2
            f2 = f1.next
            cnt += 2

        if f2 == first or s2 == second :
            break
    while first.val == second.val:
        cnt += 2
        first, second = first.next, second.next
        f1, s1 = first.next, second.next
    return cnt, first, second


def tabToCycleLink(tab):
    first = Node(tab[0], null)
    a = first
    for i in range(1, len(tab)):
        a.next = Node(tab[i], null)
        a = a.next
    a.next = first
    return first


tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tab2 = [11, 12,0,1,  2, 3, 4, 6, 8, 10]
ret, l1, l2 = func(tabToCycleLink(tab1), tabToCycleLink(tab2))
print(ret)
print(lista(l1))
print(lista(l2))
#0wy element sie nie usuwa //todo