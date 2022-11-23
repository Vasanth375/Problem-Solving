'''
In my theory whatever the element repeated twice in the B list it has to be replaced with the specified element
(the value that is not in B list) that will be in the A list
'''
# 3 testcases passed
A = [10, 11, 12, 5, 14]
B = [8,9,11, 11, 5]

A = [1, 2, 3, 4]
B = [1,2,3,3]

A = [3, 5, 7, 11,5, 8]
B = [5, 7,11, 10, 5, 8 ]

# A= [1]
# B = [1]
temp = []
count = 0
element = None

# finding the element that is not in B list and storing it in the element variable
for i in A:
    if i not in B:
        element = i
        break

# now removing the element that is present more than one times in the B list and at the same time appending the stored element and
# then break the loop 
display = False
for i in B:
    if B.count(i) > 1:
        B.remove(i)
        B.append(element)
        display = True
        break

if display:
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                count += 1
                temp.append((i, j))
                break
else:
    count = 0
print(count)
