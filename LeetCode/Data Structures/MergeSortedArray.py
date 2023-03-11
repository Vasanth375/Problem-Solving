# Accepted
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = []
# m = 0
# nums2 = [1]
# n = 1

while 0 in nums1 and len(nums1) != m:
    nums1.remove(0)

#print(nums1)

while 0 in nums2 and len(nums2) != n:
    nums2.remove(0)

nums1.extend(nums2)
nums1.sort()
print(nums1)