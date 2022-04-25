import random as rd
arr=[1,4,7,2]
k=2
temp=rd.sample(arr,k)
print(temp)
unfair=max(temp) - min(temp)
print(unfair)
# return unfair