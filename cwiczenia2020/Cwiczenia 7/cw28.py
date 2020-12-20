null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        if cp == null:
            return "List is empty!"
        ret = ""
        while cp != None:
            ret = ret + str(cp)
            cp = cp.next
        return ret


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    while first != None:
        print(first, end='')
        first = first.next
    print()


# 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
# nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
# listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.


def get(l1, val):
    if l1.first == null:
        return False
    first = l1.first
    if first.val == val:
        l1.first = l1.first.next
        return True
    cp, cp2 = first, first.next
    while cp2 != null:
        if cp2.val > val:
            return False
        if cp2.val == val:
            cp.next = cp2.next
            del cp2
            return True
        cp, cp2 = cp2, cp2.next
    return False


def check(l1: lista, l2: lista):
    cnt = 0
    while get(l1, l2.first.val):
        l2.first = l2.first.next
        cnt += 1
    cp, cp2 = second, second.next
    while cp2 != null:
        if get(l1, cp2.val):
            cnt += 1
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
            continue
        cp, cp2 = cp2, cp2.next
    return cnt


first = Node(10, null)
for i in range(9):
    first = Node(9 - i, first)
second = Node(11, null)
for i in range(10):
    second = Node(10 - i, second)
l1 = lista(first)
l2 = lista(second)
print(l1)
print(l2)
print(check(l1, l2))
print(l1)
print(l2)
