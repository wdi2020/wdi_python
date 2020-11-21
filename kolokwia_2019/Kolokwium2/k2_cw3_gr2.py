#wskazniki :/
class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next
def funck(elem):
    #elem - obiekt klasy Node
    cop = elem.val
    index_start = 0
    min_dl = 100000
    first_elem = elem
    elem = elem.next
    i = 1
    curr_dl = 1
    curr_idx = 0
    usuwamy = True
    while elem.next != None:
        if elem.val == cop:
            curr_dl+=1
        else:
            if curr_dl != 1 and curr_dl < min_dl:
                min_dl = curr_dl
                index_start = curr_idx
                usuwamy = True
            elif curr_dl != 1 and curr_dl == min_dl:
                usuwamy = False
            cop = elem.val
            curr_idx = i
            curr_dl = 1
        elem = elem.next
        i+=1
    if usuwamy:
        return min_dl
    else:
        return 0

t = [1,3,3,3,3,5,7,11,13,13,13,1,2,2,3]
elem = Node(t[-1],None)
for i in range(len(t)-1,-1,-1):
    elem = Node(t[i],elem)
print(funck(elem))