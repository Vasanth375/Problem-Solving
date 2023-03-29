# *Accepted
s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
s = "(("
s = "(){}}{"

# checking whether a brackets or sqr brackets or flower brackets
while '()' in s or '[]'in s or '{}' in s:
    # replacing the valid paranthesis with blank string
    # here we learned replacing mulitple values in string in single statment
    s = s.replace('()','').replace('[]','').replace('{}','')

# returning false if len of modified string not equal to zero 
# returns true if s is empty means all the valid paranthesis is replaced with empty string
print(False if len(s) !=0 else True)
