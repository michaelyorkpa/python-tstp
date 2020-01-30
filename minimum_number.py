# Just an example of how to optimize algorithms and calculate execution times.
# Two separate functions that search sequentially and by comparison

import time
import random

#Build a list of random 1,000,000 numbers between 1 and 1,000,000,000 (with no duplicates)
def randomlist():
    num_list = []
    for i in range(1,1000000):
        rand_sel=random.randint(1,1000000000)
        while rand_sel in num_list:
            rand_sel=random.randint(1,1000000000)
        num_list.append(rand_sel)
    return num_list

def seq_search(number_list):
    pass

start_time=time.time()
list_of_num=randomlist()
print ("{} second to compile random number list".format(time.time()-start_time()))