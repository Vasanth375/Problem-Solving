'''
Sets are an unordered collection of unique values. A single set contains values of any immutable data type.
'''
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
for i in sorted(a.symmetric_difference(b)):
    print(i)
