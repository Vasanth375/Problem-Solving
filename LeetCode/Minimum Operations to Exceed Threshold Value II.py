import heapq

nums = [2,11,10,1,3]
k = 10

def greaterEqual(nums, k):
    for val in nums:
        if val < k:
            return False
    return True

count = 0
heapq.heapify(nums)

while nums[0] < k:
    # popping the two smallest elements, directly
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    z = min(x, y) * 2 + max(x, y)
    heapq.heappush(nums, z)     # we are pushing the new element in the heap with exact sorted order
    count += 1

print(count)