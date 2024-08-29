bloomDay = [1,10,3,10,2]
m = 3
k = 1

# bloomDay = [7,7,7,7,13,11,12,1]
# m = 2
# k = 3

bloomDay = [7,7,7,7,12,7,7]
m=2
k = 3

bloomDay = [1000000000,1000000000]
m,k=1,1

def possible(bloomDay,day,  k, m):
    count = 0
    ans = 0
    for j in range(len(bloomDay)):
        if bloomDay[j] <= day:
            count += 1
        else:
            ans += (count//k)
            count = 0
    ans += (count//k)
    if ans >= m:
        return True
    return False

# # Brute Force checking from minimum to maximum from the array
# i = min(bloomDay)
# while i <= max(bloomDay):
#     if possible(bloomDay, i, k, m):
#         print(i)
#         break
#     i +=1

# # Binary Search Approach
low = min(bloomDay)
high = max(bloomDay)
ans = high
while low <= high:
    mid = (low+high)//2
    if possible(bloomDay, mid, k, m):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(low)

