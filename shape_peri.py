class Rectangle():
    def __init__(self,w,l):
        self.width=w
        self.length=l

    def calculate_perimeter(self):
        return 2*(self.width+self.length)

class Square():
    def __init__(self,s1):
        self.s1=s1

    def calculate_perimeter(self):
        return self.s1*4

    def change_size(self,new_size):
        self.s1+=new_size
