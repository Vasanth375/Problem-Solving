def checkConsecutive(array):
    sortedd = sorted(array)
    for q in range(len(sortedd)-1):
        if sortedd[q]+1 != sortedd[q+1]:
            return False
    return True

nums = [1,2,3,4,3,2,5]
k = 3
nums = [2,2,2,2,2]
k = 4
result = []

for i in range(len(nums)):
    l = nums[i:i+k]
    if l == sorted(nums[i:i+k]) and len(l) == k and checkConsecutive(nums[i:i+k]):
        result.append(max(l))
    elif len(l) == k:
        result.append(-1)


print(result)