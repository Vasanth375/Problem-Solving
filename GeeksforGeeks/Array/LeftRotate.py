# Array rotation by p positions
firstTemp = []
origin = [1,2,3,4,5,6,7,8,9,10,11,12]

d = 4

origin = [1,2,3,4,5]
d = 2

## using the above idea we can rotate an array 
# first start from d to n-1 of array and store it in a temporary array 
for i in range(d, len(origin)):
    firstTemp.append(origin[i])

# and start from 0 to d-1 of array and append it to same temporary array
for i in range(d):
    firstTemp.append(origin[i])
#print(firstTemp)

# try to rotate the original array in-place
k = 0
for i in range(d):
    origin.append(origin[i])

for i in range(d):
    origin.pop(0)

print(origin)

# ********************************
k = []
if d > len(origin):
    d = d%len(origin)
k = origin[d:] + origin[:d]

for i in range(len(origin)):
    origin[i] = k[i]
print(origin)