class Node:
    # val,next
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}"

