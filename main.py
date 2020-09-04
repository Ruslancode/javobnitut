import turtle
import random
from tkinter import messagebox

ascore = 0
bscore = 0

window = turtle.Screen()
window.title("Javobni tut")

q = []
a = ["javob11","javob21"]
b = ["javob12","javob22"]
lor = random.randint(0,len(q)-1)
colors = ["red","orange","yellow","green","blue","indigo","violet"]

question = turtle.Turtle()
question.ht()
question.left(90)
question.penup()
question.fd(250)
question.write(q[lor])

aturtle = turtle.Turtle()
aturtle.ht()
aturtle.shape("turtle")
aturtle.color(random.choice(colors))
aturtle.penup()
aturtle.left(180)
aturtle.fd(100)
aturtle.right(90)
aturtle.st()
aturtle.pendown()

bturtle = turtle.Turtle()
bturtle.ht()
bturtle.shape("turtle")
bturtle.color(random.choice(colors))
bturtle.penup()
bturtle.fd(100)
bturtle.left(90)
bturtle.st()
bturtle.pendown()

vara = turtle.Turtle()
vara.color("red")
vara.penup()

varb = turtle.Turtle()
varb.color("blue")
varb.penup()
def chd():
    posxa = 1
    while True:
        posxa = random.randint(-600,600)
        if posxa % 10 == 0:
            if posxa != -100:
                if posxa != 100:
                    break
    posya = 1
    while True:
        posya = random.randint(-300,300)
        if posya % 10 == 0:
            break
    vara.goto(posxa,posya)

    posxb = 1
    while True:
        posxb = random.randint(-600,600)
        if posxb % 10 == 0:
            if posxb != -100:
                if posxb != 100:
                    if posxb != posxa:
                        break
    posyb = 1
    while True:
        posyb = random.randint(-384,384)
        if posyb % 10 == 0:
            if posyb != posya:
                break
    varb.goto(posxb,posyb)
    emi = random.randint(1,2)

emi = random.randint(1,2)
chd()

ansa = turtle.Turtle()
ansa.color("red")
ansa.ht()
ansa.left(90)
ansa.penup()
ansa.fd(250)
ansa.lt(90)
ansa.fd(300)
if emi == 1:
    ansa.write(a[lor])
else:
    ansa.write(b[lor])

ansb = turtle.Turtle()
ansb.color("blue")
ansb.ht()
ansb.left(90)
ansb.penup()
ansb.fd(250)
ansb.rt(90)
ansb.fd(300)
if emi == 2:
    ansb.write(a[lor])
else:
    ansb.write(b[lor])

def gofd():
    aturtle.fd(10)
    if emi == 1:
        if aturtle.pos() == vara.pos():
           chd()
           if emi == 1:
               ascore+=1
        if aturtle.pos() == varb.pos():
           chd()
           if emi == 2:
               ascore+=1
    if ascore == 5:
        messagebox.showinfo("O'yin tugadi", "1-o'yinchi yutti")
          
def gobk():
    global ascore
    aturtle.bk(10)
    if aturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            ascore+=1
        if aturtle.pos() == varb.pos():
            chd()
        if emi == 2:
            ascore+=1
    if ascore == 5:
        messagebox.showinfo("O'yin tugadi", "1-o'yinchi yutti")
def golt():
    global ascore
    aturtle.lt(90)
    if aturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            ascore+=1
        if aturtle.pos() == varb.pos():
            chd()
        if emi == 2:
            ascore+=1
    if ascore == 5:
        messagebox.showinfo("O'yin tugadi", "1-o'yinchi yutti")
def gort():
    global ascore
    aturtle.rt(90)
    if aturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            ascore+=1
        if aturtle.pos() == varb.pos():
            chd()
        if emi == 2:
            ascore+=1
    if ascore == 5:
        messagebox.showinfo("O'yin tugadi", "1-o'yinchi yutti")

def goofd():
    global bscore
    bturtle.fd(10)
    if bturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            bscore+=1
    if bturtle.pos() == varb.pos():
        chd()
        if emi == 2:
            bscore+=1
    if bscore == 5:
        messagebox.showinfo("O'yin tugadi", "2-o'yinchi yutti")
def goobk():
    global bscore
    bturtle.bk(10)
    if bturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            bscore+=1
    if bturtle.pos() == varb.pos():
        chd()
        if emi == 2:
            bscore+=1
    if bscore == 5:
        messagebox.showinfo("O'yin tugadi", "2-o'yinchi yutti")
def goolt():
    global bscore
    bturtle.lt(90)
    if bturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            bscore+=1
    if bturtle.pos() == varb.pos():
        chd()
        if emi == 2:
            bscore+=1
    if bscore == 5:
        messagebox.showinfo("O'yin tugadi", "2-o'yinchi yutti")
def goort():
    global bscore
    bturtle.rt(90)
    if bturtle.pos() == vara.pos():
        chd()
        if emi == 1:
            bscore+=1
    if bturtle.pos() == varb.pos():
        chd()
        if emi == 2:
            bscore+=1
    if bscore == 5:
        messagebox.showinfo("O'yin tugadi", "2-o'yinchi yutti")

window.onkey(gofd, "w")
window.onkey(gobk, "s")
window.onkey(golt, "a")
window.onkey(gort, "d")
window.onkey(goofd, "Up")
window.onkey(goobk, "Down")
window.onkey(goolt, "Left")
window.onkey(goort, "Right")
window.listen()

window.mainloop()
