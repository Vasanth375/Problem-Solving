def hasCycle(self, head):
    s = set()
    curr = head
    while curr:
        if curr not in s:
            s.add(curr)
        else:
            return True
        curr = curr.next
    
    return False