import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.
pen = turtle.Turtle()
pen.color('white')


# Move the turtle to the starting point.
pen.penup()
pen.setposition(-55,-80)
pen.pendown()
turtle.hideturtle()

# Draw the octagon.
turtle.bgcolor('red')
pen.color('white')
for x in range(8):
    pen.forward(100)
    pen.left(45)
# Display 'STOP'
word_font = ('Arial', 80, 'bold')
turtle.write('STOP', font = word_font, align = 'center')
pen.pencolor('white')
turtle.done()
