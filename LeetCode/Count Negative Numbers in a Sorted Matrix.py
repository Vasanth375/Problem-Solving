grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

count = 0
for i in grid:
    k = sum(q < 0 for q in i)
    count += k
print(count)