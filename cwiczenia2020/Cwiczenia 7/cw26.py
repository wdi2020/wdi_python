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


# 26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
# drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
# list, funkcja powinna zwrócić wartość logiczną.


def czy_zawiera(wieksza, mniejsza):
    if wieksza == null:
        return False
    if mniejsza == null:
        return True
    cp = wieksza
    while cp != null:
        buf = mniejsza
        while buf != null:
            if cp == buf:
                return True
            buf = buf.next
        cp = cp.next


first = Node(4, Node(2, Node(3, Node(5, Node(3, Node(1, Node(0, null)))))))
second = Node(0, null)
cp = second
for i in range(10):
    a = Node(i, second)
    second = a
cp.next = first.next.next
wypisz(first)
wypisz(second)
print(czy_zawiera(second, first))
