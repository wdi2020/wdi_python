null=None
class Node:
    def __init__(self,value = null,next=null):
        self.val = value
        self.next = next
    def __str__(self):
        return f"{self.val}-->"
def wypisz(first):
    while first != null:
        print(first,end='')
        first = first.next
    print()
#12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
#jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
#leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
#dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
#oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
#czy w wyniku operacji moc zbioru uległa zmianie.
def is_grater(napis1,napis2):
    for i in range(max(len(napis1),len(napis2))):
        if i >= len(napis1):
            return False
        if i >= len(napis2):
            return True
        if ord(napis1[i]) == ord(napis2[i]):
            continue
        elif ord(napis1[i]) > ord(napis2[i]):
            return True
        elif ord(napis1[i]) < ord(napis2[i]):
            return False
    return False
def insert(zbior,element):
    if zbior ==null:
        new_elem = Node(element)
        return new_elem
    if is_grater(first.val,element):
        ret = Node(element,first)
        return ret
    prev=null
    curr=zbior
    while curr != null:
        if is_grater(curr.val,element):
            break
        if curr.val == element:
            return zbior
        prev,curr = curr,curr.next
    if element=="z":
        print(prev,curr)
    new_elem = Node(element,curr)
    prev.next = new_elem
    return zbior

first = null
a = ["a","d","c","z","f","g","h"]
for elem in a:
    print(elem)
    first = insert(first,elem)
wypisz(first)