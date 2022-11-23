# time limit exceeded

n, m = input().split()
n, m = int(n), int(m)
happy = 0
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
    
for i in array:
    if i in A:
        happy+=1
    if i in B:
        happy+=-1

print(happy)
