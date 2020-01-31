numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,11,12,12,13,13,14,14,15,15]
count = {}
for i in numbers:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

for key, value in count.items():
    if value == 1:
        print(key)