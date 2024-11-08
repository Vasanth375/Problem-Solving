arr = [1,2,5,4,3]
#arr = [-20 ,-3916237 ,-357920 ,-3620601 ,7374819 ,-7330761 ,30 ,6246457 ,-6461594 ,266854]

arr.sort()
minv=abs(arr[0]-arr[1])
k = []

for i in range(2,len(arr)-1):
    if abs(arr[i+1]-arr[i]) < minv:
        minv = abs(arr[i+1]-arr[i])

for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1]) == minv:
        k.append(arr[i])
        k.append(arr[i+1])
print(k)