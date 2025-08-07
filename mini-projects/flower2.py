import turtle
import math
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🌺 Ultimate Interactive Rotating Flower")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Color and animation settings
hue = 0.0
rotation = 0
speed = 2
zoom = 1.0

# Draw rotating and zooming flower with polar pattern
def draw_flower():
    global hue, rotation, zoom
    pen.clear()
    petal_count = 150
    base_radius = 160 * zoom

    for i in range(petal_count):
        angle_deg = i * (360 / petal_count) + rotation
        angle_rad = math.radians(angle_deg)
        r = base_radius * math.cos(6 * angle_rad)
        x = r * math.cos(angle_rad)
        y = r * math.sin(angle_rad)

        r_col, g_col, b_col = colorsys.hsv_to_rgb(hue % 1.0, 1, 1)
        pen.pencolor(r_col, g_col, b_col)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.goto(x, y)

        hue += 0.002

    rotation += speed
    screen.ontimer(draw_flower, 50)

# Controls

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed = max(1, speed - 1)

def zoom_in():
    global zoom
    zoom += 0.1

def zoom_out():
    global zoom
    zoom = max(0.5, zoom - 0.1)

def reset_flower():
    global hue, rotation, speed, zoom
    hue = 0
    rotation = 0
    speed = 2
    zoom = 1.0

def quit_program():
    turtle.bye()

# Bind keys
screen.listen()
screen.onkey(increase_speed, "Up")       # Speed up
screen.onkey(decrease_speed, "Down")     # Slow down
screen.onkey(zoom_in, "+")               # Zoom in
screen.onkey(zoom_out, "-")              # Zoom out
screen.onkey(reset_flower, "r")          # Reset
screen.onkey(quit_program, "q")          # Quit

# Start animation
draw_flower()
screen.mainloop()