# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def returnInt(self, list1):
        str_list1 = [str(i) for i in list1]
        str_list1.reverse()
        val1 = "".join(str_list1)
        val1 = int(val1)
        return val1

    def retriveDataAndReturnInt(self, curr):
        list1 = []

        while curr!= None:
            list1.append(curr.val)
            curr = curr.next

        return self.returnInt(list1)

    def insert(self, data):
        temp = ListNode(data)   

        if self.head is None:   
            self.head = temp     
            return 

        current = self.head      
        while current.next is not None:     
            current = current.next    
        current.next = temp
        

    def addTwoNumbers(self, l1, l2):
        add1 = self.retriveDataAndReturnInt(l1)
        add2 = self.retriveDataAndReturnInt(l2)
        sum1 = add1 + add2
        sum1 = list(str(sum1))
        sum1.reverse()

        for i in range(len(sum1)):
            self.insert(sum1[i])
        return self.head

# To execute this code first create two linkedlist and pass it as parameter
# 