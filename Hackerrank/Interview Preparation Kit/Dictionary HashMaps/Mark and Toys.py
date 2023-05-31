prices = [1, 2, 3, 4]
k = 7

l = []
list1 = []
m = 0
for i in prices:
    if m <= k:
        m += i
        l.append(i)
    else:
        list1.append(l)
        l = []
        m = 0
print(list1)
