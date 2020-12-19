null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    if first == null:
        print("List is empty!")
    while first != null:
        print(first, end='')
        first = first.next
    print()


# stad w dol do komentarza z trescia to zadanie 2 i wś
class Node2:
    # val,next,idx
    def __init__(self, val=0, next=None, idx=0):
        self.next = next
        self.val = val
        self.idx = idx

    def __str__(self):
        return f"{self.idx},{self.val}"


def init(num):
    return Node2(num)


def insertIfNotInList(first, key):
    if first.next == null:
        first.next = Node2(val=key, idx=1)
        return False
    cp = first.next
    while cp.next != null:
        if key == cp.val:
            if cp.idx >= 2:
                return True
            cp.idx += 1
            return False
        cp = cp.next
    if key == cp.val:
        if cp.idx >= 2:
            return True
        cp.idx += 1
        return False
    cp.next = Node2(key, idx=1)
    return False


# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

def delete(cp, cp2):
    cp.next = cp2.next
    del cp2


def check(first, rzadka_tablicka=init(0), last=False):
    if first == null:
        return null
    if first.next == null:
        return first
    insertIfNotInList(rzadka_tablicka, first)
    cp, cp2 = first, first.next
    while cp2 != null:
        if insertIfNotInList(rzadka_tablicka, cp2.val):
            delete(cp, cp2)
            cp, cp2 = cp, cp.next
            continue
        cp, cp2 = cp2, cp2.next
    if last == False:
        return check(first, rzadka_tablicka, True)
    return first


first = Node(1)
for i in range(1, 10):
    a = Node(9, first)
    first = a
wypisz(first)
wypisz(check(first))
