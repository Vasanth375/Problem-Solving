# Two pointer/Sliding window

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

# Two pointers - O(2n)
l = 0
r = 0
zeros = 0
maxlen = 0

while r < len(nums):
    if nums[r] == 0:
        zeros += 1
    
    while zeros > k:
        if(nums[l] == 0):
            zeros -=1
        l += 1
    if (zeros <= k):
        le = r - l + 1
        maxlen = max(maxlen, le)
    r += 1
print(maxlen)

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# most optimized version - O(n)
# we didn't used any inner loop to traverse left to the right position
# here we just sliding the window from left to right
l = 0
r= 0
maxle = 0
zeros = 0
while r < len(nums):
    if nums[r] == 0:
        zeros += 1
    
    if zeros > k:
        if(nums[l] == 0):
            zeros -= 1
        l += 1
    if(zeros <= k):
        le = r - l + 1
        maxle = max(maxle, le)
    r += 1
print(maxle)

