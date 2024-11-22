nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]

nums1 = [3,1,5,7,9,2,6]
nums2 = [1,2,3,5,6,7,9,11]

k = []
for i in nums1:
    ind = nums2.index(i)
    m = nums2[ind:]
    for j in m:
        if j > i:
            k.append(j)
            flag = True
            break
    if not flag:
        k.append(-1)
print(k)