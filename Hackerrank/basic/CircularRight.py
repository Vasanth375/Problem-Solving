a = [3,4,5]
k = 2
q = [1,2]

a = [1,2,3]
k = 2
q = [0,1,2]

d = []
n = len(a)

## here this is the best and efficient of O(q) time complexity
for i in q:
    l = (i-k+n)%n
    d.append(a[l])

print(d)
