import sys
n = 3
arr = [1,3,-1]

n = 4
arr = [5,9,2,6]
max1, min1, max2, min2=arr[0],arr[0],arr[0],arr[0]
for i in range(1, n):
    max1=max(max1, arr[i]-i)
    min1=min(min1, arr[i]-i)
    max2=max(max2, arr[i]+i)
    min2=min(min2, arr[i]+i)
print(max(max1-min1, max2-min2))