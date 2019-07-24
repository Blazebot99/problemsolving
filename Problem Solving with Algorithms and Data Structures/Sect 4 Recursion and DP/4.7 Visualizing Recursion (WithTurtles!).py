import turtle

def tree(branchLen,t):
    import random
    rng=random.Random()
    if branchLen > 5:
        ang=rng.randrange(10,30)
        t.forward(branchLen)
        t.right(ang)
        ang=rng.randrange(30,50)
        cut=rng.randrange(10, 20)
        tree(branchLen-cut,t)
        t.left(ang)
        ang=rng.randrange(10,30)
        cut=rng.randrange(5, 15)
        tree(branchLen-cut,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()

