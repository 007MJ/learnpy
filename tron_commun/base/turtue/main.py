import turtle

def stare(n, size=30):
    for i in range(0, n):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
        i +=1
    t.forward(30)

t = turtle.Turtle()
stare(2)
turtle.done()