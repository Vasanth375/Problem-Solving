# # a=input()

# a = "122311"

# a = [int(i) for i in a]
# count = 1
# # sub_list = [[a[i]] for i in range(len(a)-1) if a[i]==a[i+1]]

# final_list = []
# items = ()
# for i in range(len(a)-1):
#     if a[i]==a[i+1] and (a[i] not in items and count not in items):
#         count+=1
#     items = (a[i], count)
#     final_list.append(items)
#     count=1

# print(final_list)

a = {0:9, 2:3, 1:2}
print(a)
for _ in range(len(a)):
    if 1 in a:
        print(True)