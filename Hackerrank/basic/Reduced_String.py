# Superreduced string 
'''
remove adjacent pairs of the s string
'''

def superReducedString(s):
    s = list(s)
    for _ in range(len(s)):
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s.remove(s[i+1])
                s.remove(s[i])            
                break
    if s is []:return "Empty String"
    else:return "".join(s)

print(superReducedString("aabddvfvvvjf"))