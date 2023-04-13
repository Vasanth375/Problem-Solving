
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]

pushed = [1,0]
popped = [1,0]
stack = []
j = 0

## iterate through the pushed loop
for i in pushed:
    stack.append(i)     # append the loop
    # iterate through while loop checking the condition then pop the top of the loop
    while j < len(popped) and stack[-1] == popped[j]:
        stack.pop()
        j+=1
        ## if in case we pop the last element in the stack check if the stack is empty break the loop or not
        if stack == []:
            break
print(stack)

if stack:
    print(False)
else:
    print(True)