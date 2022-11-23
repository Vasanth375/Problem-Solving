'''
1. finding the minimun distance from the pair of a value using their indices
2. gathering all the pair value's indices into a list
3. returing -1 if no such pairs found
4. return the minimum value by doing like this
each set contains the i and j (i, j) and performing the j-i operation
appending all the computed values into a list and using built in min() function returing the minimum value
'''

#a = [3, 2, 1, 2, 3]
#a = [7, 1,3, 4, 1, 7]
a = [1,2,3,4,10]
count_set=[]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            count_set.append((i, j))
#print(count_set)
if count_set != []:    
    bList = []
    for i in count_set:
        bList.append(i[1]-i[0])
    print(min(bList))
else:
    print(-1)