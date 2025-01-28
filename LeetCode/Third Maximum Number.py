from collections import Counter

nums = [3,2,1]
nums =[1,2,2,5,3,5]
k = Counter(nums)
i = 2
keys = list(k.keys())[::-1]
keys.sort(reverse=True)

if k[keys[i]] > 1:
    print(keys[i])
else:
    print(max(keys))
