def capitalize(s):
    '''In this function converting string's first letter into capital and seperating the word with space'''
    s = s.split(" ")
    text = ""
    for i in s:
        text+=i.capitalize()
        text+=" "
    return text

print(capitalize("chris alan"))