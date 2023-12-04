num = "6777133339"
# num = "2300019"
# num = "42352338"
# num = "222"
# num = "1221000"
if len(set(num)) == 1 and len(num) == 3:
    print(num)
else:
    k = []

    l = []
    maxV = 0
    for i in range(len(num)-2):
        b = num[i:i+3]
        B = set(b)
        m = "".join(B)
        if len(B) == 1 and m not in l:
            k.append(b)
            if maxV < int(m):
                maxV = int(m)
        l.append(m)
    k.sort()
    print(k[-1])
