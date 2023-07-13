n = 509

n = str(n)
s = []
for i in n:
    s.append(int(i))
def digitSum(n):
    n = str(n)
    k = []
    for i in n:
        k.append(int(i))

    if sum(k)%2 != sum(s)%2:
        return (int(n))
    else:
        return digitSum(int(n)+1)

print(digitSum(n))