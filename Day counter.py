from tkinter import *
from datetime import *
import turtle

#user input

turtle.bgcolor("black")

year = int(turtle.numinput("Enter previous year:  ","year"))
months = int(turtle.numinput("Enter previous month:  ","Month"))
day = int(turtle.numinput("Enter previous date:  ","Date"))


today = datetime.now()

# days calculation process

previous_date = date(year, months , day)

present_date = today.date()

Day_count = present_date - previous_date


#print result

turtle.color('cyan')

Style = ('Courier', 18, 'bold')

turtle.write( Day_count,' days',font=Style, align='center')

turtle.done()


#created by 
# Tasnimul Hasan

