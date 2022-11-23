'''
# strong Password
1. counting the if the password meets the contraints or not
2. finding the password length
3 returing the max of length of passwordLength minus 6 and length of counted constraints -4  
'''


numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

password = "2bb#A"
#password = "2bbbb"
#password = "Ab1"
#password = "#HackerRank"

passwordLength = len(password)
characterCount = []

for i in password:
    if i in special_characters:
        print("It Contains Special Characters")
        characterCount.append(1)
        break

for i in password:
    if i in numbers:
        print("Contains numbers")
        characterCount.append(1)
        break
        
for i in password:
    if i in lower_case:
        print("Contains LowerCase")
        characterCount.append(1)
        break
        
for i in password:
    if i in upper_case:
        print("Contains UpperCase")
        characterCount.append(1)
        break

print(max(4- len(characterCount),6- passwordLength))
