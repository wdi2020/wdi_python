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


# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.

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


first = Node(1, null)
cp = first
for i in range(12):
    a = Node(i, first)
    first = a
print(jest_cyklem(first))
cp2 = cp
for i in range(1):
    a = Node(i, cp)
    cp = a
cp2.next = cp

print(jest_cyklem(first))
