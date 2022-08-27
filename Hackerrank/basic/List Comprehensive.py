# x,y,z,n=3,2,3,2

x=4
y=5
z=6
n=-10

# pushing sublists into list a if condition satisfies and also checking each sublist is equal to n or not
# loop from 0 to x+1 only
a=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(a)