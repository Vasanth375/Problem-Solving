arr=[2,5,23,6]
cw=0
arr.sort()
for i in range(0,len(arr)-1):
    cw=cw+arr[i]
    
print(cw,end=" ")
cw=0
for i in range(1,len(arr)):
    cw=cw+arr[i]
print(cw)