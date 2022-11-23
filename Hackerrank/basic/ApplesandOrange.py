'''
1. given two lists and a and b are the values of apple and orange trees, s and t are the house of the range
2. add 
'''

# s, t, a, b, m, n = 7, 11, 5, 15, 3, 2
# apples = [-2, 2, 1]
# oranges = [5, -6]
s,t,a,b,m,n = 2,3,1,5,1,1
apples = [2]
oranges = [-2]
AtHomeApples, AtHomeOranges = [], []

AtHomeApples = [i+a for i in apples]
AtHomeOranges = [i+b for i in oranges]

appleCount = [1 for i in AtHomeApples if i in range(s, t+1)]
orangeCount = [1 for i in AtHomeOranges if i in range(s, t+1)]

print(len(appleCount))
print( len(orangeCount))