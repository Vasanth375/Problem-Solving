# After 3 attempts
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [2,0,0]

maxind = 0
if len(nums) == 1 and nums[0] == 0:
    print( True)
for i in range(len(nums)):
    if i > maxind:
        print( False)
    if i == len(nums)-1:
        print( (True))
    if (i+nums[i]) > maxind:
        maxind = i+nums[i]
if maxind >= len(nums):
    print( (True))
print( False)