k = 0
a = [2, 9, -10, 25, 1]

a.sort()

## at a time pop the first and last elements from the list
for i in range(k):
    a.pop(i)
    a.pop(-1)

print(sum(a) / len(a))
