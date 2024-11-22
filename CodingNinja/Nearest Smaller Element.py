A = [4, 5, 2, 10, 8]
#A = [3, 2, 1]
nge = [-1]*len(A)
stack = []
for i in range( len(A)):
    # for j in range(i, -1, -1):
    #     if A[j] < A[i]:
    #         nge[i] = A[j]
    #         break

    while stack and stack[-1] >= A[i]:
        stack.pop()
    if stack:
        nge[i] = stack[-1]
    stack.append(A[i])
print(nge)
