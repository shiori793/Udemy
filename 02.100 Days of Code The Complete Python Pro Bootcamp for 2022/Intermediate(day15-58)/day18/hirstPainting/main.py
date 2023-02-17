import colorgram
import turtle as t
import random

t.colormode(255)

rgb_colors = []
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r < 240 or b < 240 or b < 240:
        rgb_colors.append((r, g, b))

def draw_hirst_painting():
    dot = t.Turtle()
    dot.pu()
    dot.hideturtle()
    dot.setpos(-200, -200)
    for _ in range(10):
        for _ in range(10):
            dot.dot(20, random.choice(rgb_colors))
            dot.forward(40)
        dot.setpos(-200, dot.ycor() + 40)

draw_hirst_painting()

screen = t.Screen()
screen.exitonclick()