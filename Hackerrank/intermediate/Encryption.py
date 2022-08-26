from math import ceil, floor, sqrt

def encryption(s):
    A = []
    n = 0
    # if list has spaces replace it
    s = s.replace(" ", "")

    # converting to list
    s = list(s)

    # finding the length
    length = sqrt(len(s))

    # finding the row and column using length
    row = floor(length) # 
    column = ceil(length) # 

    # checking if row*column less than length
    if row*column < int(len(s)):
        row+=1
    
    # spliting the string into different lists
    for i in range(len(s)):
        A.append(s[i:i+column])

    # declaring a single space list inside the list     
    multiArray = [[' ']]

    # picking the lists what we need
    for i in range(0,len(A), column):
        multiArray.append(A[i])

    # adding spaces at end of the lists because if we print the list vertically it gives index out of range error
    for i in range(1,len(multiArray)):
        if len(multiArray[i]) < column:
            for _ in range(len(multiArray[i]),column):
                multiArray[i].append(' ')

    # removing the single space list added 
    multiArray.remove([' '])   

    # printing the  multiArray elements vertically
    finalArray = []
    for i in range(column):
        for j in range(row):
            if multiArray[j][i] == ' ':
                pass
                break
            else:
                finalArray+=multiArray[j][i]
        finalArray+=' '
    return "".join(finalArray)

# s = "chillout"
#s = "haveaniceday"
s = "iffactsdontfittotheorychangethefacts"

print(encryption(s))