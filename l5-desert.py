import turtle as t
import random

t.speed (0)

#sand-box
t.penup ()
t.goto (-300,-100)
t.pendown ()
t.color ("#b3873d")
t.begin_fill ()
for x in range (2) :
    t.forward (600)
    t.right (90)
    t.forward (200)
    t.right (90)
t.end_fill ()

#sand particles

for x in range (30) :
    t.penup ()
    x = random.randint (-300,300)
    y = random.randint (-300,-100)
    t.goto (x,y)
    t.pendown ()
    t.color ("#7a4f04")
    t.dot ()

# hold the turtle screen
t.mainloop ()