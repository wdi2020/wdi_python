#8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
#element listy. Do funkcji należy przekazać wskazanie na first element
#listy.
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
        first= first.next
    print()

def Usunco2(first):
    licznik=1
    cp= first
    cp2=first.next
    while(cp2.next!=None):
        if(licznik%2==1):
            cp.next = cp2.next
        cp,cp2 = cp2,cp2.next
        licznik+=1

first= Node()
for i in range(1,17):
    a = Node(i+1)
    a.next = first
    first=a
wypisz(first)
Usunco2(first)
wypisz(first)