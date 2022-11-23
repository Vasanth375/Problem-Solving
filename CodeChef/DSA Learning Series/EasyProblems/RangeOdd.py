l = 2
r = 8
k = []
for i in range(l, r+1):
    if i%2!=0:
        k.append(i)
print(*k)