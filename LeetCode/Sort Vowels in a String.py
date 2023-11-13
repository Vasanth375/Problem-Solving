s = list("ieTwHeOR")
vowels = ['a', 'e', 'i', 'o', 'u']

temp = ""
# Iterating all the vowels and storing in a temp
for i in s:
    if i.lower() in vowels:
        temp += i

temp = list(temp)

# then we just sort function
# all elements are sorted using the ASCII values internally
temp.sort()

# iterating over the s and if any element finds vowel then
# replace it with the temp data where elements are sorted
ans = ""
j = 0
for i in range(len(s)):
    if s[i].lower() in vowels:
        ans += temp[j]
        j += 1
    else:
        ans += s[i]
print(ans)

# # my solution with TLE
# for i in range(len(s)):
#     if s[i].lower() in vowels:
#         for j in range(i+1, len(s)):
#             if s[j].lower() in vowels:
#                 if ord(s[i]) > ord(s[j]):
#                     s[i], s[j] = s[j], s[i]

# print("".join(s))
