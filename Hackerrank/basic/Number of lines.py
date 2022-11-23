x1,v1,x2,v2=2,1,1,2
#x1, v1, x2, v2 = 1, 8 , 2, 5
# 1. 8 testcases FAILED
# 2. 5 testcases FAILED
if x1>1000:
    print("YES")
else:
    k1=[i for i in range(x1,(x1+v1),v1)]
    # print(k1)
    k2=[i for i in range(x2,(x2+v2),v2)]
    # print(k2)
    n=0
    for i,v in enumerate(k1):
        for j,m in enumerate(k2):
            if v == m and i == j:
                print(v,m,i,j)
                print("YES")
                n=n+1
                break
    if n==0:
        print("NO")