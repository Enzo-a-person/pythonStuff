#walk around by Enzo


#imporing things
import turtle
t = turtle.Turtle('turtle')
from tkinter import *
from tkinter import ttk
import random
#this command will make sure the turtle will start facing up, and make it blue, because blue is my favorite color.
t.color('blue','blue')
t.left(90)


# define stuffz
def mvforward():
  t.forward(10)
def mvbackward():
  t.backward(10)
def turnright():
  t.left(10)
def turnleft():
  t.right(10)
def quit():
  exit()

def cls():
  t.clear()

def cool():
  test = 0
  while (test < 100):
    t.forward(10)
    t.left(1)
    test = test + 1
#def letsgo():
  #xint = int(x)
  #yint = int(y)
  #t.goto(xint,yint)



#configuring tkinter
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

#def goto():
 # x = "x"
 # y = "y"
 # print("hello")
 # goto = Tk()
 # gotofrm = ttk.Frame(goto, padding=10)
 # gotofrm.grid()
 # goto.title('where do you want to go today?')
 # ttk.Button(gotofrm, text="GO!", command=letsgo).grid(column=3, row=1)
 # ttk.Entry(gotofrm, textvariable=x).grid(column=1, row=1)
 # ttk.Entry(gotofrm, textvariable=y).grid(column=2, row=1)
 # goto.mainloop()
#about window
def AboutSpawning():
  about = Tk()
  aboutfrm = ttk.Frame(about, padding=10)
  aboutfrm.grid()
  about.title('moving turtle thing')
  ttk.Label(aboutfrm, text="Moving turtle program").grid(column=1, row=0)
  ttk.Label(aboutfrm, text="").grid(column=1, row=1)
  ttk.Label(aboutfrm, text="Writen by Enzo").grid(column=1, row=2)
  ttk.Button(aboutfrm, text="Ok", command=about.destroy).grid(column=0, row=3)
  ttk.Button(aboutfrm, text="Cool", command=cool).grid(column=2, row=3)

  about.mainloop()


#controller window
root.title('Controller')
ttk.Label(frm, text="click the buttons to move the turtle").grid(column=1, row=5)
ttk.Button(frm, text="Quit", command=quit).grid(column=2, row=6)
ttk.Button(frm, text="forwards", command=mvforward).grid(column=1, row=0)
ttk.Button(frm, text="backwards", command=mvbackward).grid(column=1, row=3)
ttk.Button(frm, text="turn left", command=turnleft).grid(column=2, row=1)
ttk.Button(frm, text="turn right", command=turnright).grid(column=0, row=1)
ttk.Button(frm, text="Clear", command=cls).grid(column=1, row=6)
ttk.Button(frm, text="About", command=AboutSpawning).grid(column=0, row=6)
#ttk.Button(frm, text="goto", command=goto).grid(column=0, row=7)
root.option_add('*tearOff', FALSE)
#testing out a file menu lol (didn't work out in the end lol)
menubar = Menu(root)
root['menu'] = menubar

root.mainloop()
