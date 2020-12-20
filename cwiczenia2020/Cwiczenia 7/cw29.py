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


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}--> "


# 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
# funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
# funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
# łączną liczbę usuniętych elementów.


def check_v2(l1: lista, l2: lista):
    cnt = 0
    while l1.first.val == l2.first.val:
        l1.first = l1.first.next
        l2.first = l2.first.next
        cnt += 1
    l1.first = Node(0, l1.first)
    l2.first = Node(0, l2.first)
    f1, f2 = l1.first, l1.first.next
    s1, s2 = l2.first, l2.first.next
    while s2 != null and f2 != null:
        if f2.val == s2.val:
            cnt += 1
            f1.next = f2.next
            del f2
            f2 = f1.next
            s1.next = s2.next
            del s2
            s2 = s1.next
            continue
        elif f2.val > s2.val:
            s1, s2 = s2, s2.next
        else:
            f1, f2 = f2, f2.next
    l1.first = l1.first.next
    l2.first = l2.first.next
    return cnt


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
print(check_v2(l1, l2))
print(l1)
print(l2)
