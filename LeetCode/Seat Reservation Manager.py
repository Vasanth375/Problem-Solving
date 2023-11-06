## My Solution is Acceptable but its giving TLE 
# class SeatManager:

#     def __init__(self, n: int):
#         self.seats = list(range(1,n+1))
#         self.reserved = [0]*n

#     def reserve(self):
#         k = self.reserved.index(0)
#         self.reserved[k] = 1
#         # print(self.seats[k])


#     def unreserve(self, seatNumber: int) -> None:
#         self.reserved[seatNumber-1] = 0
        


# # Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(5)
# param_1 = obj.reserve()
# param_1 = obj.reserve()
# param_1 = obj.reserve()
# obj.unreserve(2)
# print(obj.seats)
# print(obj.reserved)

## Another Approach is using MinHeap
# we can dynamically maintain a collection of numbers and
# find the smallest number from the collection in the shortest time using minheap
# This data structure is a complete binary tree, where the parent nodes are always
# smaller than the corresponding child nodes, in order to keep the minimum-valued
# element at the root node of the tree. Here, pushing an element and popping an element
# are both logarithmic time operations, but getting the minimum-valued element is a constant time operation.
# implementatio of minheap in python

import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1,n+1))
        

    def reserve(self):
        ## heappop will pops the minimum value from the heap
        seat_number = heapq.heappop(self.seats)
        return (seat_number)

    def unreserve(self, seatNumber: int) -> None:
        # if we try to reserve the seat, then just add this seatNumber to the seats list
        # it push the value to the list based on the lowest or highest value
        heapq.heappush(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
obj = SeatManager(5)
param_1 = obj.reserve()
param_1 = obj.reserve()
param_1 = obj.reserve()
obj.unreserve(1)
obj.unreserve(2)
obj.unreserve(3)
print(obj.seats)

