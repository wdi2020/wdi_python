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
# Każdy łańcuch zawieraj niepowtarzające się liczby naturalne. W pierwszym łańcuchu liczby są
# posortowane rosnąco, a w drugim nie. Proszę napisać funkcję usuwającą z obu łańcuchów liczby
# występujące w obu łańcuchach. Do funkcji należy przekazać wskazania na oba łańcuchy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów. u
def if_in_list(first: lista, val):
    if first.first == null:
        return False
    if first.first.val == val:
        first.first = first.first.next
        return True
    cp, cp2 = first.first, first.first.next
    while cp2 != null :
        if cp2.val == val:
            cp.next = cp2.next
            del cp2
            return True
        cp, cp2 = cp2, cp2.next
    return False


def func(first_lista, second_lista):
    cnt = 0
    # check pierwszy
    while second_lista.first != null and if_in_list(first_lista, second_lista.first.val):
        cnt += 2
        second_lista.first = second_lista.first.next
    s1, s2 = second_lista.first, second_lista.first.next
    while s2 != null:
        if if_in_list(first_lista, s2.val):
            cnt += 2
            s1.next = s2.next
            del s2
            s2 = s1.next
        else:
            s1, s2 = s2, s2.next
    return cnt


tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tab2 = [0, 1, 2, 1111111111111111111, 4, 511, 6, 7, 8, 12, 5]
lista1 = tabToLista(tab)
lista2 = tabToLista(tab2)
print(func(lista1, lista2))
print(lista1)
print(lista2)
