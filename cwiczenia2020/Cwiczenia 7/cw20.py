null = None


class Node:
    class przedzial:
        def __init__(self, a=0, b=0):
            self.a = a
            self.b = b

        def wsp_pr(self, pr):
            return min(pr.a, self.a), max(pr.b, self.b)

        def zawiera(self, pr):
            return pr.a <= self.a <= pr.b or \
                   pr.a <= self.b <= pr.b

        def __str__(self):
            return f"[{self.a},{self.b}]"

    def __init__(self, val=null, next=null):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    if first == null:
        print("List is empty!")
    while first != null:
        print(first, end='')
        first = first.next
    print()


def check(first):
    if first == null:
        return null
    if first.next == null:
        return first
    buf = first
    flag = False
    cp = first.next
    while first.val.zawiera(cp.val) and cp!=null:
        a = first.val.wsp_pr(cp.val)
        first.val = Node.przedzial(a[0], a[1])
        flag = True
        first.next = cp.next
        cp = cp.next
    cp, cp2 = first.next, first.next.next
    while cp2 != null:
        if first.val.zawiera(cp2.val):
            a = first.val.wsp_pr(cp2.val)
            first.val = Node.przedzial(a[0], a[1])
            flag = True
            cp.next = cp2.next
            del cp2
            cp2 = cp.next
            continue
        cp, cp2 = cp2, cp2.next
    first = first.next
    cp.next = buf
    buf.next = null
    if flag:
        return check(first)
    return first


first = Node(Node.przedzial(15, 19), Node(Node.przedzial(2, 5), Node(Node.przedzial(7, 11), Node(Node.przedzial(8, 12),
        Node(Node.przedzial(5, 6), Node(Node.przedzial(13, 17), null))))))

wypisz(first)
wypisz(check(first))
