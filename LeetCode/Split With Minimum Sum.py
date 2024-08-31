num = 43258997
num = 687
num = [int(i) for i in str(num)]
num.sort()
print(num)

num1 = ""
num2 = ""
for i in range(0,len(num)):
    if i %2 ==0 :
        num1 += str(num[i])
    else:num2 += str(num[i])
