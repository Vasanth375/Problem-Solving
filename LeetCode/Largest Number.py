from functools import cmp_to_key

def compare(n1, n2):
    if n1+n2 > n2+n1:
        return -1
    else:
        return 1

nums = [3,30,34,5,9]

for i, n in enumerate(nums):
    nums[i] = str(n)

nums = sorted(nums, key=cmp_to_key(compare))

if nums.count("0") == len(nums):
    print(0)
else:
    print(nums)
