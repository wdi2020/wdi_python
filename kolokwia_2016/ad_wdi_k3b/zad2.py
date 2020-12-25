null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


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


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


# Zbiór liczb naturalnych jest reprezentowany jako jednokierunkowa lista. Y-lista to struktura
# reprezentująca dwa zbiory liczb naturalnych (rysunek).
# Proszę napisać funkcję, która dwa zbiory A,B reprezentowane jako Y-lista przekształca w dwa
# zbiory reprezentowane jako niezależne listy. Do funkcji należy przekazać wskaźniki do dwóch
# list, funkcja powinna zwrócić liczbę elementów części wspólnej zbiorów A,B.

def count(first, second):
    cnt = 0
    cp, cp2 = first, second
    while cp.val == cp2.val and cp != null and cp2 != null:
        cnt += 1
        cp = cp.next
        cp2 = cp2.next
    return cnt


def func(first, second):
    cp = first
    nowa_first = null
    while cp != null:
        nowa_first = Node(cp.val, nowa_first)
        cp = cp.next

    cp = second
    nowa_sec = null
    while cp != null:
        nowa_sec = Node(cp.val, nowa_sec)
        cp = cp.next

    return count(nowa_first, nowa_sec)


tab1 = [6, 9, 10, 11]
tab2 = [0, 8, 10]
wspolna = Node(1,Node(2,Node(3,Node(4,Node(5,Node(7,null))))))
first = tabToLista(tab1).first
cp = first
while cp.next != null:
    cp = cp.next
cp.next = wspolna

second = tabToLista(tab2).first
cp = second
while cp.next != null:
    cp = cp.next
cp.next = wspolna
print(func(first,second))
print(lista(first))
print(lista(second))
