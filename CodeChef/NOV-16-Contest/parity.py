t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    n = n[0]
    if n % 2 == 0:
        print("Yes")
    else:
        print("No")