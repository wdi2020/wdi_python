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


# 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
# podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
# najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
# dokładnie jednej najdłuższej podlisty rosnącej.

def delete(first, idx_strt, lengh):
    if first == null:
        return null
    if first.next == null:
        return first
    if idx_strt == 0:
        while lengh != 0:
            first = first.next
            lengh -= 1
        return first
    else:
        cp = first
        idx_strt -= 1
        while idx_strt != 0:
            cp = cp.next
            idx_strt -= 1
        cp.next = delete(cp.next, 0, lengh)
        return first


def check(first):
    if first == null:
        return null
    if first.next == null:
        # zostaje usuniete
        return null
    max_idx, max_lengh = 0, 0
    curr_idx, curr_lengh = 0, 1
    do_usuniecia = False
    idx = 0
    cp, cp2 = first, first.next
    while cp2 != null:
        if cp2.val > cp.val:
            curr_lengh += 1
        else:
            if curr_lengh == max_lengh:
                do_usuniecia = False
            elif curr_lengh > max_lengh:
                do_usuniecia = True
                max_idx = curr_idx
                max_lengh = curr_lengh
            curr_lengh = 1
            curr_idx = idx + 1
        cp, cp2 = cp2, cp2.next
        idx += 1
    if curr_lengh == max_lengh:
        do_usuniecia = False
    elif curr_lengh > max_lengh:
        do_usuniecia = True
        max_idx = curr_idx
        max_lengh = curr_lengh

    if do_usuniecia:
        return delete(first, max_idx, max_lengh)
    return first


first = Node(4, Node(2, Node(3, Node(5, Node(3, Node(1, Node(0, null)))))))
wypisz(first)
wypisz(check(first))
