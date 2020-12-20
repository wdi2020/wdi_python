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


def jest_cyklem(first):
    if first == null:
        return False
    if first.next == null:
        return False
    p, q = first, first
    while q != null and q.next != null and q.next.next != null:
        p, q = p.next, q.next.next
        if p == q:
            return True
    return False


def dlugosc_przed_cykl(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    cnt = 0
    p = first
    while p != q:
        p = p.next
        q = q.next
        cnt += 1
    return cnt


# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.

def get_last_(first):
    if not jest_cyklem(first):
        return null
    cnt = dlugosc_przed_cykl(first)
    p = first
    while cnt != 1:
        p = p.next
        cnt -= 1
    return p


first = Node(1, null)
cp = first
for i in range(12):
    a = Node(10 - i, first)
    first = a

cp2 = cp
for i in range(100):
    a = Node(i, cp)
    cp = a
cp2.next = cp
print(get_last_(first))
