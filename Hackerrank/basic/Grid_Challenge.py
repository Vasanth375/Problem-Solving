'''
1) Given a grid list of strings.
2) Sort each item in grid list and store it i new temp list.
3) Now check condition of normal list temp and sorted temp list
4) if both are same then return YES or NO
'''
#  One TestCase left out of 13
grid=['kc', 'iu']
grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

# Using list comprehensive sorted the grid items and stored in temp
temp=[''.join(sorted(i)) for i in grid]

print(temp)
if temp == sorted(temp):
    print("YES")
    #return "YES"
else:
    print("NO")
    # return "NO"
