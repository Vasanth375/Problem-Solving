## Memory Limit Exceeded

from itertools import permutations

s1 = "ab"
s2 = "eidboaooo"

s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"

def generate_permutations(string):
    if len(string) == 1:
        return [string]
 
    permutations = []
    for i in range(len(string)):
        fixed_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in generate_permutations(remaining_chars):
            k = fixed_char + perm
            permutations.append(k)
 
    return permutations
# permstring = generate_permutations(s1)
# k = []

# for i in permstring:
#     k.append("".join(i))
# print(k)
# for i in k:
#     if i in s2:
#         print(True)
#         break

