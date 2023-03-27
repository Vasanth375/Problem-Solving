# Accepted
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2,3,4,4,4]
size = len(nums)
insertIndex = 1
for i in range(1, size):
    # Found unique element
    if nums[i - 1] != nums[i]:      
        # Updating insertIndex in our main array
        nums[insertIndex] = nums[i] 
        # Incrementing insertIndex count by 1 
        insertIndex = insertIndex + 1       
print(insertIndex,nums)