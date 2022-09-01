# importing the string lib to create lower ascii values
import string

def designerPdfViewer(h, word):
    # retrieving the lowercase letters
    alphabets = str(string.ascii_lowercase)
    
    #finding the index of word from lowercase letters
    wordIndex = [alphabets.find(i) for i in word]

    # fetching the data
    Value_H = [h[i] for i in wordIndex]

    # returing the output
    return (len(Value_H) * max(Value_H))

print(designerPdfViewer([1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,7],'zaba'))