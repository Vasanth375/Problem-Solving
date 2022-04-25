k=2
arr=[1, 5, 3, 4, 2]
n=0
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if (arr[j]-arr[i]) == k:
            n=n+1
print(n)
