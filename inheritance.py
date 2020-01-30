class Shape():
   
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass
    def __init__(self,w,l):
        self.width=w
        self.length=l

    def calculate_perimeter(self):
        return 2*(self.width+self.length)

class Square(Shape):
    def __init__(self,s1):
        self.s1=s1

    def calculate_perimeter(self):
        return self.s1*4

    def change_size(self,new_size):
        new_size += self.s1

square_obj=Square(5)
rect_obj=Rectangle(20,10)

square_obj.what_am_i()
rect_obj.what_am_i()
