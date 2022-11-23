cube = lambda x: x*x*x

def fibonacci(number):
    k,l = 0, 1
    
    n = [k,l]
    for i in range(number):
        m = n[i] + n[i+1]
        n.append(m)

    list = n[:-2]
    # list2 = []
    return (list)
    # for i in list:
    #     list2.append(cube(i))
    # return(list2)

print(list(map(cube, fibonacci(5))))

'''
01123
'''