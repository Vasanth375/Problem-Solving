arr=[2, 4, 6, 8, 3]
temp=0
for j in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            temp=arr[i+1]
            arr[i+1]=arr[i]
            arr[i]=temp
