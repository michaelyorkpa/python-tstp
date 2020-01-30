def same(obj1,obj2):
    return obj1 is obj2

class Square:
    def __init__(self):
        pass

sq1=Square()
sq2=sq1
sq3=Square()

print(same(sq1,sq3))
