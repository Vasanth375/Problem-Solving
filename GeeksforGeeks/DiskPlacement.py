import math
n = 17
k = 0
for i in range(1, n):
    for j in range(n, 0, -1):
        if i+j == n:
            if i*j > k:
                k = i*j
k = 0
# Optimized Approach
a = n/2
b = n/2
a = math.ceil(a)
b = math.floor(b)
k = a*b
print(a,b, k)