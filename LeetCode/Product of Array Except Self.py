nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]

pre = 1
post = 1
k = [1]
# here we are calculating the prefix of the nums form 0 to n
# multiplying the initial pre value with current nums value
# updating the pre value to the value multiplied value
for i in range(len(nums)-1):
    k.append(pre*nums[i])
    pre *= nums[i]

# same as above, calculating the postfix from n-1 to 0, from the above calculated list
# updating the k[i] is multiplied with initial post value and storing in the same location
# updating the post value with original list of i index 
i = len(nums)-1
while i >= 0:
    k[i] *= post
    post *= nums[i]
    i -= 1
print(k)
