from random import randint

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def falls_within_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


    #def distance_from_point(self, point):
    #    return((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft 
        self.upright = upright


rand_rectangle = Rectangle(Point(randint(0,9), randint(0, 9)), Point(randint(10, 19),randint(10, 19)))

print(f"The dimensions of the rectangle are ({rand_rectangle.lowleft.x}, {rand_rectangle.lowleft.y}) for the lower left point and ({rand_rectangle.upright.x} and {rand_rectangle.upright.y}) for the upper right point")

guessed_point = Point(int(input("Choose your x cordinate: ")), int(input("Choose your y coordinate: ")))

print(f"Your point falls within the rectangle: {guessed_point.falls_within_rectangle(rand_rectangle)}")
