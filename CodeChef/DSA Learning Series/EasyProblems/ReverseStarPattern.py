#python3 code to implement above approach
height = int(input())
for row in range(1, height+ 1):
	print(" " * (height - row) +"*" * row)
