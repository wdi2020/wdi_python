# 3. Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
# liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
# w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.
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
        while null != cp2:
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


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


def check(first: Node, second: Node, third: Node):
    f1, f2 = null, first
    s1, s2 = null, second
    t1, t2 = null, third
    cnt = 0
    while f2 != null and s2 != null and t2 != null:
        if f2.val == s2.val == t2.val:
            if f1 != null:
                f1.next = f2.next
                del f2
                f2 = f1.next
            else:
                first = first.next
                f2 = first
            if s1 != null:
                s1.next = s2.next
                del s2
                s2 = s1.next
            else:
                second = second.next
                s2 = second
            if t1 != null:
                t1.next = t2.next
                del t2
                t2 = t1.next
            else:
                third = third.next
                t2 = third
            cnt += 3
            continue
        if f2.val > s2.val:
            s1, s2 = s2, s2.next
        elif s2.val > f2.val:
            f1, f2 = f2, f2.next
        elif t2.val > f2.val:
            f1, f2 = f2, f2.next
        elif f2.val > t2.val:
            t1, t2 = t2, t2.next

    return first, second, third, cnt


tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tab2 = [1, 3, 5, 7, 9, 11]
tab3 = [0, 1, 2, 3, 4, 6, 8, 9]
print(tabToLista(tab1))
print(tabToLista(tab2))
print(tabToLista(tab3))
first, second, third, cnt = check(tabToLista(tab1).first, tabToLista(tab2).first, tabToLista(tab3).first)
print(lista(first))
print(lista(second))
print(lista(third))
print(cnt)
