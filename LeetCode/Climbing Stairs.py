# Concepts used in this prob Dynamic Programming and Memoization
n = 3   # number of steps to reach top of the stairs
k = [1, 1]  # ..., 4(1), 5(1)
for i in range(n):  # simply finding fibonacci series
    k.append(k[-1] + k[-2])
print(k[n])
