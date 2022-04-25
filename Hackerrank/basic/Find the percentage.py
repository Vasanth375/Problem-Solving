    # Dictionary for names and marks
student_marks={
    'Krishna' :[67 ,68 ,69],
'Arjun': [70 ,98 ,63],
'Malika':[ 52 ,56, 60]

}
x=[]
# Converting dictionary keys into list to check
# query name with x list
x=list(student_marks.keys())
query_name='Malika'

Average=0
for i in range(len(x)):
    if x[i]==query_name:
        y=student_marks[x[i]]
        for j in y:
            Average=Average+j

# Used to print float of 2 precision format
print("{:.2f}".format(Average/len(y)))

