#Accepted

def NoLines(x1,v1, x2,v2):
    for i in range(1,10000):
        '''Loop through from 1 to 10000 and check the condition
        return YES if condition is true or NO'''
        x1 += v1   
        x2 += v2
        if x1 == x2:
            return('YES')
    return('NO')

x1,v1,x2,v2=2,1,1,2
print(NoLines(x1,v2, x2,v2))