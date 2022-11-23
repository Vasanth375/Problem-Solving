a=[2,6]
b=[24,36, "sai"]


def getTotalX(a, b):
    # Write your code here
    # return len([i for i in range(a[-1],b[0]+1) if all(i%j==0 for j in a) and all(k%i == 0 for k in b) ])
    c=[]
    for i in range(a[-1], b[0]+1):
        if all(i%j == 0 for j in a) and all(k%i == 0 for k in b):
            c.append(i)
    return len(c)

print(getTotalX(a,b))
