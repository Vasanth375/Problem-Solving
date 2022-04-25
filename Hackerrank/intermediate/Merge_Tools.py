'''
divide the string by k number of substring
remove the redundant substring 
print all removed ones
'''
k=3
string='AABCAAADA'


for part in zip(*[iter(string)] * k):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
# string=list(string)
# ab=iter(string)
# #dividing the list into k parts
# Output = [list(islice(ab,k)) for i in range(k)]

# for i in Output:
#     i = list(dict.fromkeys(i))
#     print(*i,sep="")
#     print(end="")
