s = "the sky is blue"
# s = "  hello world  "
# s = "a        good       example"

s = s.strip(" ")

s = s.split(" ")

i = 0
while i < len(s):
    if s[i] == "":
        s.remove(s[i])
        i -=1
    i += 1
# print(s)

print(" ".join(s[::-1]))

#########################
s = "  hello world  "
# actual solution with 22ms
s = s.split()

print(" ".join(reversed(s)))