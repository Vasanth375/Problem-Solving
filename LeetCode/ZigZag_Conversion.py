# Use pythontutor to find where you want to resume your work

s = "PAYPALISHIRING"
numRows = 4

cols = len(s)
matrix = []
for i in range(numRows):
    k = [' ']* cols
    matrix.append(k)

k = 1
l = 0
for i in range(0, cols, numRows-1):
    if l == len(s):
        break
    j = 0
    while j < numRows:
        if l == len(s):
            break
        matrix[j][i] = s[l]
        l += 1
        j += 1
    
    j -=2
    while j > 0:
        if l == len(s):
            break
        matrix[j][k] = s[l]
        l += 1
        j -=1
        k += 1
    k +=1

result = ""
for m in matrix:
    k = "".join(m).replace(" ", '')
    result += k
print(result)