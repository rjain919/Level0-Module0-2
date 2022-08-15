import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))

    Teal.penup()

    Teal.goto(42, 31)
    
    # 6. Call the turtle .penup() method
    
    # 7. Move the turtle to a new location using .goto(x, y)


def turtle_clicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
        
        # 9. Make the turtle spin 360 degrees using the .right() method
        
        # 10. Use the .color() method and getRandomColor() function to change
        # the color of the turtle,
        # myTurtle.color(get_random_color())


if __name__ == '__main__':
    window = Turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)


    Teal = turtle.Turtle

    Teal.shape('turtle')

    Teal.color('Green')
    Teal.pencolor('Blue')

    Teal.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

    Teal.oneclick(turtle_clicked)



# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done()
