num = 9669
# num = 9999

a =  str(num)
k = [a]
for i in range(len(a)):
    l = list(a)
    if a[i] == '9':
        l[i] = '6'
    elif a[i] == '6':
        l[i] = '9'
    k.append("".join(l))
        
k = [int(i) for i in k]
print(max(k))