grid = [[2,5,4],[1,5,1]]

# each grid has only two rows with N columns
N = len(grid[0])
pre1, pre2 = grid[0].copy(), grid[1].copy()

# finding the prefix sum of each row
for i in range(1, N):
    pre1[i] += pre1[i-1]
    pre2[i] += pre2[i-1]

res = float('inf')
for i in range(N):
    top = pre1[-1]-pre1[i]
    bottom = pre2[i-1] if i > 0 else 0
    sec = max(top, bottom)
    res = min(res, sec)
print(res)