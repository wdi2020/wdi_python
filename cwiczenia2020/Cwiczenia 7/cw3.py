null= None
class Node:
    #val,next
    def __init__(self,val=0,next=null):
        self.next = next
        self.val = val
    def __str__(self):
        return f"{self.val}--->"
def wypisz(first):
    while first != null:
        print(first,end='')
        first = first.next
    print()
#rekurencja
def reku(first,second,new_last):
    if first==null:
        if second!=null:
            buffer = second.next
            second.next = null
            new_last.next = second
            return reku(first,buffer,second)
        else:
            return
    if second==null:
        if first!=null:
            buffer = first.next
            first.next = null
            new_last.next = first
            return reku(buffer,second,first)
        else:
            return 
    if first.val>second.val:
        buffer = second.next
        second.next = null
        new_last.next = second
        return reku(first,buffer,second)
    else:
        new_last.next = first
        buffer = first.next
        first.next = null
        return reku(buffer,second,first)
def strt(first,second):
    new_ = Node()
    ret = reku(first,second,new_)
    return new_.next


#iter
def iter(first,second):
    new_strt = Node()
    new_end = new_strt
    while first!=null and second!=null:
        if first.val>second.val:
            new_end.next = Node(second.val)
            new_end = new_end.next
            a = second
            second = second.next
            del a
        else:
            new_end.next = Node(first.val)
            new_end = new_end.next
            a = first
            first = first.next
            del a
    if second!=None:
        while second!=null:
            new_end.next = Node(second.val)
            new_end = new_end.next
            a = second
            second= second.next
            del a
    if first!=None:
        while first!=null:
            new_end.next = Node(first.val)
            new_end = new_end.next
            a =first 
            first= first.next
            del a
    return new_strt.next


first = Node()
second = Node()
for i in range(5):
    first.next = Node(15-i+2,first.next)
    second.next = Node(15-i+1,second.next)
wypisz(first.next)
wypisz(second.next)
wypisz(iter(first.next,second.next))
wypisz(strt(first.next,second.next))


