null = None


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

    def is_empty(self):
        return self.first == null


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val


def wypisz(first):
    while first != None:
        print(first, end='')
        first = first.next
    print()


# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
# się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
# drugiej elementy występują w przypadkowej kolejności. Proszę napisać
# funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

def merge(l1: lista, l2: lista):
    if l1.is_empty():
        return null
    if l2.is_empty():
        return null
    cp = l2.first
    while cp != null:
        if cp <= l1.first:
            l1.first = Node(cp.val, l1.first)
        else:
            op, op2 = l1.first, l1.first.next
            while op2 != null and op2 < cp:
                op, op2 = op2, op2.next
            if cp.val != op2.val:
                op.next = Node(cp.val, op2)
        cp = cp.next


first = Node(19, null)
for i in range(9):
    first = Node((9 - i), first)
second = Node(11, null)
for i in range(10):
    second = Node((10 - i), second)
l1 = lista(Node(0, first))
l2 = lista(second)
print(l1)
print(l2)
merge(l1, l2)
print(l1)
