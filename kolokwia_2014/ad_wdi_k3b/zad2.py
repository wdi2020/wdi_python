null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


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


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


# 2. Dane są dwa jednokierunkowe łańcuchy odsyłaczowe (listy) zbudowane z elementów:
# struct node { int w; node* next; };
# Każdy łańcuch zawiera niepowtarzające się liczby naturalne. W obu łańcuchach liczby są posortowane rosnąco.
# Proszę napisać funkcję usuwającą z każdego łańcucha liczby nie występujące w drugim. Do funkcji należy przekazać
# wskazania na oba łańcuchy, funkcja powinna zwrócić łączną liczbę usuniętych elementów.

def func(first, second):
    f1, f2 = first, first.next
    s1, s2 = second, second.next
    cnt = 0
    while f2 != null and s2 != null:
        if f2.val < s2.val:
            f1, f2 = f2, f2.next
        elif f2.val > s2.val:
            s1, s2 = s2, s2.next
        else:
            s1.next = s2.next
            del s2
            s2 = s1.next
            f1.next = f2.next
            del f2
            f2 = f1.next
            cnt += 2
    while first.val == second.val:
        cnt += 2
        first, second = first.next, second.next
    val = first.val
    cp, cp2 = second, second.next
    while cp2 != null:
        if cp2.val > val:
            break
        elif cp2.val == val:
            cnt += 2
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
        else:
            cp, cp2 = cp2, cp2.next
    val = second.val
    cp, cp2 = first, first.next
    while cp2 != null:
        if cp2.val > val:
            break
        elif cp2.val == val:
            cnt += 2
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
        else:
            cp, cp2 = cp2, cp2.next
    return cnt,first,second


tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tab2 = [2, 3, 4, 6, 8, 10]
val, fir, sec = func(tabToLista(tab1).first, tabToLista(tab2).first)
print(val)
print(lista(fir))
print(lista(sec))
