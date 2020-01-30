import random

def ss(number_list,n):
    found=False
    for i in number_list:
        if i==n:
            found=True
            break
    return found

#build random number list
def randomlist():
    rando = random.randint(1,100)
    num_list = []
    for i in range(1,rando+1):
        rand_sel=random.randint(1,100)
        while rand_sel in num_list:
            rand_sel = random.randint(1,100)
        num_list.append(rand_sel)
    return num_list
    
random_list=randomlist()
result=ss(random_list,37)
print(random_list)
print(result)