# Accepted
n = 1012
#n = 111
nl = list(str(n))
u = [int(x) for x in nl]
count = 0
for i in u:
    if  (i != 0):
        if n%i == 0:
            count+=1
print(count)