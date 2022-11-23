S = '123'

print(any(i.isalnum() for i in S))
# [True, True, True]

print(any(i.isalpha() for i in S))
print(any(i.isdigit() for i in S))
print(any(i.islower() for i in S))
print(any(i.isupper() for i in S))


