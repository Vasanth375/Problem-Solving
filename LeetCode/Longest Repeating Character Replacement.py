# Problem solved using Sliding Window approach
# review again the statement and video in neetcode

s = "ABAB"
k = 2

# s = "AABABBA"
# k = 1
# s = "AAAA"
# k = 2

count = {}
res = 0
l = 0
maxf = 0
for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    maxf = max(maxf, count[s[r]])
    while (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l+1)
print(res)

# left, right = 0, 1
# maxCount = 0
# maxChar = ""
# windowsize = 0
# res = 0
# while right <= len(s):
#     hashmap = defaultdict(int)
#     for i in s[left:right]:
#         hashmap[i] += 1
#         if maxCount < hashmap[i]:
#             maxCount = hashmap[i]
#             maxChar = i
#     # print(hashmap)
#     # print(maxChar, maxCount)
#     windowsize = left + right
#     if windowsize - maxCount <= k:
#         res = windowsize
#     right += 1
# left += 1
# print(res)

# while left < right - 1:
#     hashmap = defaultdict(int)
#     for i in s[left:right]:
#         hashmap[i] += 1
#         if maxCount < hashmap[i]:
#             maxCount = hashmap[i]
#             maxChar = i
#     # print(hashmap)
#     # print(maxChar, maxCount)
#     windowsize = left + right
#     if windowsize - maxCount <= k:
#         res = windowsize
#     # print(hashmap)
#     left += 1

# print(res)
