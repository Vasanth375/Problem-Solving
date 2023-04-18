import bisect

ranked = [100, 90, 90, 80]
player = [70, 80, 105]

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5,25,50, 120]

ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]

x = []

c = set(ranked)
d = list(c)
d.sort()
for i in player:
    ## bisect left used to find the elements left side of the given i value
    j = bisect.bisect_left(d,i)
    if j != len(d) and d[j] == i:
        x.append(len(d) - j) 
    else:
        x.append(len(d) + 1 - j)
print(x)