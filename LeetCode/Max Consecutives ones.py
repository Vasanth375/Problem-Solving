nums = [1,1,0,1,1,1]
#nums = [1,0,1,1,0,1]
#nums = [1,1,0,1]
nums = [0, 0]

# Bases cases
# Brute Force method
if nums.count(0) == len(nums):
    print(0)
if len(nums) == 1:
    if nums[0] == 0:
        print(0)
    print(1)

count = 0
maxCount = 0
for i in range(len(nums)-1):
    if nums[i] == 1 and nums[i+1] == 1:
        count = count + 1
        maxCount = max(count, maxCount)
    else:
        count = 0
print(maxCount+1)

# Two Pointers/Sliding window approach - working
nums = [1,1,0,1,1,1]

l = 0
r = 0
maxLe = 0

while r < len(nums):
    # checking if the right is zero and finding the length and storing max length
    if nums[r] != 0:
        le = r - l + 1
        maxLe = max(maxLe, le)
        r += 1
    else:
        # when we reached to zero right will be incremented and left pointing to the right
        r += 1
        l = r
print(maxLe)