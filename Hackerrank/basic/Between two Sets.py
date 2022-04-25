a=[2,6]
b=[24,36]
temp=[]
for j in range(2):
    for i in range(1,50) :
        if i%a[0] == 0 and i%a[1] == 0 and b[j]%a[1] == 0 and b[j]%a[1] == 0:
            temp.append(i)

temp=list((temp[0],temp[1]))
print(len(temp))
