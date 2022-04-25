'''
1) given a list of elements
2) in the list count from 0 if two elements are same then increment k value by 1 and remove 
    remaining same equal elements where in the list.
'''
#list declaration
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
m,k=0,0
n=len(ar)
#remove specified elements in ar list
def remove_el(m,n):
    ar.pop(n)
    ar.pop(m)

for i in range(n):
    for j in range(1,n):
        if i!=j:
            if ar[i]==ar[j]:
                k+=1
                remove_el(i,j)
                break
    n=len(ar)
# for i in range(n):
#     for j in range(i+1,n):
#         if ar[i]==ar[j]:    
#             k+=1
#             remove_el(ar[j],ar[i])
#             break
#     n=len(ar)
