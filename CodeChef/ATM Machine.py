k = 10
a = [3, 5, 3, 2, 1]

l = []

for i in range(0, len(a)):
    if a[i] <= k:
        k -= a[i]
        l.append(1)
    else:
        l.append(0)

print(l)
