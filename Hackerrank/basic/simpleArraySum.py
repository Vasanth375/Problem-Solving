#Problem Name: Simple Array Sum
a=[1,2,3,4,5]
print(sum(a))
temp=0

#without inbuilt function
for i,v in enumerate(a):
    temp=temp+v
print(temp)
