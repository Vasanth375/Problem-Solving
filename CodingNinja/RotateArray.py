# Rotating an array
N = int(input())
arr = list(map(int, input().split()))
k = int(input())
l = arr[k:] + arr[:k]
print(*l)
