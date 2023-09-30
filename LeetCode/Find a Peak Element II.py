# Accepted in 4th Submission
# 1073ms - 47MB used

mat = [[1,4],[3,2]]
mat = [[10,20,15],[21,30,14],[7,16,32]]
mat = [[20,43,38,24,31],[36,34,23,28,48],[22,23,45,30,18],[20,17,15,8,47],[13,21,8,48,35],[49,45,12,13,14],[48,31,18,47,38],[49,34,39,19,7]]
mat  = [[48,36,35,17,48],[38,28,38,26,24],[15,9,33,32,6],[49,4,8,10,41]]
mat = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]

k = []
found = False
for i in range(len(mat)):
    # for j in range(i, len(mat)-1):
    j = 0
    while j < len(mat[i]):
        value, top, left, right, bottom = -1, -1, -1, -1, -1,
        # top
        if i-1 >= 0 :
            print(mat[i-1][j], " top")
            top = mat[i-1][j]
        else:
            print(-1, " top")
            

        # bottom
        if i+1 < len(mat):
            print(mat[i+1][j], " bottom")
            bottom = mat[i+1][j]
        else:
            print(-1, " bottom")
            

        # actual value
        print(mat[i][j], " actual value")
        value = mat[i][j]

        # left
        if j-1 >= 0:
            print(mat[i][j-1], " left")
            left = mat[i][j-1]
        else:
            print(-1, " left")


        # right
        if j+1 < len(mat[i]):
            print(mat[i][j+1], " right")
            right = mat[i][j+1]
        else:
            print(-1, " right")

        
        j += 1
        # top 
        
        if value > top and value > right and value > bottom and value > left:
            k.append([i, j-1])
            break
    if found:
        break
        
print(k)