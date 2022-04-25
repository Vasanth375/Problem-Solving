'''
A Discrete Mathematics professor has students, he is very frustated with his students
professor decides to cancel class if fewer than some number of students are present 
when class starts. 
inputs--
n= num of testcases
k= num of students want to start class
a=[] list of arriving of each student
if arrived time < 0 student is present
if arrived time > 0 student is absent
and finally compare the number of present student with k
return 'YES' if k>Present , if not return 'NO'
'''
def AngryProfessor(k,a):
    A,P=0,0
    for i in a:
        if i<=0:
            P+=1
        elif i>0:
            A+=1
    if k>P:
        return 'YES'
    return 'NO'
print(AngryProfessor(3,[-1,-3,4,2]))