'''
1. given a list of integers scores
2. find the minimum and maximum numbers
3. to find minimum items from the list
    min_list = [scores[0]]place the first element as it is
    for loop starts i:
        minimum = min([scores[i+1], min_list[i]])
        min_list.append(scores[i+1])

4. to find maximum items from the list
    max_list = [scores[0]] place the first element as it is
    for loop starts i:
        maximum = max([scores[i+1], min_list[i]])
        max_list.append(scores[i+1])
'''

scores = [3 ,4 ,21 ,36 ,10 ,28 ,35 ,5 ,24 ,42]

# placing the same value for maximum and minimum
min_list = [scores[0]]
max_list = [scores[0]]

# finding the minimum value from the min_list value and scores
for i in range(len(scores)-1):
    min_list.append(min([scores[i+1], min_list[i]]))

# finding the maximum value from the max_list element and scores
for i in range(len(scores)-1):
    max_list.append(max([scores[i+1], max_list[i]]))

# without counting the first element finding the length of the max and min lists
integer_Array = [len(set(max_list))-1, len(set(min_list))-1]
print(integer_Array)