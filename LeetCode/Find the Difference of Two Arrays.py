## Find the difference between two lists and return the difference
nums1 = [1,2,3]
nums2 = [2,4,6]

ans = []

nums1 = set(nums1)
nums2 = set(nums2)

a = nums1.difference(nums2)
ans.append(list(a))

b = nums2.difference(nums1)
ans.append(list(b))
print(ans)