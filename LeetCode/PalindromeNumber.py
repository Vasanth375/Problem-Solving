#Accepted
x = -121
x = list(str(x))
y = x.copy()
y.reverse()
if x[0] == '-' or x[0] == '+':
    print(False)
else:
    if x == y:
        print(True)