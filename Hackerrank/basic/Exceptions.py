T = int(input())
for _ in range(T):
    try:
        a, b =map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e1:
        print("Error Code:", e1)
    except ValueError as e2:
        print("Error Code:",e2)
