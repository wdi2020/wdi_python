#1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listyodsyłaczowej.
#-czy element należy do zbioru
#-wstawienie elementu do zbioru
#-usunięcie elementu ze zbioru
class Node:
    def __init__(self,value = None):
        self.val = value
        self.next = None
def elem(zbior, element):
    p = zbior
    while p != None:
        if p.val == element:
            return True
        p = p.next
    return False
def insert(zbior,element):
    if zbior ==None:
        new_elem = Node(element)
        return new_elem
    prev=None
    curr=zbior
    while curr != None:
        if curr.val == elem:
            return zbior
        prev,curr = curr,curr.next
    new_elem = Node(element)
    prev.next = new_elem
    return zbior
def delete(zbior, el):
    if zbior is None:
        return zbior
    prev = None
    curr = zbior
    if curr.val == el:
        prev = curr.next
        del curr
        return prev
    while curr is not None and curr.val != el:
        prev = curr
        curr = curr.next
    if curr is None:
        return zbior
    prev.next = curr.next
    del curr
    return zbior
def wypisz(first):
    bef = first
    while bef != None:
        print(bef.val)
        bef = bef.next

zbior = None
for i in range(15):
    zbior = insert(zbior,i)
for i in range(15):
    print(elem(zbior,i))
print("---")
delete(zbior, 1)
for i in range(14):
    print(elem(zbior,i))