import turtle
import colorsys
import time

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Lighting Flower")

# Create turtle
pen = turtle.Turtle()
pen.speed(79)
pen.width(2)
pen.hideturtle()

# Function to draw the colorful flower
def draw_flower():
    hue = 0
    for i in range(100):
        # Convert HSV to RGB
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        pen.color(color)
        pen.circle(100)
        pen.left(360 / 10)
        hue += 0.01
        time.sleep(0.05)  # Simulate lighting effect

# Draw the flower
draw_flower()

# Keep window open
turtle.done()
