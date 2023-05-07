nums = [10, 4, 8, 3]

leftsum = []
rightsum = []
diff = []
for i in range(len(nums)):
    leftsum.append(sum(nums[:i]))
    rightsum.append(sum(nums[i + 1 :]))
print(leftsum, rightsum)

diff = [abs(i-j) for i,j in zip(leftsum, rightsum)]
print(diff)