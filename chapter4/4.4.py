import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(3)

def make_pattern(turt,size):
    for i in range(16):
        tess.left(360/16)
        for i in range(4):
            turt.forward(size)
            turt.lt(90)
       
        
make_pattern(tess,100)
        
                 
