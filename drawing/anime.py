"""
Source: https://github.com/Harshit-Hackerxguy/Harshit-Hackerxguy/blob/main/goku2.py
"""

import turtle

a  = turtle.Turtle()
a.speed(3)
a.color("black","#FFD7C1")
a.penup()
a.goto(-282.50,-160.14)
a.pendown()
a.begin_fill()
a.rt(85)
a.fd(30)
a.left(45)
a.bk(40)
a.fd(70)
a.lt(35)
a.back(110)
a.fd(110)
a.circle(-30,extent=50)
a.forward(50)
a.rt(140)
a.circle(-800,extent=15)
xx=a.pos()
a.goto(-385,50)
a.end_fill()
a.hideturtle()


b = turtle.Turtle()
b.speed(1)
b.color("black","#FFD7C1")
b.penup()
b.goto(-205,-85)
b.pendown()
b.begin_fill()
b.lt(50)
b.fd(10)
b.lt(45)
b.fd(85)
z = b.pos()
b.penup()
b.goto(-205,-85)
b.pendown()
b.rt(145)
b.fd(30)
b.right(110)
b.fd(20)
b.lt(60)
b.forward(10)
b.right(45)
b.forward(10)
x=b.pos()
b.rt(45)
b.fd(20)
b.lt(25)
b.fd(10)
b.penup()
b.goto(x)
b.pendown()
b.left(45)
b.fd(10)
b.rt(45)
b.fd(10)
b.back(5)
b.lt(45)
b.fd(35)
for i in range(5):
    b.rt(17)
    b.fd(3)
b.fd(30)
n = b.pos()
b.fd(70)
b.rt(70)
b.fd(40)
y=b.pos()
b.fd(100)
b.goto(z)
b.end_fill()
b.hideturtle()


c = turtle.Turtle()
c.speed(1)
c.penup()
c.goto(-385,50)
start=c.pos()
c.pendown()
c.begin_fill()
c.lt(45)
c.circle(-100,extent=30)
c.lt(65)
c.circle(-200,extent=45)
c.rt(160)
c.circle(200,extent=35)
c.lt(135)
c.forward(50)
c.rt(20)
c.circle(-200,extent=45)
c.right(135)
c.circle(200,extent=25)
c.left(145)
c.circle(-120,extent=75)
c.rt(135)
c.circle(300,extent=15)
c.lt(145)
c.fd(30)
c.circle(-150,extent=30)
c.rt(135)
c.circle(300,extent=25)
c.lt(90)
c.circle(-60,extent=50)
c.rt(130)
c.circle(100,extent=45)
c.left(130)
c.circle(-60,extent=50)
c.rt(130)
c.circle(100,extent=35)
c.lt(100)
c.circle(60,extent=50)
c.rt(135)
c.circle(-60,extent=30)
c.lt(120)
c.forward(155)
c.goto(start)
c.end_fill()
c.hideturtle()


d=turtle.Turtle()
d.speed(6)
d.color("black","#FFD7C1")
d.penup()
d.goto(y)
d.pendown()
d.begin_fill()
d.right(90)
for i in range(5):
    d.rt(27)
    d.fd(2)
d.forward(25)
d.rt(70)
d.circle(-200,extent=10)
d.color("#FFD7C1","#FFD7C1")
d.rt(110)
d.forward(30)
d.goto(y)
d.end_fill()
d.hideturtle()


e = turtle.Turtle()
e.speed(4)
e.color("black")
e.penup()
e.goto(-206.27,-262.95)
e.pendown()
e.begin_fill()
e.right(35)
e.circle(-100,extent=40)
e.rt(110)
e.fd(250)
e.goto(xx)
e.end_fill()
e.hideturtle()


f = turtle.Turtle()
f.speed(6)
f.color("#F85B1A")
f.penup()
f.goto(xx)
f.pendown()
f.begin_fill()
f.rt(50)
f.circle(400,extent=40)
f.left(10)
f.back(250)
f.goto(xx)
f.end_fill()

g = turtle.Turtle()
g.speed(1)
g.penup()
g.goto(-210,-75)
g.pendown()
g.right(125)
g.forward(5)
e = g.pos()
g.rt(90)
g.begin_fill()
g.fd(60)
g.lt(70)
g.fd(10)
g.lt(115)
g.fd(17)
e1 = g.pos()
g.fd(40)
g.goto(e)
g.end_fill()
g.goto(e1)
g.color("black","white")
g.begin_fill()
g.rt(70)
g.fd(17)
g.lt(85)
g.fd(37)
g.end_fill()
g.begin_fill()
g.color("black")
g.circle(5)
g.end_fill()
g.hideturtle()



h = turtle.Turtle()
h.speed(1)
h.penup()
h.goto((189.15,-42.93))
h.pendown()
h.begin_fill()
h.lt(105)
h.fd(80)
h.left(25)
h.back(20)
h.rt(50)
h.fd(30)
h.rt(25)
h.fd(100)
h.lt(35)
h.back(40)
h.rt(35)
h.circle(-200,extent=30)
h.lt(45)
h.back(35)
h.rt(25)
h.circle(-100,extent=20)
h.circle(100,extent=30)
h.left(35)
h.back(310)
h.lt(90)
h.fd(100)
h.goto((189.15,-42.93))
h.end_fill()
h.hideturtle()



