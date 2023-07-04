from collections import Counter

nums = [2, 2, 3, 2]

k = Counter(nums)

## problem statement
# find the number which is exactly repeated only once
for i in k:
    if k[i] == 1:
        print(i)
        break
