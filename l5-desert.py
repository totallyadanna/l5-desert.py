import turtle as t
import random

t.speed (0)
# sky

t.bgcolor ("#23B8FE")

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

# triangle

t.penup()
t.goto (-200,-100)
t.pendown()
t.color ("#7a4f04","#b3873d")
t.begin_fill()
for i in range (3):
    t.forward (200)
    t.left (120)
t.end_fill()
t.penup()
t.goto (-180,-70)
t.pendown()
t.forward (170)
t.penup()
t.goto (-180,-100)
t.forward (150)
t.pendown()
t.backward (150)
t.penup ()
t.goto (-162,-30)
t.pendown()
t.forward (120)
t.penup ()
t.goto (-145,0)
t.pendown()
t.forward (90)
t.penup ()
t.goto (-128, 30)
t.forward (60)

# sand of cacti

t.penup ()
t.goto (90, -100)
t.pendown ()
t.setheading(270)
t.color ("#7a4f04","#b3873d")
t.begin_fill ()

t.circle (45,-180)
t.end_fill ()




# cacti

t.penup ()
t.goto (115,-65)
t.pendown ()
t.color ("#1D3D1D", "#1FB01F")
t.begin_fill ()
t.forward (55)
t.seth (180)
t.circle (-20,180)
t.seth(90)
t.forward (20)
t.circle (-20,180)
t.forward (30)
t.seth(0)
t.circle (-15,180)
t.seth(270)
t.forward (50)
t.end_fill ()

t.mainloop ()
