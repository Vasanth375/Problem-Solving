s = "coaching"
t = "coding"
s = "abcde"
t = "a"
s = "z"
t = "abcde"
# s = "a"
# t = "z"


def appendCharacters(s: str, t: str) -> int:
    i = 0                                           # Two Pointers for string s & t
    j = 0

    # We check if current chars at s & t match.
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            # If they match, then we update our pointers for both
            i += 1
            j += 1
        else:
            # If they don't, then we update pointer for only s and try again.
            i += 1

    # The answer would be the number of unmatched chars in t.
    # We can get that by the differene of length and matched pointer of t.
    return len(t) - j


print(appendCharacters(s, t))
