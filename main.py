from random import randint
import turtle

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def falls_within_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


    #def distance_from_point(self, point):
    #    return((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1 
        self.point2 = point2

    def area_of_rectangle(self):
        length = self.point2.y - self.point1.y
        width = self.point2.x - self.point1.y 
        return length * width

class GraphRectangle(Rectangle):

    def draw(self, canvas):

        # deactivate pen
        canvas.penup()

        # navigate to coordinates
        canvas.goto(self.point1.x, self.point1.y)

        # activate pen
        canvas.pendown()

        # draw shape
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)




class GraphPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        # deactivate pen
        canvas.penup()

        # navigate to point
        canvas.goto(self.x, self.y)

        # activate pen
        canvas.pendown()

        # submit dot
        canvas.dot(size, color)

        # end turtle
        turtle.done()

graph_rectangle = GraphRectangle(Point(randint(0,100), randint(0, 100)), Point(randint(101, 200),randint(101, 200)))

print(f"The dimensions of the rectangle are ({graph_rectangle.point1.x}, {graph_rectangle.point1.y}) for the lower left point and ({graph_rectangle.point2.x} and {graph_rectangle.point2.y}) for the upper right point")

guessed_point = GraphPoint(int(input("Choose your x cordinate: ")), int(input("Choose your y coordinate: ")))

print(f"Your point falls within the rectangle: {guessed_point.falls_within_rectangle(graph_rectangle)}")

guessed_area = int(input("What do you think the area is of the rectangle?: "))

print(f"You were off by {int(graph_rectangle.area_of_rectangle() - guessed_area)}, the actual area is {graph_rectangle.area_of_rectangle()}")

myturtle = turtle.Turtle()
graph_rectangle.draw(canvas=myturtle)
guessed_point.draw(canvas=myturtle)


