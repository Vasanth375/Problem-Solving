'''
Sliding window approach
'''

target = 7
nums = [2,3,1,2,4,3]
target = 11
nums = [1,1,1,1,1,1,1,1]
target = 4
nums = [1,4,4]

left = 0
right = 0
total = 0

minL = float('inf')     #default minimum value

while right <= len(nums)-1:
    total += nums[right]        # taking right index value to total
    while total >= target:      # deleting left window till total < target
        minL = min(abs(right-left)+1, minL)     # finding minimum value with 0 error adding 1 to difference
        total-=nums[left]
        left += 1
    right += 1

print(0 if minL==float('inf') else minL)