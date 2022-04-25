#     N.Vasanth
#matrix script
#matrix declaration
try:
    matrix =[
        ["T","s","i"],
        ["h","%","x"],
        ["i"," ","#"],
        ["s","M"," "],
        ["$","a"," "],
        ["#","t","%"],
        ["i","r","!"] 
    ]
    print("original matrix",matrix,end="\n")
    decodedstr=[]
    string=" "
    temp=len(matrix [0])
    index_start=0
    index_end=0

    #setting matrix into a individual string
    for j in range(len(matrix[0])):   #matrix [0] 3 size of a row
        for i in range(len(matrix)):  #matrix  7 size of columns
            decodedstr.extend(matrix [i][-temp])
        temp=temp-1

    print("\nconverted matrix to list ",decodedstr,end="\n")

    for i in range(len(decodedstr)):
        if(decodedstr[i].isalpha()==True):
            index_start=i
            break

    # last string index value finding here returning last
    # character index to remove special symbols from the list
    for i in range(len(decodedstr)):
        if(decodedstr[i].isalpha() ==True):
            index_end=i

    #clearing all special symbols

    for i in range(index_start,index_end):
        if(decodedstr[i].isalpha()==False):
            decodedstr[i]=" "

    # #converting all list values to single string
    print("Decoded String: ",end="")
    print("".join(decodedstr))


except Exception as e:
    print(e)