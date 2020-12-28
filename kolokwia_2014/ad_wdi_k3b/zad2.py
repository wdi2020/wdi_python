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
# ale chuj napisalem odwrotny program elo

def func(first, second):
    f1, f2 = null, first
    s1, s2 = null, second
    cnt = 0
    while f2 != null and s2 != null:
        if f2.val == s2.val:
            f1, f2 = f2, f2.next
            s1, s2 = s2, s2.next
        elif f2.val > s2.val:
            if s1 != null:
                s1.next = s2.next
                del s2
                s2 = s1.next
            else:
                s2 = s2.next
                del second
                second = s2
            cnt+=1
        elif f2.val < s2.val:
            if f1 != null:
                f1.next = f2.next
                del f2
                f2 = f1.next
            else:
                f2 = f2.next
                del first
                first = s2
            cnt += 1
    if s2 != null:
        s1.next = null
        cp = s2
        while cp != null:
            temp = cp
            cp = cp.next
            del temp
    if f2 != null:
        f1.next = null
        cp = f2
        while cp != null:
            temp = cp
            cp = cp.next
            del temp
    return cnt, first, second

tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tab2 = [0,2, 3, 4, 6, 8, 10]
val, fir, sec = func(tabToLista(tab1).first, tabToLista(tab2).first)
print(val)
print(lista(fir))
print(lista(sec))
