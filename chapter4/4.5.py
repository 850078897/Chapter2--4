import turtle
sn = turtle.Screen()
sn.bgcolor("lightgreen")
shell = turtle.Turtle()
shell.color("blue")
shell.pensize(3)
shell.speed(30)
def draw_spiral(sb,newbee):
    """
    draws on spiral
    """
    for i in range(75):
        sb = sb + 5
        shell.fd(sb)
        shell.right(91)
    
draw_spiral(5,10)
