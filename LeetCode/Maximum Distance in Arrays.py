arrays = [[1,2,3],[4,5],[1,2,3]]
#arrays = [[1,4],[0,5]]
arrays = [[1],[0]]
arrays = [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
arrays = [[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]
minarr = []
maxarr = []

# for arr in arrays:

#     minarr.append(arr[0])
#     maxarr.append(arr[-1])

# print(max(maxarr) - min(minarr))
# k = 0
# for i in range(len(arrays)-1):
#     for j in range(i+1,len(arrays)):
#         first = arrays[i]
#         second=arrays[j]
#         maxi = max(abs(second[-1] - first[0]), abs(first[-1]-second[0]), abs(first[0]-second[0]), abs(first[-1]-second[-1]))
#         if (maxi) >k:
#             k = maxi
        
# print(k)

# Greedy Solution
smallest = arrays[0][0]
biggest = arrays[0][-1]
max_distance = 0

for i in range(1, len(arrays)):
    arr = arrays[i]
    max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
    smallest = min(smallest, arr[0])
    biggest = max(biggest, arr[-1])
print(max_distance)