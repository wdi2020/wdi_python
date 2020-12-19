null = None


class Node:
    def __init__(self, val=null, next=null):
        self.val = val
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


# 19. Elementy w liście są uporządkowane według wartości klucza. Proszę
# napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
# funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.

def delete(cp, cp3):
    cp.next = cp3


def check(first):
    if first == null:
        return null
    if first.next == null:
        return first
    if first.next.next == null:
        if first.val == first.next.val:
            return null
        return first
    first = Node(first.val - 1, first)
    cp, cp2, cp3 = first, first.next, first.next.next
    last = -1
    while cp3 != null:
        if cp2.val == cp3.val or cp2.val == last:
            last = cp2.val
            delete(cp, cp3)
            cp2, cp3 = cp3, cp3.next
            continue
        cp, cp2, cp3 = cp2, cp3, cp3.next
    if cp2.val == last:
        delete(cp, cp3)
    return first.next


first = Node(10)
for i in range(10):
    b = Node(10 - i, first)
    first = b
    b = Node(10 - i, first)
    first = b
b = Node(1, first)
first = b
wypisz(first)
wypisz(check(first))
