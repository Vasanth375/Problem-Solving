# TC(O(N))

nums = [2,3,1,1,4]
#nums = [0]

jumps = 0
l = 0
r = 0
n = len(nums)

# Approach is left and right goes from the index of the nums from l to r
# the far value updated based on max of current far and previous far
# l point to the next to r
# r points to the farest index
while r < n - 1:
    far = 0
    for i in range(l, r+1):
        far = max(i+nums[i], far)
    l = r+1
    r = far
    jumps += 1
print(jumps)

