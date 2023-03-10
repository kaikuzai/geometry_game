class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def falls_within_rectangle(self, rectangle):
        if (rectangle.lowleft[0] < self.x < rectangle.upright[0] and rectangle.lowleft[1] < self.y < rectangle.upright[1]):
            return True
        else:
            return False

    def distance_from_point(self, point):
        return((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft 
        self.upright = upright


point_one = Point(3,3)
rectangle_one = Rectangle(Point(1,1), Point(10,10))

print(point_one.falls_within_rectangle(rectangle_one))







