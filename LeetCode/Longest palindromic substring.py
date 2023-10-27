s = "babad"

## using two pointer method we can find whether a string is palindrome or not
# which is an efficient method
def check(i,j):
    left = i
    right = j - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right-=1
    return True

k = ""

# checking all substrings and from n to 0 checking all strings 
# if we found any palindromic string retrun it we don't have to check all the substrings
for length in range(len(s), 0, -1):
    for start in range(0,len(s) - length + 1):
        if check(start, start+length):
            k = s[start:start+length]
            print(k)
            break
# if input is nothing 
print("")
