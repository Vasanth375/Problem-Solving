#Accepted

a = [1,2,2,1]
b = [2,2]

a = [4,9,5]
b = [9,4,9,8,4]

a = [1,2,2,1]
b = [2]

a = [1,2,2,1]
b = [1,2]

def intersection(nums1, nums2):
    #example:
    #nums1 = [1,2,2,1]
    #nums2 = [2,2]
    #output = [2,2]
    #find first 2 and remove from target, continue iterating
    target, iterate = [nums1, nums2] if len(nums2) >= len(nums1) else [nums2, nums1] #iterate will look into target

    if len(target) == 0:
            return []
    i = 0
    store = []
    while i < len(iterate):

         element = iterate[i]

         if element in target:
               store.append(element)
               target.remove(element)

         i += 1

    return store

print(intersection(a,b))