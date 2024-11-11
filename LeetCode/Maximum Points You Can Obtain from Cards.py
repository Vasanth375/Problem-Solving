# Sliding Window and Two pointers
cardPoints = [1,2,3,4,5,6,1]
k = 3

lsum = sum(cardPoints[:k])
rsum = 0
rightIndex= len(cardPoints)-1
maxsum = lsum

for i in range(k-1, -1, -1):
    lsum -= cardPoints[i]
    rsum += cardPoints[rightIndex]
    maxsum = max(maxsum, lsum+rsum)
    rightIndex -= 1
print(maxsum)
