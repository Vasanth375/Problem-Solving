'''
1)there are apple and orange arrays.we have points a and b, from a to left is negative and from a to right is positive.
2)there's a red region between s and t.
3)we have two arrays check each element whether it is positive or not if it is positive then place it to rightside.
4)check how many elements from apples and oranges arrays are between s and t, increase k if apples and oranges element are true.
'''
a,b=4,12
apples=[2,3,-4]
apple=[]
oranges=[3,-2,-4]
orange=[]
#Red region area points
s,t=7,10

for i in range(len(oranges)):
    if oranges[i]>0:
        orange.append(oranges[i])
print(len(orange))

for i in range(len(apples)):
    if apples[i]>0:
        apple.append(apples[i])

print(len(apple))