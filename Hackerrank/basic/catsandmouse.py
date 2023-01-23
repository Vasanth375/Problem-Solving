# Accepted
x,y,z = 1,2,3
x,y,z = 1,3,2

xDiff = abs(x-z)
yDiff = abs(y-z)
print([xDiff, yDiff])
if xDiff == yDiff:
    print("Mouse C")
elif min([xDiff, yDiff]) == xDiff:
    print("Cat A")
elif min([xDiff, yDiff]) == yDiff:
    print("Cat B")
