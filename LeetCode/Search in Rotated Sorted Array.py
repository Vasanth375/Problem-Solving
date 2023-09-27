nums = [4,5,6,7,0,1,2,3]
target = 3

# O(n)
for i in range(len(nums)):
    if nums[i] == target:
        print(i) 
        break

# O(log n)
# Find the pivot(Which is finding the left and right index where 
# [4,5,6,7,0,1,2,3] after executing this block of code left at index 4 [4,5,6,7] and right at index 3 [0,1,2,3])
left, right = 0, len(nums)-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] > nums[-1]:
        left = mid + 1
    else:
        right = mid - 1

print(f"Pivot is {left}") # where left is from 0 to left a sorted subarray exist
# where we can perform binarysearch operation and left - 1 to len remaining subarray
def binarySearch(low, high, target):
    print(f"Binary search [{low}, {high}]")
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high=mid-1
        else:
            low = mid+1 
    return -1

if ((answer:= binarySearch(0,left-1, target))!= -1 ):
    print( answer)
print( binarySearch(left,len(nums)-1,target))