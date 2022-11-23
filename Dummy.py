# # Apples and Oranges

# # sentence, t, a, b, m, n = 7, 11, 5, 15, 3, 2
# # apples = [-2, 2, 1]
# # oranges = [5, -6]
# sentence,t,a,b,m,n = 2,3,1,5,1,1
# apples = [2]
# oranges = [-2]
# AtHomeApples, AtHomeOranges = [], []
# for i in apples:
#     AtHomeApples.append(i+a)

# for i in oranges:
#     AtHomeOranges.append(i+b)

# appleCount = 0
# for i in AtHomeApples:
#     if i in range(sentence,t+1):
#         appleCount+=1
# print(appleCount)

# orangeCount=0
# for i in AtHomeOranges:
#     if i in range(sentence,t+1):
#         orangeCount+=1
# print(orangeCount)


# missing Characters
# sentence = "8hypotheticall024y6wxz"
# sentence = "0123456789"
# sentence = "abcdefghijklmnopqrstuvwxyz007"
# sentence = "123567890abcdefgijklmnopqrstuvwxyz"
# sentence ="13570fghkmnprtuz"

# k=[0]*123
# result=""
# for i in range(len(sentence)):
#     x=ord(sentence[i])
#     k[x]+=1
# for i in range(48,58):
#     if(k[i]==0):
#         result+=chr(i)
# for i in range(97,123):
#     if(k[i]==0):
#         result+=chr(i)
# print(result)

# string Transformation

sentence = "a Blue MOON"
l=sentence.split()

li=[]
st=""
for i in l:
    st+=i[0]
    for j in range(0,len(i)-1):
        if(i[j].lower()<i[j+1].lower()):
            st+=(i[j+1].upper())
        elif(i[j].lower()>i[j+1].lower()):
            st+=(i[j+1].lower())
        else:
            st+=i[j+1]
    li.append(st)
    st=""
result=""

# for i in li:
#     result=result+" "+i
# print(result.strip())

for i in li:
    result +="".join(i) + " "
print(result)