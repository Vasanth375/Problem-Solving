k = [1, 1]
n = 6
for i in range(n-2):
    k.append(k[-1] + k[-2])
print(k[-1])
