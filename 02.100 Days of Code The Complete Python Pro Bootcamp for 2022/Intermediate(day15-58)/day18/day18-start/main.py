# from turtle import Turtle, Screen
import random
import turtle as t

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")



# write a square

# square = Turtle()
# for _ in range(4):
#     square.right(90)
#     square.forward(100)



# write a dotted line

# dot_line = Turtle()
# for _ in range(10):
#     dot_line.forward(10)
#     dot_line.pu()
#     dot_line.forward(10)
#     dot_line.pd()



# write triangle to decagon

# tim = Turtle()
# all_angle = 360
# color = ["black", "red", "blue", "green", "brown", "pink", "orange", "purple"]
#
#
# def draw_shape(number_sides):
#     for _ in range(number_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for num in range(3, 11):
#     angle = all_angle / num
#     tim.color(color[num - 3])
#     draw_shape(num)



# random walk
# rw = Turtle()
# color = ["black", "red", "blue", "green", "brown", "pink", "orange", "purple"]
# rw.pensize(15)
# rw.speed("fastest")
#
# for i in range(200):
#     mov = random.randrange(0, 270, 90)
#     rw.color(color[i % len(color)])
#     rw.setheading(mov)
#     rw.forward(30)



# Random Colors
# rc = t.Turtle()
# rc.pensize(15)
# rc.speed("fastest")
#
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# for i in range(200):
#     mov = random.randrange(0, 270, 90)
#     rc.pencolor(random_color())
#     rc.setheading(mov)
#     rc.forward(30)



# Spiral Circle
# sc = t.Turtle()
# sc.speed("fastest")
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# def draw_spirograph(size_of_gap):
#     for deg in range(0, 360, size_of_gap):
#         sc.pencolor(random_color())
#         sc.setheading(deg)
#         sc.circle(50)
#
# draw_spirograph(20)



#


screen = t.Screen()
screen.exitonclick()