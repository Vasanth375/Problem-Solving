n = 4
time = 5

# n = 3
# time = 2

k = list(range(1,n+1))
for i in range(time):
    l = reversed(k[:-1])
    if len(k) > time:
        break
    k += l
print(k)
print(k[time])