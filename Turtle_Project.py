from tkinter import *
import turtle
from matplotlib import pyplot as plt
   
def click():
    #corona virus

        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor('black')

        t.pencolor('green')
        t.speed(5)
        t.penup()
        t.goto(0,200)
        t.pendown()

        #driver code
        a=0
        n=0

        while True:
            t.forward(a)
            t.right(n)
            a+=3
            n+=1

            if n==210:
                break
            t.hideturtle()

        turtle.done() 

def click1():

# DDA Function for line generation

	def DDA(x0, y0, x1, y1):

		# find absolute differences
		dx = abs(x0 - x1)
		dy = abs(y0 - y1)

		# find maximum difference
		steps = max(dx, dy)

		# calculate the increment in x and y
		xinc = dx/steps
		yinc = dy/steps

		# start with 1st point
		x = float(x0)
		y = float(y0)

		# make a list for coordinates
		x_coorinates = []
		y_coorinates = []

		for i in range(steps):
			# append the x,y coordinates in respective list
			x_coorinates.append(x)
			y_coorinates.append(y)

			# increment the values
			x = x + xinc
			y = y + yinc

		# plot the line with coordinates list
		plt.plot(x_coorinates, y_coorinates, marker = "o", markersize = 1, markerfacecolor = "cyan")
		plt.show()


	if __name__ == "__main__":

		# coordinates of 1st point
		x0, y0 = 20, 20

		# coordinates of 2nd point
		x1, y1 = 60, 50
		DDA(x0, y0, x1, y1)

  
def click2():

        # Emoji

        tools = turtle.Turtle() 

        #tools speed difine..
        tools.speed(2)

        #console background colour...
        turtle.getscreen().bgcolor("black")

        # function for creation of eye

        def eye(r, c): 

            tools.down() 

            tools.fillcolor(r) 

            tools.begin_fill() 

            tools.circle(c) 

            tools.end_fill() 

            tools.up() 

        # draw face

        tools.fillcolor('yellow') 

        tools.begin_fill()

        tools.circle(100) 

        tools.end_fill()

        tools.up()

        # draw eyes

        tools.goto(-40, 120) 

        eye('white', 15) 

        tools.goto(-37, 125) 

        eye('black', 5) 

        tools.goto(40, 120) 

        eye('white', 15) 

        tools.goto(40, 125) 

        eye('black', 5) 

        # draw mouth

        tools.goto(0, 45) 

        eye('black', 20) 


        tools.end_fill()

        tools.hideturtle()

def click3():

        #midPointCircleDraw

	def midPointCircleDraw(x_centre, y_centre, z):
		x = z
		y = 0
		
		# Printing the initial point the
		# axes after translation
		print("(", x + x_centre, ", ", y + y_centre, ")", sep = "", end = "")
		
		# When radius is zero only a single
		# point be printed
		if (z > 0) :
		
			print("(", x + x_centre, ", ", -y + y_centre, ")", sep = "", end = "")
			print("(", y + x_centre, ", ", x + y_centre, ")",sep = "", end = "")
			print("(", -y + x_centre, ", ", x + y_centre, ")", sep = "")
		
		# Initialising the value of P
		P = 1 - z

		while x > y:
		
			y += 1
			
			# Mid-point inside or on the perimeter
			if P <= 0:
				P = P + 2 * y + 1
				
			# Mid-point outside the perimeter
			else:		
				x -= 1
				P = P + 2 * y - 2 * x + 1
			
			# All the perimeter points have
			# already been printed
			if (x < y):
				break
			
			# Printing the generated point its reflection
			# in the other octants after translation
			print("(", x + x_centre, ", ", y + y_centre,")", sep = "", end = "")
			print("(", -x + x_centre, ", ", y + y_centre,")", sep = "", end = "")
			print("(", x + x_centre, ", ", -y + y_centre,")", sep = "", end = "")
			print("(", -x + x_centre, ", ", -y + y_centre,")", sep = "")
			
			# If the generated point on the line x = y then
			# the perimeter points have already been printed
			if x != y:
			
				print("(", y + x_centre, ", ", x + y_centre,")", sep = "", end = "")
				print("(", -y + x_centre, ", ", x + y_centre,")", sep = "", end = "")
				print("(", y + x_centre, ", ", -x + y_centre,")", sep = "", end = "")
				print("(", -y + x_centre, ", ", -x + y_centre,")", sep = "")
								
	# Driver Code
	if __name__ == '__main__':
		
		# To draw a circle of radius 3
		# centered at (0, 0)
		midPointCircleDraw(0, 0, 3)


     #Printing Name 

def click4(): 
        
        t=turtle.Pen()
        turtle.bgcolor("black")

        #define user input
        colors=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray', 'brown', 'aqua']

        your_name = turtle.textinput("Enter your name", "What is your name?")
        sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-10)?", 5, 1, 10) )

        #drive code
        for x in range(100):

            t.pencolor(colors[x%sides%3])
            t.penup()
            t.forward(x*3)
            t.pendown()
            t.write(your_name, font=("Arial", int( (x*1)/1), "bold") )
            t.left(120/sides)

 #Rainbow Benzene
  
