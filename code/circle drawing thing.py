#circle drawer
import turtle
t = turtle.Turtle('turtle')
rotation = int(input("rotation: ")) #input questions 
movement = int(input("move: "))
time = int(input("time: "))
color = input('what color do you want?:')

t.color(color)

for _ in range(time):     #the loop for drawing the circle
    t.forward(movement)
    t.left(rotation)
#everything below here prints a finshed message
message = "Finished"
t.penup()
t.goto(0, 150)
t.color('black')
t.write(message, font=("Arial", 20, "normal"))
print ("goodbye")
turtle.done()


