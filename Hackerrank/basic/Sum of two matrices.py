k = input()
n, m =k.split()
n = int(n)
m = int(m)
matrixA = []
matrixB = []
  
# For user input
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(m):      # A for loop for column entries
         a.append(int(input()))
    matrixA.append(a)
print(matrixA)

# For user input
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(m):      # A for loop for column entries
         a.append(int(input()))
    matrixB.append(a)

print(matrixB)
result=[]
# iterating by row of A
for i in range(len(matrixA)):
 
    # iterating by column by B
    for j in range(len(matrixB[0])):
 
        # iterating by rows of matrixB
        for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]
 
for r in result:
    print(r)