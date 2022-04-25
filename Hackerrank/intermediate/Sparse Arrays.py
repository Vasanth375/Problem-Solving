strings=['def',
'de',
'fgh']
queries=['de',
'lmn',
'fgh']
temp=[]
a=0
for i in range(len(queries)):
    for j in range(len(strings)):
        if queries[i]==strings[j]:
            a+=1
    temp.append(a)
    a=0
print(temp)

'''
1. taken two strings A and B 
2. note how many strings are there in B by checking each element with A
3. make a list of number of strings which is repeated in B
'''

# string=['ab','ab','abc']
# queries=['ab','abc','bc']