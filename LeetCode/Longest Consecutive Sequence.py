nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = list(set(nums))
nums.sort()
k = []
l = 0
if len(nums) == 0:
    print(l)
for i in range(len(nums)-1):
    if nums[i]+1 == nums[i+1]:
        l += 1
    else:
        l += 1
        k.append(l)
        l = 0
k.append(l+1)
print(max(k))
