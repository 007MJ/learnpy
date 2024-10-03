import turtle


def carre(size):
    for i in range(0, 4):
         t.forward(size)
         t.left(90)

    
def carreN(size, nb):
    if nb == 0:
        nb =1
    for i in range(0, nb):
        n_size = size * (i + 1)
        carre(n_size)


def stare(n, size=30):
    for i in range(0, n):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
        i +=1
        size +=10
    t.forward(size)

t = turtle.Turtle()
# stare(2)

carreN(50, 3)
turtle.done()