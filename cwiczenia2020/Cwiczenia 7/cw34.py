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


# to pomocnicza lista
class Node2:
    # val,next
    def __init__(self, val=0, idx=-1, next=null):
        self.next = next
        self.val = val
        self.idx = idx

    def __str__(self):
        return f"{self.idx}({self.val})-->"


def wypisz(first):
    while first != null:
        print(first, end='')
        first = first.next
    print()


# nie wiem jaka nazwa to niech zostanie
def insertIfNotInList(first, key):
    first = Node2(-1, -1, first)
    if first.next == null:
        return Node2(val=1, idx=key, next=null)
    if key < first.next.idx:
        return Node2(val=1, idx=key, next=first.next)
    cp = first
    while cp.next != null:
        if key == cp.next.idx:
            cp.next.val += 1
            return first.next
        elif key < cp.next.idx:
            break
        cp = cp.next
    cp.next = Node2(1, key, cp.next)
    return first.next


def check(first, k, key):
    cp = first
    while cp != null:
        if cp.idx > key:
            return False
        if cp.idx == key and cp.val == k:
            return True
        cp = cp.next
    return False


# 34. Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
# których klucz występuje dokładnie k razy. Do funkcji należy przekazać
# wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
# zwrócić informację czy usunięto jakieś elementy z listy.


def usun(first: Node, k):
    pomocniczy = Node2(1, first.val, null)
    cp, cp2 = first, first.next
    while cp != cp2:
        pomocniczy = insertIfNotInList(pomocniczy, cp2.val)
        cp2 = cp2.next
    wypisz(pomocniczy)
    # tu juz sa w pomocniczy teraz wyciagnac co usunac i to policzyc i usunac
    cnt = 0
    cp3 = first
    while check(pomocniczy, k, cp2.val):
        cnt += 1
        cp3 = cp2.next
        del cp2
        cp2 = cp3.next
        cp.next = cp3
    cp, cp2 = cp3, cp3.next
    while cp2 != cp3:
        if check(pomocniczy, k, cp2.val):
            cnt += 1
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
            continue
        cp, cp2 = cp2, cp2.next
    if cp == cp2:
        if check(first, k, cp2.val):
            cnt += 1
            first = null
    return cnt


last = Node(1, null)
first = Node(1, Node(2, Node(9, Node(3, Node(6, Node(8, Node(0, Node(7, Node(5, Node(3, Node(2, last)))))))))))
last.next = first
print(lista(first))
print(usun(first, 2))
