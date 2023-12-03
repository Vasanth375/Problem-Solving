points = [[1, 1], [3, 4], [-1, 0]]
# points = [[3,2],[-2,2]]
k = 0
for i in range(len(points)-1):
    a, b = points[i]
    x, y = points[i+1]
    k += max(abs(a-x), abs(b-y))
print(k)