i = turtle.Turtle()
i.speed(2)
i.color("black","#FFE1CD")
i.penup()
i.goto(243.28,-169.45)
i.pendown()
i.begin_fill()
i.rt(85)
i.fd(30)
i.rt(45)
i.bk(40)
i.fd(70)
t = i.pos()
i.lt(130)
i.circle(300,extent=32)
i.lt(90)
end = i.pos()
i.circle(300,extent=30)
i.goto(243.28,-169.45)
i.end_fill()
i.hideturtle()



j = turtle.Turtle()
j.speed(1)
j.color("black","#FFE1CD")
j.penup()
j.goto(180,-85)
j.pendown()
j.begin_fill()
j.rt(140)
j.fd(30)
j.lt(110)
j.fd(20)
j.rt(60)
j.forward(7)
j.lt(45)
j.fd(10)
v = j.pos()
j.lt(55)
j.fd(20)
j.lt(25)
j.fd(10)
j.penup()
j.goto(v)
j.pendown()
j.rt(105)
j.fd(10)
j.lt(45)
j.fd(10)
j.back(5)
j.rt(45)
j.fd(35)
j.speed(0)
for i in range(5):
    j.lt(17)
    j.fd(3)
j.fd(30)
g = j.pos()
j.fd(70)
j.lt(70)
j.fd(40)
j.rt(150)
j.circle(5,extent=110)
j.fd(30)
j.lt(70)
j.circle(200,extent=7)
j.circle(10,extent=100)
j.fd(25)
j.rt(100)
j.fd(30)
j.rt(145)
j.fd(10)
j.circle(5,extent=140)
j.forward(70)
j.circle(20,extent=65)
j.fd(5)
j.circle(45,extent=65)
j.fd(35)
j.fd(35)
j.goto(180,-85)
j.end_fill()
j.hideturtle()



k = turtle.Turtle()
k.speed(6)
k.color("black")
k.penup()
k.goto(t)
k.pendown()
k.begin_fill()
k.rt(160)
k.circle(20,extent=40)
k.fd(110)
k.lt(120)
k.fd(250)
k.goto(end)
k.end_fill()
k.hideturtle()

l= turtle.Turtle()
l.speed(6)
l.color("#F3A903")
l.penup()
l.goto(end)
l.pendown()
l.begin_fill()
l.rt(180)
l.circle(120,extent=75)
l.lt(100)
l.fd(50)
s = l.pos()
l.lt(100)
l.circle(-70,extent=95)
l.goto(end)
l.end_fill()
l.penup()
l.goto(s)
l.pendown()
l.color("black","#707070")
l.pensize(2)
l.begin_fill()
l.rt(182)
l.fd(70)
l.circle(10,extent=90)
l.fd(5)
l.rt(90)
l.fd(50)
l.circle(18,extent=70)
l.fd(35)
l.lt(110)
l.fd(250)
l.lt(90)
l.fd(63)
l.goto(s)
l.end_fill()
l.hideturtle()



m = turtle.Turtle()
m.speed(1)
m.penup()
m.goto(185,-75)
m.pendown()
m.right(35)
m.forward(5)
e2 = m.pos()
m.lt(70)
m.begin_fill()
m.fd(60)
m.rt(70)
m.fd(10)
m.rt(115)
m.fd(17)
e3 = m.pos()
m.fd(40)
m.goto(e2)
m.end_fill()
m.goto(e3)
m.color("black","white")
m.begin_fill()
m.lt(70)
m.fd(17)
m.rt(85)
m.fd(37)
m.end_fill()
m.begin_fill()
m.color("black")
m.circle(-5)
m.end_fill()
m.hideturtle()



t=turtle.Turtle()
t.speed(3)
t.penup()
t.goto(-380,330)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(762)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()
t.hideturtle()

n = turtle.Turtle()
n.speed(1)
n.penup()
n.goto(-170,240)
n.pendown()
n.color("yellow")
style = ('Impact',40,'bold')
n.write("DRAG   N",font=style)
n.penup()
n.goto(8,240)
n.pendown()
n.color("red")
n.write("BALL",font=style)
n.penup()
n.goto(130,240)
n.speed(2)
n.pendown()
n.begin_fill()
n.lt(45)
n.fd(70)
n.rt(45)
n.bk(30)
n.lt(50)
n.bk(25)
n.left(25)
n.fd(40)
n.rt(75)
n.fd(80)
n.lt(45)
n.bk(70)
n.rt(45)
n.fd(30)
n.left(50)
n.fd(25)
n.lt(25)
n.bk(40)
n.goto(130,240)
n.end_fill()
n.hideturtle()


o = turtle.Turtle()
o.speed(2)
o.penup()
o.goto(-40,250)
o.pendown()
o.color("flax","flax")
o.begin_fill()
o.circle(20)
o.end_fill()
o.goto(-50,275)
o.color("red","red")
o.speed(2)
o.begin_fill()
for i in range(5):
    o.forward(20)
    o.rt(144)
o.end_fill()
o.hideturtle()


turtle.mainloop()
