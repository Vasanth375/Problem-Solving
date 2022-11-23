'''
1. given an array and K value
2. check i<j and ar[i] + ar[j] divisible by k
3. store index or value as tuple in a List object
4. return the length of the stored list
'''

k = 5
ar = [1,2,3,4,5,6]
count = []

for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        if i<j and (ar[i] + ar[j]) % k == 0:
            #count.append((i,j))
            count.append((ar[i], ar[j]))
print(len(count))
