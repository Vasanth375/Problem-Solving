n = 6
andy = [1, 7, 3, 0, 2, 13]
om = [0, 2, 3, 4, 5, 0]

# n = 3
# andy = [1,3,4]
# om = [3,1,2]

andyl = []
oml = []

count = 0
for i in andy:
    if i != 0:
        count += 1
    else:
        andyl.append(count)
        count = 0
andyl.append(count)
count = 0
for i in om:
    if i != 0:
        count += 1
    else:
        oml.append(count)
        count = 0
oml.append(count)

# print(andyl)
# print(oml)

omlongstreak = max(oml)
andylongstreak = max(andyl)

if andylongstreak > omlongstreak:
    print("OM")
elif andylongstreak < omlongstreak:
    print("Andy")
else:
    print("DRAW")
