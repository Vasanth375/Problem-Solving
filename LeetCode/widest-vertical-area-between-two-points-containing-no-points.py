points = [[8, 7], [9, 9], [7, 4], [9, 7]]
# [vertical, horizontal
]
points.sort()

ans = 0
for i in range(len(points)-1):
    if (points[i+1][0] - points[i][0]) > ans:
        ans = points[i+1][0] - points[i][0]
print(ans)
