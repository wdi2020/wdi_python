null= None
class Node:
    #val,next
    def __init__(self,val=0,next=null):
        self.next = next
        self.val = val
    def __str__(self):
        return f"{self.val}"
def wypisz(first):
    while first != null:
        print(first,end='')
        first= first.next
    print()
#9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
#elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
#zwiększającą taką liczbę o 1.
#to dziala ale jak jest przepelnienie na najwyzszym indeksie to wtedy jak sie wypisze liczbe to jest git ale jak sie zrobi co tam jest to jest 10 zamiast 1 0
def dodaj1(first):
    if first == null:
        return Node(1)
    if first.next == null:
        first.val+=1
        return first
    cp = first
    cp2 = first.next
    while cp2.next!=null:
        cp,cp2= cp2,cp2.next
    cp2.val +=1
    if cp2.val == 10:
        cp.next = null
        ret = dodaj1(first)
        cp2.val = 0
        cp.next = cp2
        return ret
    return first

first = Node(9)
for i in range(2,7):
    a = Node(9,first)
    first = a
wypisz(first)
dodaj1(first)
wypisz(first)