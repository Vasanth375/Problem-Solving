from collections import Counter

nums = [3, 2, 3]

# nums = [2, 2, 1, 1, 1, 2, 2]
n = len(nums) // 2

k = Counter(nums)
for i in k:
    if k[i] > n:
        print(i)
        break
