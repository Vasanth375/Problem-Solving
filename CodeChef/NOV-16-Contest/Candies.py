# failed
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a[:n])
    c = set(a[n:])
    flag = True
    if len(b) == len(c):
        print("Yes")
    else:
        print("No")
    # for i,j in zip(b,c):
    #     if i == j:
    #         flag = False
    # if flag:
    #     print("Yes")
    # else:
    #     print("No")