# Accepted
def s(n):
    for i in range(1, 151):
        if n%2 == 0:
            return(n)
        return 2*n
        
n = 77
print(s(n))