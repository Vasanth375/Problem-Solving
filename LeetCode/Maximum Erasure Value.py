nums = [4,2,4,5,6]

# nums = [5,2,1,2,5,2,1,2,5]

# nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]

# max_sum = 0

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)+1):
#         subarray = nums[i:j]
#         if len(set(subarray)) == len(subarray):  # Check if all elements are unique
#             current_sum = sum(subarray)
#             max_sum = max(max_sum, current_sum)
# print(max_sum)

# efficient solution using two pointers concept
max_sum = 0
current_sum = 0
seen = set()
left = 0
# iterate through the array with the right pointer  
for right in range(len(nums)):
    # if the element is already seen, move the left pointer to remove elements until it's unique
    while nums[right] in seen:
        seen.remove(nums[left])
        current_sum -= nums[left]
        left += 1
    # add the current element to the set and update the current sum
    seen.add(nums[right])
    current_sum += nums[right]
    max_sum = max(max_sum, current_sum)

print(max_sum)
print(seen)