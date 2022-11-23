arr=[3 ,-7 ,0]
arr.sort()
temp=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        n=abs(arr[i]-arr[j])
        temp.append(n)
print(min(temp))

# min_diff = abs(arr[-1]-arr[0])

# for i in range(len(arr)-1):
#     min_diff = min(abs(arr[i]-arr[i+1]),min_diff)
# return min_diff