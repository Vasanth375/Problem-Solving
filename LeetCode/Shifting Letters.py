# My approach
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# s = list("zbz")
# shifts = [1,5,1]
# n = 1
# for shiftby in shifts:
#     for i in range(n):
#         k = s[i]
#         indk = alphabet.index(k) + shiftby
#         s[i] = alphabet[indk % 26]
#     n += 1
# print(s)

s = list("abc")
shifts = [3,5,9]
# Accumulate shifts means that we will apply the shifts from the end of the string
# to the beginning. This is because the shifts are applied to the whole string, so we can directly apply the shifts to the last character.
for i in range(len(shifts) - 2, -1, -1):
    shifts[i] += shifts[i + 1]

# Apply shifts
for i in range(len(s)):
    s[i] = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))

print("".join(s))