## Memory Limit Exeeded

s = "leet2code3"
k = 10

# s = "ha22"
# k = 5
  
   
# s = "a2345678999999999999999"
# k = 1

# # s = 'abc'
# # k = 2

# s = "yyuele72uthzyoeut7oyku2yqmghy5luy9qguc28ukav7an6a2bvizhph35t86qicv4gyeo6av7gerovv5lnw47954bsv2xruaej"
# k = 123365626

# s = "cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg"
# k = 480551547

# My approach with MLE
# m = ""
# n = 0
# l =0
# for q in s:
#     if q.isalpha():
#         l += 1
# if l == 1:
#     print(s[0])
# else:
#     for i in s:
#         if i.isdigit():
#             n = int(i)
#             m = m*n
#             if len(m) > k:
#                 break
#         else:
#             m += i

#     # print(m)
#     print(m[k-1])
s = ""
k = 0
# reverse Traversal Approach
# starting from the end of the string and multiplying the length of the
# string with the digit till length is not greater than k
# from end of the string for each iteration of string if digit exist then
# length divided by digit came and doing modulo operator on k with length
# each iteration checking if k==0 or k==length, return i the character where the required key exist
length = 0
n = 0
while length < k:
    if s[n].isdigit():
        length *= int(s[n])
    else:
        length += 1
    n += 1

for i in range(n-1, -1, -1):
    if s[i].isdigit():
        length //= int(s[i])
        k = k%length
    else:
        if (k == 0 or k == length):
            print(s[i])
        length -= 1
