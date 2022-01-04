import turtle
import random
import numpy as np

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Vector Norms")
wn.setup(600,700)





tt = turtle.Turtle()
tt.color("white")
tt.shape("square")
tt.shapesize(0.1)
style = ('Courier', 20, 'italic')
tt.write('Press "P" to randomly select ball!', font=style, align='center')
wn.tracer(0)

is_paused = False
balls = []


for _ in range(8):
	balls.append(turtle.Turtle())
def color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

	return (r,g,b)


for ball in balls:
	ball.shape("circle")
	ball.shapesize(2)
	ball.screen.colormode(255)
	ball.color(color())
	ball.penup()
	ball.speed(0)
	x = random.randint(-290,290)
	y = random.randint(-300,300)
	ball.goto(x,y)
	ball.dy = random.randint(-3,3)
	ball.dx = random.randint(-5,5)
	ball.da = random.randint(-2,2)

gravity = 0.1 
def toggle_pause():
	global is_paused
	if is_paused:
		is_paused = False
		for txt in txts:
			txt[0].clear()
			txt[0].color("black")
			txt[0].hideturtle()
	else:
		is_paused = True
		select()

txts = []

def select():
	temp = 0
	for ball in balls:
		if ball.shapesize()[0] == 4.5:
			temp = balls.index(ball)
			ball.shapesize(2)
	n = random.randint(0,8)
	if n != temp:
		balls[n].shapesize(4.5)
		selected = np.array(balls[n].color()[0])
	ls = sorted(balls,key = lambda a:np.linalg.norm(selected - np.array(a.color()[0])))
	for ball in balls:
		txt = turtle.Turtle()
		txt.color("white")
		txt.goto(ball.xcor()+4,ball.ycor()+15)
		txts.append([txt,str(ls.index(ball))])
	for txt in txts:
		txt[0].write(txt[1], font=("Arial", 20, "normal"))
	print(len(balls))


wn.listen()
wn.onkeypress(toggle_pause,"p")


while True:
	if not is_paused:
		for ball in balls:
			wn.update()
			ball.rt(ball.da)
			ball.dy -= gravity
			ball.sety(ball.ycor() + ball.dy)
			ball.setx(ball.xcor() + ball.dx)

			if ball.ycor() >  345 or ball.ycor() < -345:
				if ball.ycor() < -345:
					ball.sety(-340)
				ball.dy *=-1
				ball.da *= -1

			if ball.xcor() > 290 or ball.xcor() < -290:
				if ball.xcor() < -290:
					ball.setx(-290)
				ball.dx *= -1
				ball.da *= -1
		for i in range(0,8):
			for j in range(i+1,8):
				if balls[i].distance(balls[j]) < 30:
					balls[i].dx,balls[j].dx = balls[j].dx,balls[i].dx
					balls[i].dy,balls[j].dy = balls[j].dy,balls[i].dy
	else:
		wn.update()

wn.mainloop()


