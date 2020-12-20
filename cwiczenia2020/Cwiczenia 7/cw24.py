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


# 24. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.

def dlugosc_przed_cykl(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    cnt = 0
    p = first
    while p != q:
        p = p.next
        q = q.next
        cnt += 1
    return cnt
