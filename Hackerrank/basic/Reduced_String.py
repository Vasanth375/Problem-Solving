
string=""
name=list('aa')
# print(name)
def add1s():
    for i in range(len(name)-1):
        if name[i]==name[i+1]:
            name[i],name[i+1]='1','1'
    

# print(name)

def removeFunction():
    global string
    for i in range(len(name)):
        n=name[i]
        if n.isalpha()==True:
            string+=n

# print(string)

add1s()
removeFunction()
name=list(string)
# print(name)
if name[0]==name[1]:
    name.remove(name[1])
    name.remove(name[0])
    ' '.join(name)
    print(name)
else:
    print(string)
 