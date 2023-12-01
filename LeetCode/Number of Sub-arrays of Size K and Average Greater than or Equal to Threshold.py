arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

# arr = [11,13,17,23,29,31,7,5,2,3]
# k = 3
# threshold = 5

res = 0
curSum = sum(arr[:k-1])

for L in range(len(arr) - k + 1):
    curSum += arr[L + k - 1]
    if (curSum / k) >= threshold:
        res += 1
    curSum -= arr[L]
print(res)

# # My Solution Failed at 68th Case out of total 69 cases
# count = 0

# for i in range(len(arr) - k+1):
#     if (sum(arr[i:i+k])//k) >= threshold:
#         count += 1
# print(count)
