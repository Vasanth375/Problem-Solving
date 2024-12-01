## 100% Beats 0ms in python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self) -> None:
        self.head = None

    def display(self):
        """display method will traverse through linked list and display each data in it"""

        current = self.head  # current points to head

        while current:  # checking if current is pointing to None or not
            print(current.data, end=" ")
            current = current.next  # current is now pointing to next node
        print()
    def getLength(self, head):
        """returns the length of the linkedlist"""
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length
    def insert(self, data):
        """Insert method used to creating new data
        to existing data or very basic level of
        linkedlist insertion"""

        temp = Node(data)  # creating new node
        if self.head is None:  # checks if head is pointing to None or notx
            # this block of code is executed only once in the whole life of the program
            self.head = temp  # now created head points to new node
            return 0

        # if the above if condition goes False interpreter comes below
        current = self.head  # now head points to current
        while current.next is not None:  # checking if the current's next is not None
            current = current.next
        current.next = temp  # current.next is now pointing to newly created node # type: ignore

    def ReorderList(self, head):
        '''
        1. Split the linkedlist using fast and slow pointers and point a pointer as first and last
        2. reverse second list
        3. Now using two pointers iterate both lists and connect the links 
        '''
        #1
        curr = head.head
        first = curr
        next = curr
        while curr is not None:
            if next.next is None:
                break
            if next.next is not None:
                next = next.next
                if next.next is not None:
                    next = next.next
                else:
                    break
            else:
                break
            curr = curr.next
        last = curr.next
        curr.next = None

        ##2 Reversing the links of second list
        prev = None
        c = None
        nex = None

        while last is not None:
            nex = last.next
            last.next = prev

            prev = last
            last = nex
        last = prev

        #3
        while first is not None and last is not None:
            k = first.next
            first.next = last
            
            l = last.next
            last.next = k

            first = k
            last = l
        
        curr = head.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
                

list = Solution()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(6)
list.insert(7)
list.ReorderList(list)
# list.display()
