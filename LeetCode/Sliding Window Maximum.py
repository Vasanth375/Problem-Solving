## SOLVED - Hard problem
# Monotonic stack
from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [7,2,4]
k = 2
# nums = [1]
# k = 1

arr = []
queue = deque()
l = 0
r = 0
while r < len(nums):
    
    # removing all smaller values
    while queue and nums[queue[-1]] < nums[r]:
        queue.pop()
    
    queue.append(r)
        
    if l > queue[0]:
        queue.popleft()
    
    if (r+1) >= k:
        arr.append(nums[queue[0]])
        l += 1
    r += 1
print(arr)