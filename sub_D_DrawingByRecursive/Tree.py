import turtle as t

def tree(br):
    if br <= 5:
        return
    new = br * 0.7
    t.forward(br)
    t.right(20)
    tree(new)
    t.left(40)
    tree(new)
    t.right(20)
    t.backward(br)

t.speed(0)
t.left(90)
tree(70)
t.hideturtle()
t.done()