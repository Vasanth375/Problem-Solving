def binomial(n, k):
    # if k > (n-k) then k should be updated to (n-k) that
    # decreases the k, when we reach to the point like
    # 13 - here in 13 the k is not decreased and
    # 31 - here 31 the k should be decreased
    # Actual Binomial Formula is 
    # k=0 to n (n k) a^n-k b^k
    if k > n-k:
        k = n-k
    res = 1
    # loop till the k
    for i in range(k):
        res = res * (n-i)
        res = res // (i+1)
    return res

def generate(n: int):
    a = []
    for line in range(n):
        k = []
        for i in range(line+1):
            k.append(binomial(line, i))
        a.append(k)
    return a[n-1]

def particularRow(row):
    # Solution by different user
    p=1
    a=[]
    a.append(1)
    for i in range(1,row+1):
        c=p*(row-i+1)//i
        a.append(c)
        p=c
    return a
print(generate(3+1))
print(particularRow(3))
# c:\Users\VASANTH\AppData\Local\Temp\sddefault.jpg