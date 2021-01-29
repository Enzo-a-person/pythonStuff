import turtle
t = turtle.Turtle('turtle')
while True:
    m = input('movement')
    if m == 'w':
        t.forward(10)
    if m == 's':
        t.backward(10)
    if m == 'a':
        t.left(10)
    if m == 'd':
        t.right(10)
    if m == ' ':
        t.penup()
        
        
    