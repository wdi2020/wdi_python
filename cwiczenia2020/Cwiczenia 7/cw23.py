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


# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.

def dl_cyklu(first):
    p = first
    q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    cnt = 1
    q = q.next
    while p != q:
        q = q.next
        cnt += 1
    return cnt


first = Node(1, null)
cp = first
for i in range(12):
    a = Node(i, first)
    first = a

cp2 = cp
for i in range(1):
    a = Node(i, cp)
    cp = a
cp2.next = cp
print(dl_cyklu(first))
