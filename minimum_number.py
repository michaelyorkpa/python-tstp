# Just an example of how to optimize algorithms and calculate execution times.
# Two separate functions that search sequentially and by comparison

import time
import random

#Build a list of random 1,000,000 numbers between 1 and 1,000,000,000 (with no duplicates)
def randomlist():
    num_list = []
    for i in range(100000):
        rand_sel=random.randint(1,10000000)
        while rand_sel in num_list:
            rand_sel=random.randint(1,10000000)
        num_list.append(rand_sel)
    return num_list

def seq_search(number_list):
    prev_num=number_list[0]
    for i in range(100000):
        if number_list[i] < prev_num:
            prev_num=number_list[i]
    return prev_num

start_time=time.time()
list_of_num=randomlist()
print("It took %s seconds to compile random number list" % (time.time()-start_time))
print(list_of_num)

start_time=time.time()
seq_result=seq_search(list_of_num)
print("It took %s seconds to identify the lowest number sequentially." % (time.time()-start_time))
print("The lowest number is: %s"%seq_result)

start_time=time.time()
list_of_num.sort()
print("It took %s seconds to identify the lowest number with sort." % (time.time()-start_time))
print("The lowest number is: %s" % list_of_num[0])