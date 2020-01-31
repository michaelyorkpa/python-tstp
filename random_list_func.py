import random

def randomlist(size_of_list,max_value):
    num_list = []
    for i in range(size_of_list):
        rand_sel=random.randint(1,max_value)
        while rand_sel in num_list:
            rand_sel=random.randint(1,max_value)
        num_list.append(rand_sel)
    print(num_list)

randomlist(40000,100000)