import turtle
import random


turtle.hideturtle()
turtle.home()


count = 2

dictionary = ["☀","♪","☼","Δ","☽","◎","&","*","∞","░"]


turtle.penup()
while count > 0:
	dotsize = random.randint(50,150)
	turtle.pensize(dotsize)
	turtle.colormode(255)
	# col1 = random.randint(100,245)
	col2 = random.randint(100,200)
	col3 = random.randint(1,100)
	col1 = random.randint(10,50)
	# col2 = random.randint(50,100)
	# col3 = random.randint(100,150)
	color = [col1,col2,col3]
	x = random.randint(-200,200)
	y = random.randint(-200,200)
	# turtle.pendown()
	turtle.color(color)
	coord = (x,y)
	turtle.setpos(x,y)

	if dotsize < 10 or dotsize > 30:
		dot = turtle.dot(dotsize,color)
		turtle.pensize((dotsize/2))
		turtle.setpos(x+dotsize,y+dotsize)
		turtle.pendown()
		turtle.pensize((dotsize/2))
		turtle.setpos(x+dotsize,y-dotsize)
		turtle.pensize((dotsize/2))
		turtle.setpos(x-dotsize,y-dotsize)
		turtle.pensize((dotsize/2))
		turtle.setpos(x-dotsize,y+dotsize)
		turtle.setpos(x+dotsize,y+dotsize)
		turtle.penup()


	gorked = random.randint(0,50)
	ran = random.randint(0,3)
	gorkx = random.randint(0,100)
	gorky = random.randint(0,100)


	if ran == 1:
		turtle.setpos(x-gorkx,y-gorky)

	elif ran == 2:
		turtle.setpos(x+gorkx,y-gorky)

	elif ran ==3:
		turtle.setpos(x-gorkx,y+gorky)

	else:	
		turtle.setpos(x+gorkx,y+gorky)

	color = (col1+50,col2+50,col3+50)
	dotsize = random.randint(10,100)
	dot =turtle.dot(dotsize,color)

	if dotsize > 10 or dotsize < 30:
		turtle.pencolor(color)
		turtle.begin_fill()
		turtle.fillcolor(color)
		turtle.pensize((dotsize/2))
		turtle.setpos(gorkx+dotsize,gorky+dotsize)
		turtle.pendown()
		turtle.pensize((dotsize/2))
		turtle.setpos(gorkx+dotsize,gorky-dotsize)
		turtle.pensize((dotsize/2))
		turtle.setpos(gorkx-dotsize,gorky-dotsize)
		turtle.pensize((dotsize/2))
		turtle.setpos(gorkx-dotsize,gorky+dotsize)
		turtle.setpos(gorkx+dotsize,gorky+dotsize)
		turtle.penup()
		turtle.end_fill()


	count -=1
	

x2=random.randint(-200,200)
y2=random.randint(-200,200)
turtle.setpos(x2,y2)
number = random.randint(0,9)
symbol = dictionary[random.randint(0,9)]
fontsize = random.randint(100,200)
scale = random.randint(0,200)
turtle.bgcolor(scale,scale,scale)


if col1 < 240:
	col1+=15
elif col1 < 15 and col1 > 0:
	col1+=15
if col2 < 240:
	col2+=15
elif col2 < 15 and col2 > 0:
	col2+=15
if col3 < 240:
	col3+=15
else:
	col1 = random.randint(10,245)
	col2 = random.randint(10,245)
	col3 = random.randint(10,245)
	color = [col1,col2,col3]
turtle.color(col1-10,col2-10,col3-10)
# turtle.write(symbol,False,"center",("Helvetica",fontsize,'bold'))


turtle.penup()
turtle.setpos(random.randint(-50,50),random.randint(-200,200))
num = random.randint(0,20)
if num != 20:
	fonts = ['Apple Chancery','Arial','Comic Sans','Courier New','Futura','Georgia','Helvetica','Times New Roman','Trebuchet','Veranda']
	num = random.randint(0,2)
	style = ['bold','italic',['bold','italic']]
	num2 = random.randint(0,9)
	turtle.color("white")
	textx = random.randint(1,110)
	texty = random.randint(1,110)

	hope = ["hope you","one step","you can","you're on","rest","take","find","forge","see","until"]
	great = ["have","at","change","the","a","","your","a","you","we meet"]
	rest = ["a great day","a time","your life","right track","minute","care","opportunity","path","later","again"]

	phrase = random.randint(0,9)
	phrase2 = random.randint(0,9)
	phrase3 = random.randint(0,9)

	# hope[phrase]=hope[phrase].replace(hope[phrase],dictionary[phrase]*len(hope[phrase]))
	# great[phrase]=great[phrase].replace(great[phrase],dictionary[phrase]*len(great[phrase]))
	# rest[phrase]=great[phrase].replace(great[phrase],dictionary[phrase]*len(great[phrase]))

	font = fonts[num2]
	one = turtle.setpos(random.randint(-80,100),random.randint(30,200))
	turtle.color("white")
	turtle.write(hope[phrase],False,"center",(font,random.randint(50,76),style[num]))
	two=turtle.setpos(random.randint(-100,100),random.randint(-50,-1))
	turtle.color("white")
	turtle.write(great[phrase],False,"center",(font,random.randint(50,76),style[num]))
	three=turtle.setpos(random.randint(-50,50),random.randint(-200,-90))
	turtle.write(rest[phrase],False,"center",(font,random.randint(50,76),style[num]))
	turtle.color("white")

turtle.mainloop()