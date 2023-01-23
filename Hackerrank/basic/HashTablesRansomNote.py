# Accepted

def StringList(magazine, note):
    magazine_words = {}
    for word in magazine:
        magazine_words.setdefault(word, 0)
        magazine_words[word] += 1
    
    for word in note:
        if magazine_words.get(word, 0) > 0:
            magazine_words[word] -= 1
        else:
            print('No')
            return
    
    print('Yes')

m,n = 6,4

magazine = "give me one grand today night"
note = "give one grand today"
# m,n = 6,5

magazine = "two times three is not four"
note = "two times two is four"

# m,n = 7,4

# magazine = "ive got a lovely bunch of coconuts"
# note = "ive got some coconuts"

# m,n = 15, 17

# magazine = "o l x imjaw bee khmla v o v o imjaw l khmla imjaw x"
# note = "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o"


StringList(magazine, note)