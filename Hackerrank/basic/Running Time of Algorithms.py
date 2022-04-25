# arr list to sort and check how many iterations have done
arr=[4 ,4 ,3 ,4]
n=0 #N declaration and assigned 0
temp=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                #Incrementing n to 1 for each iteration
                n=n+1 
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
print(n)
# return n