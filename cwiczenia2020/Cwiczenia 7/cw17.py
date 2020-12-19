null = None


class Node:
    def __init__(self, value=null, next=null, prev=null):
        self.val = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    if first == null:
        print("List is empty!")
    while first != null:
        print(first, end='')
        first = first.next
    print()


# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

def ile_1(num1):
    ilosc = 0
    num = num1
    while num != 0:
        if num % 2 == 1:
            ilosc += 1
        num //= 2
    return ilosc


def check(first):
    cp = first
    while cp != null:
        if ile_1(cp.val) % 2 == 1:
            if cp.next == null:
                cp.prev.next = null
            elif cp.prev == null:
                cp.next.prev = null
                first = cp.next
            else:
                cp.prev.next = cp.next
                cp.next.prev = cp.prev
        cp = cp.next
    return first


first = Node(11)
for i in range(10):
    a = Node(i, first, null)
    first.prev = a
    first = a

wypisz(first)
wypisz(check(first))