def click5():

        colors = ['red', 'purple', 'blue', 'green', 'orange', 'violet']
        t = turtle.Pen()
        t.speed(39)
        turtle.bgcolor('black')
        for x in range(360):
            t.pencolor(colors[x%6])
            t.width(x//100 + 1)
            t.forward(x)
            t.left(59)

        #Rainbow

def click6():

    # Creating a turtle screen object
	sc = turtle.Screen()

	# Creating a turtle object(pen)
	pen = turtle.Turtle()

	# Defining a method to form a semicircle
	# with a dynamic radius and color
	def semi_circle(col, rad, val):

		# Set the fill color of the semicircle
		pen.color(col)

		# Draw a circle
		pen.circle(rad, -180)

		# Move the turtle to air
		pen.up()

		# Move the turtle to a given position
		pen.setpos(val, 0)

		# Move the turtle to the ground
		pen.down()

		pen.right(180)


	# Set the colors for drawing
	col = ['violet', 'indigo', 'blue',
		'green', 'yellow', 'orange', 'red']

	# Setup the screen features
	sc.setup(600, 600)

	# Set the screen color to black
	sc.bgcolor('black')

	# Setup the turtle features
	pen.right(90)
	pen.width(10)
	pen.speed(7)

	# Loop to draw 7 semicircles
	for i in range(7):
		semi_circle(col[i], 10*(
		i + 8), -10*(i + 1))

	# Hide the turtle
	pen.hideturtle()

#Sun Raise

def click7():

    
        screen = turtle.Screen()

        # background color
        screen.bgcolor("lightpink")

        # turtle object
        y = turtle.Turtle()

        # define function
        # for drawing rays of Sun
        def drawFourRays(t, length, radius):
            
            for i in range(4):
                t.penup()
                t.forward(radius)
                t.pendown()
                t.forward(length)
                t.penup()
                t.backward(length + radius)
                t.left(90)


        # Draw circle
        # to make sun
        y.penup()
        y.goto(85, 110)
        y.fillcolor("yellow")
        y.pendown()
        y.begin_fill()
        y.circle(45)
        y.end_fill()

        # Use the defined
        # function to draw rays
        y.penup()
        y.goto(85, 169)
        y.pendown()
        drawFourRays(y, 85, 54)
        y.right(45)
        drawFourRays(y, 85, 54)
        y.left(45)

        # To keep the
        # output window active
        turtle.done()


    # function for line generation

def click8():


        def bresenham(x1,y1,x2, y2):

            zm_new = 2 * (y2 - y1)
            slope_error_new = zm_new - (x2 - x1)

            y=y1
            for x in range(x1,x2+1):
            
                print("(",x ,",",y ,")\n")

                # Add slope to increment angle formed
                slope_error_new =slope_error_new + zm_new

                # Slope error reached limit, time to
                # increment y and update slope error.
                if (slope_error_new >= 0):
                    y=y+1
                    slope_error_new =slope_error_new - 2 * (x2 - x1)
                
            


        # driver function
        if __name__=='__main__':
            x1 = 3
            y1 = 2
            x2 = 15
            y2 = 5
            bresenham(x1, y1, x2, y2)

#driver code.....

window = Tk()
window.title("computer graphics project")
window.geometry("520x520")
window.config(background="#000000")

lable = Label(window,text="Please choice your desire method 😊",height=2, width=45, font=45,bg="light pink")
lable.pack()

button = Button(window,text="Corona Virus",height=1, width=42, font=25,bg="#D1EDEF",command=click)
button.pack()

button1 = Button(window,text="DDA",height=1, width=42, font=25,bg="#D1EDEF",command=click1)
button1.pack()

button2 = Button(window,text="Emoji",height=1, width=42, font=25,bg="#D1EDEF",command=click2)
button2.pack()

button3 = Button(window,text="Mid Point Circle Draw",height=1, width=42, font=25,bg="#D1EDEF",command=click3)
button3.pack()

button4 = Button(window,text="Printing Name",height=1, width=42, font=25,bg="#D1EDEF",command=click4)
button4.pack()

button5 = Button(window,text="Rainbow Benzene",height=1, width=42, font=25,bg="#D1EDEF",command=click5)
button5.pack()

button6 = Button(window,text="Rainbow",height=1, width=42, font=25,bg="#D1EDEF",command=click6)
button6.pack()

button7 = Button(window,text="Sun Raise",height=1, width=42, font=25,bg="#D1EDEF",command=click7)
button7.pack()

button8 = Button(window,text="Bresenham’s Line Generation",height=1, width=42, font=25,bg="#D1EDEF",command=click8)
button8.pack()

window.mainloop()