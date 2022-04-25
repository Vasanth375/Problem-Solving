arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

matA = []
mat = [[int(input()) for x in range (n)] for y in range(m)]

for i in range(n):
    sum=0
    for j in range(m):
        if i == j:
            sum+=mat[j][i]
        print(sum)
