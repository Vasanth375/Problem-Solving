# from collections import defaultdict

# a = input()
# a = a.split(" ")

# n = int(a[0])
# m = int(a[1])

# d = defaultdict(list)
# a=[]
# for i in range(n):
#     a.append(input())

# # print(a)

# b = []
# for i in range(m):
#     a.append(input())
# print(a)

# length = len(a)
# j=0
# dicta = {i:j for i in a: j+=1 }

def factorial(n):
    if n == 1:
        return (n)
    else:
        return (n * factorial(n-1))
print(factorial(25))