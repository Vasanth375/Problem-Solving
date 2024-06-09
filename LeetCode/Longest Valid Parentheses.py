s = ")()())"
# s = ""
# s = "()(())"
# s = ')('
# s = '(()()'
s = "()(()"

stack=[]
l=['0']*len(s)
for ind,i in enumerate(s):
    if i=='(':
        stack.append(ind)
    else:
        if stack:
            l[stack.pop()]='1'
            l[ind]='1'
print(max(len(i) for i in ''.join(l).split('0')))

# My Solution worked on 80 cases
# stack = []
# count = 0
# s = list(s)
# while s:
#     k = s.pop(0)
#     if k == "(":
#         stack.append(k)
#         count = 0
#     elif k == ")":
#         while stack:
#             m = stack.pop()
#             if m == "(":
#                 count += 2
#                 break
#     else:
#         break
# print(count)
