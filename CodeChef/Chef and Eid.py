n = 3
a = [1, 4, 2]
a = [1, 3, 3]

a.sort()

minV = abs(a[0] - a[1])

for i in range(1, n - 1):
    if abs(a[i] - a[i + 1]) < minV:
        minV = abs(a[i] - a[i + 1])

print(minV)
