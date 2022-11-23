'''
1. pizza contains 4 slices.
2. there are n friends and x slices, we have to find how many pizzas required for n friends
3. multiply n*x store into a
4. condition a mod 4 greater than or equal to 1 print floor division of a and 4 plus 1
5. else print floor division of a and 4 DON'T increment by 1
'''

n = 1
x = 5

# n = 2
# x = 6
a = n*x
if a%4 >=1:
    print((a//4)+1)
else:
    print(a//4)