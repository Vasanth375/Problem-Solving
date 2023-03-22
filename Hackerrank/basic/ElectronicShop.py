# Accepted
b = 60
keyboard = [40, 50, 60]
drive = [5,8,12]

b = 10
keyboard = [3,1]
drive = [5,2,8]

b = 5
keyboard = [4]
drive = [5]


k = []
for i in keyboard:
    for j in drive:
        if i+j <= b:
            k.append(i+j)

if k:
    print(max(k))
else:
    print(-1)