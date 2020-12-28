# Zadanie 3.
# Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
# nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.
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


def check(first: Node, second: Node):
    f1, f2 = null, first
    s1, s2 = null, second
    cnt = 0
    while f2 != null and s2 != null:
        if f2.val == s2.val:
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
            cnt += 2
        elif f2.val > s2.val:
            s1, s2 = s2, s2.next
        elif s2.val > f2.val:
            f1, f2 = f2, f2.next
    return first, second, cnt


tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tab2 = [1, 3, 5, 7, 9, 11]
print(tabToLista(tab1))
print(tabToLista(tab2))
first, second, cnt = check(tabToLista(tab1).first, tabToLista(tab2).first)
print(lista(first))
print(lista(second))
print(cnt)
