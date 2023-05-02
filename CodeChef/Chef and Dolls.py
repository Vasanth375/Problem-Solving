# returing the missing doll from the collection
k = [1,2,1, 3]
d = {}
q = 0
for i in k:
    d[i] = d.get(i, 0) + 1

for i in d:
    if d[i] == 1:
        q = i
        break
print(q)