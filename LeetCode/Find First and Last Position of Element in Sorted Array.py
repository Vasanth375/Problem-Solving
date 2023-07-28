nums = [5,7,7,8,10, 9, 8,10]
target = 8
nums, target = [1], 1

## Actually they asked to solve the problem in log n time, but i tried to in n and it's accepted
if target not in nums:
    print([-1, -1])

count = []
for i in range(len(nums)):
    if target == nums[i]:
        count.append(i)
print([count[0], count[-1]])
