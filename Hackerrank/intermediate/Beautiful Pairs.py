a=[1 ,2 ,3 ,4]
b=[1, 2, 3, 3]
k=len(a)
list=[]


for i in range(k):
    for j in range(k):
        if a[i] == b[j]:
            list.append(tuple([i,j]))
            break

print(list)