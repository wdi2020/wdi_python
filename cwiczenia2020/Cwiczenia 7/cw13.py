null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    while first != null:
        print(first, end='')
        first = first.next
    print()


# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.
def delete(cp, cp2):
    cp.next = cp2.next
    del cp2
    return cp


def check(first):
    flag = True
    while flag:
        flag = False
        if first == null:
            return null
        if first.next == null:
            return first
        cp = first
        cp2 = first.next
        while cp2 != null:
            if cp.val > cp2.val:
                delete(cp, cp2)
                flag = True
            cp, cp2 = cp2, cp2.next
    return first


first = null
for i in range(9):
    a = Node(i, first)
    first = a
wypisz(check(first))
