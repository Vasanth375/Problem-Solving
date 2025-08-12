# Pending
class Node:
    def __init__(self, data, head=None):
        self.data = data
        self.next = head

class ListNode:
    def __init__(self, data, head=None):
        self.val = data
        self.next = head
def reverseBetween(head, left: int, right: int):
    dummy = ListNode(0, head)
    
    # reach node at position left
    left_prev, curr = dummy, head
    for i in range(left-1):
        left_prev, curr = curr, curr.next
    
    # reverse left to right
    prev = None
    for i in range(right-left+1):
        tempNext = curr.next
        curr.next = prev
        prev, curr = curr, tempNext
    
    #update pointers
    left_prev.next.next = curr
    left_prev.next = prev
    return dummy.next 
    
    
    

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
# root.next.next.next.next.next = Node(6)
left = 2
right = 4
k = reverseBetween(root, left, right)
while k is not None:
    print(k.data)
    k = k.next