# Accepted
mat = [[1,2],[3,4]] 
r = 4
c = 1

# checking if the original matrix length and the given parameters length is equal or not
if (len(mat)*len(mat[0]) == r*c):
    
    # combining the all elements into single list
    a = mat[0]
    for i in range(1, len(mat)):
        a.extend(mat[i])

    # print([a])

    # inserting the single list according to the given parameters
    new_mat = []
    l = 0
    for i in range(r):
        k = []
        for j in range(c):
            k.append(a[l])
            l+=1
        new_mat.append(k)
        
    print(new_mat)

else:

    # if condition fails return original array
    print(mat)


