n=int(input())
mylist=[]

text =input()
mylist = text.split()

ulist=[]
for i in mylist:
    ulist.append(int(i))

print(max(ulist))
