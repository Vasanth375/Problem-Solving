arr=[1 ,2 ,5]
temp=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        n=abs(arr[i]-arr[j])
        temp.append(n)
temp.sort()
n=temp[len(temp)-1]
print(n)