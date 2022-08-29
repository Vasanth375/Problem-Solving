from itertools import product
A = input().split(' ')
A = [int(i) for i in A ]

B = input().split(' ')
B = [int(i) for i in B ]

# this itertools.product() is used to find the cartesian product from the given iterator
f = list(product(A,B))
for k in f:
    print(k,end=" ")