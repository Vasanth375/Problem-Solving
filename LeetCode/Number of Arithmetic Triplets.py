nums = [0,1,4,6,7,10]
diff = 3

indices = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                indices.append([i,j,k])
print(len(indices))