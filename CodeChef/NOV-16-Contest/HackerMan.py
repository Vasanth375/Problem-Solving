# program code: PRIMEDICE
from math import sqrt
def isPrime(n):
    if n<=1:
        return False

    
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True
    
t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    if isPrime(a+b):
        print("Alice")
    else:
        print("Bob")