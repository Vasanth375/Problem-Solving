from collections import defaultdict

# O(N*M)
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]

k = defaultdict(list)
for i in nums:
    n = ''
    m = str(i)
    for u in m:
        n += str(mapping[int(u)])
    k[int(n)].append(i)

keys = list(k.keys())
values = k.values()
keys.sort()

res = []
for i in keys:
    res.extend(k[i])
print(res)