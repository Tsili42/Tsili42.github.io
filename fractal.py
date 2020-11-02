import turtle, sys

def koch_curve(len, dep):

    if (dep == 0):
        turtle.forward(len)
    else:
        koch_curve(len, dep - 1)
        turtle.right(60)
        koch_curve(len, dep - 1)
        koch_curve(120, 0)
        koch_curve(len, dep - 1)
        turtle.right(60)
        koch_curve(len, dep - 1)

turtle.left(90)
turtle.backward(30)
koch_curve(int(sys.argv[1]), int(sys.argv[2]))
