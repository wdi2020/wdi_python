null = None
class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    while first != null:
        print(first, end='')
        first = first.next
    print()

'''
14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
element listy o wartościach typu int, usuwającą wszystkie elementy, których
wartość dzieli bez reszty wartość bezpośrednio następujących po nich
elementów. 
'''
def delete(cp, cp2):
    cp.next = cp2.next
    del cp2
    return cp

def check(first):
    flag = True
    while flag:
        flag=False
        if first==null:
            return null
        if first.next==null:
            return first
        if first.next.val%first.val==0:
            first = first.next
            flag = True
            continue
        if first.next.next==null:
            return first
        cp=first
        cp2=first.next
        while cp2.next!=null:
            if cp2.next.val%cp2.val==0:
                delete(cp,cp2)
                flag = True
            cp,cp2=cp2,cp2.next
    return first

first=Node(8)
for i in range(1,12):
    a = Node(4,first)
    first = a
wypisz(first)
wypisz((check(first)))