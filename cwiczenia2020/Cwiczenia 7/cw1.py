class Node:
    def __init__(self,val=0,next=None):
        self.next = next
        self.val = 0

def is_in_list(first,val):
    cp = first
    while cp != None:
        if cp.val == val:
            return True
        cp = cp.next
    return False

def insert(first,idx,val):
    if idx ==0:
        nod = Node()
        nod.next = None
        nod.val = val
        first = nod
        return first
    idx-=1
    i = 0
    bef=first
    cp = bef.next
    while cp != None and i<idx:
        bef,cp = cp,cp.next
        i+=1
    new_node = Node()
    new_node.next = cp
    new_node.val = val
    bef.next = new_node
    return first

def delte(first,val):
    bef=first
    cp = bef.next
    while cp != None:
        if cp.val == val:
            bef.next = cp.next
            return True
        bef,cp = cp,cp.next
    return False

def wypisz(first):
    bef = first
    while bef != None:
        print(bef.val)
        bef = bef.next

first = None
for i in range(5):
    first = insert(first,i,10-i)
for i in range(5):
    first = insert(first,i+2,20-i)
wypisz(first)
