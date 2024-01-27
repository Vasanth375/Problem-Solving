asteroids = [5, 10, -5]
asteroids = [10, 2, -5]
asteroids = [8, -8]
asteroids = [-2, -1, 1, 2]
asteroids = [-2, -2, -2, 2]
res = []

stack = []
for i in asteroids:
    while stack and i > 0 and stack[-1] < 0:
        diff = i + stack[-1]
        if diff < 0:
            stack.pop()
        elif diff > 0:
            i = 0
        else:
            i = 0
            stack.pop()
    if i:
        stack.append(i)
print(stack)
