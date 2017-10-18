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
    for i in range(80):
        sb = sb + 5
        shell.fd(sb)
        shell.right(90)
    
draw_spiral(5,10)
