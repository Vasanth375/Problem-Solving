n = 4
k = 4

l = []
count = 0
for i in range(1, n+1):
    if n % i == 0:
        l.append(i)

if len(l) >= k:
    print(l[-1])
else:
    print(-1)