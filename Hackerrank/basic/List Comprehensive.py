#x,y,z,n=1,1,2,3
x=4
y=5
z=6
n=-10
# pushing sublists into list a if condition satisfies
a=[[i,j,k] for i in range(n+1) for j in range(n+1) for k in range(n+1) if 0<=i<=x and 0<=j<=y and 0<=k<=z]
print(a)
b=[k for i,k in enumerate(a) if sum(k) != n]
print(b)