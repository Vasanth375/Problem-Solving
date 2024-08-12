from heapq import *

k = []
nums = [4,3,2,5]
heapify(nums)
print(heappop(nums))
print(nlargest(1,nums)[0])