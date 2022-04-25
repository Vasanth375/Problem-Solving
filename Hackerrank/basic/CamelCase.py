s="saveChangesInTheEditor"
s=list(s)
n=1
for i in range(len(s)):
    if(s[i].isupper()==False):
        pass
    else:
        n+=1
        
print(n)
'''
1.take isupper() to check whether a character is uppercase or not 
    if the character is uppercase returns true, if not false
2.calculate how many word are there in the strings
'''
