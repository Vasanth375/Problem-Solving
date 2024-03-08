from collections import defaultdict

k = defaultdict(list)

nums = [1, 2, 3, 2, 1]
for i in nums:
    k[nums.count(i)].append(i)

key = max(list(k.keys()))
print(len(k[key]))
