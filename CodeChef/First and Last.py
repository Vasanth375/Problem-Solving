
a = [5,10,15]

count = a[0] + a[-1]
for i in range(len(a)-1):
    k = a[i] + a[i+1]
    if k > count:
        count = k
print(count)
