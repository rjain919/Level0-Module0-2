import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Teal = turtle.Turtle()

    Teal.shape('turtle')

    Teal.speed(2)

    Teal.color('green')

    Teal.pencolor('blue')

    Teal.forward(100)

    Teal.left(90)

    Teal.right(90)

    Teal.begin_fill()
    for i in range(4):
        Teal.forward(100)
        Teal.right(90)

    Teal.goto(0, 0)

    Teal.circle(50, steps=30)
    Teal.end_fill()



    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
