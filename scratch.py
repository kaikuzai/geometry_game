import turtle 

# Create a canvas instant
myturtle = turtle.Turtle()

# deactivate pen
myturtle.penup()


#Navigate to coordinate
myturtle.goto(54, 75)

# activate pen
myturtle.pendown()

# Move turtle to create a rectangle
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()


