# Problem Code:
# MONOPOLY

def Monopoly(x,y,z):
    if x>(y+z):
        return "Yes"
    elif y>(x+z):
        return "Yes"
    elif z>(x+y):
        return "Yes"
    return "No"
t = int(input())
for _ in range(t):
    n,i,u = map(int, input().split())
    print(Monopoly(n,i,u))
    