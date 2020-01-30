class Square:
    def __init__(self,s1):
        self.s1=s1
    def calculate_perimeter(self):
        return sef.s1*4
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)

square_obj=Square(5)
print(square_obj)
