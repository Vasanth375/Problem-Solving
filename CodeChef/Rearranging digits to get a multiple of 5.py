a = 1234

l = [a]
flag = False

## loop used to rearrange the number in different ways
for i in range(1, len(str(a))):
    k = str(a)[i:] + str(a)[:i]

    l.append(int(k))

for i in l:
    if i % 5 == 0:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")
