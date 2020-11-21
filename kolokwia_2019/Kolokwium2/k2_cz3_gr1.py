#ciezka by byla implementacja w python z tym wskaznikiem :(
class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

def func(elem):
    max_dl = 0
    curr_dl = 0
    cop = 0
    usuwac = True
    while elem != None:
        if cop == elem.val:
            curr_dl += 1
        else:
            if max_dl < curr_dl:
                max_dl = curr_dl
                usuwac = True
            elif max_dl == curr_dl:
                usuwac = False
            #end if
            curr_dl = 1
            cop = elem.val
        #end if
        elem = elem.next
    #end while
    if usuwac :
        return max_dl
    else:
        return 0


t = [1,3,3,3,3,5,7,11,13,13,13,1,2,2,2,3]
elem = Node(t[-1],None)
for i in range(len(t)-1,-1,-1):
    elem = Node(t[i],elem)
print(func(elem))