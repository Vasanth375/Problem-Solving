N = 4
S = 0

larget = ""

for i in range(N):
    if S >= 9:
        larget += '9'
        S -= 9
    else:
        larget += str(S)
        S = 0
    
if S == 0:
    print(int(larget))
else:
    print(-1)