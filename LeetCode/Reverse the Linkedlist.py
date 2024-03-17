def reverseList(self):
    """To perform a reverse operation on linkedlist we need three pointers to
    one is previous pointer which points to the previous node and
    current pointer is to point the current node
    next pointer is to point the next node in the linkedlist
    curr pointer will point to the current node(Head Node)
    next pointer will point to the next node (node after the head node)"""
    prev = None
    curr = None
    nex = None

    curr = self.head  # current node to head node

    while curr is not None:
        nex = curr.next  # next node to next reference to current node
        curr.next = prev  # current node points to previous node

        # moving the pointers forward
        prev = curr  # here is the previous node points to the current node
        curr = nex

    ## at the end of linked list operations only prev pointer is connected to node
    # so head is pointing to the previous node
    self.head = prev
