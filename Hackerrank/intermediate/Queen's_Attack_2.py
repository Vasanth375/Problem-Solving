
n=5 #number of R and C in board
k=0 #number of obstacles

r_q,c_q=4,3
# Queen's position

# Moves of queen
m=0

#Creating static board of nxn format and filling with zeros
board=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

# placing queen on board
board[r_q-1][c_q-1]=1


#Checking for obstacles from left to right
for i in board[r_q-1]:
    if i != -1 and i !=1:
        m=m+1
    else:
        break

#checking for obstacles from top to bottom
for i in range(r_q):
  if board[i][c_q-1] != -1 and board[i][c_q-1] != 1:
      m=m+1
  else:
      break
print(m)