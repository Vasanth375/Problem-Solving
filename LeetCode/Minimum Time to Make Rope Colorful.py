colors = "abaac"
neededTime = [1, 2, 3, 4, 5]

colors = list("aaabbbabbbb")
neededTime = [3,5,10,7,5,3,5,5,4,8,1]
k = 0
# Two pointers Approach 

left, right = 0, 1
for right in range(1, len(colors)):
    if colors[left] == colors[right]:
        if neededTime[left] < neededTime[right]:
            k += neededTime[left]
            left = right
        else:
            k += neededTime[right]
        
    else:
        left = right

print(k)
    