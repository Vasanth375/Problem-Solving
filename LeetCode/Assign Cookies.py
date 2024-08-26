greedy = [1,5,3,3,4]
cookie = [4,2,1,2,1,3]

# greedy = [1,2,3]
# cookie = [1,1]

l = 0
r = 0
greedy.sort()
cookie.sort()
while r <= len(greedy)-1 and l <= len(cookie)-1:
    if greedy[r] <= cookie[l]:
        r += 1
    l += 1
print(r)