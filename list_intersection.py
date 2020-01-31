def intersection(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3

this_week = [2,43,48,62,64,28,3]
most_comm = [1,28,42,70,2,10,62,31,4,14]
print(intersection(this_week,most_comm))

def return_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

new_list = return_intersection(this_week,most_comm)
print(new_list)