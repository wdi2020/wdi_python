class Node:
    def __init__(self):
        pass

def is_in_list(first,val):
    cp = first
    while cp != None:
        if cp.val == val:
            return True
        cp = cp.next
    return False

def insert(first,idx,val):
    i = 0
    bef=first
    cp = bef.next
    while cp != None and i<idx:
        bef,cp = cp,cp.next
    new_node = Node()
    new_node.next = cp
    new_node.val = val
    bef.next = new_node

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
