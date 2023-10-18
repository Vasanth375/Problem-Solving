n = 3
count = 0
k = 0
if n == 1:
    print(k+1)
for i in range(1, n+1):
    count += i
    if count == n:
        k = i
        break
    if count >= n:
        k = i-1
        break

print(k)