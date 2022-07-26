                                    #               Day counter project
  
                                    #  -> it helps to count, girls previous or future period day
                                    # -> it helps to count, any product purchasing days like as phone, sim card.... etc
                                    
# define module

from tkinter import *
from datetime import *
import turtle
                                                                                 
#manual Day count

def manualCount():

    #user input
    
    turtle.bgcolor("black")

    past_year1 = int(turtle.numinput("Enter previous year:  ","1st prvious year"))
    past_months1 = int(turtle.numinput("Enter previous month:  ","1st prvious Month"))
    past_dayy = int(turtle.numinput("Enter previous date:  ","1st prvious Date"))

    past_year2 = int(turtle.numinput("Enter previous year:  ","2nd previuos year"))
    past_months2 = int(turtle.numinput("Enter previous month:  ","2nd previous Month "))
    past_day2 = int(turtle.numinput("Enter previous date:  ","2nd previous Date"))

    # past days calculation process

    pastDay = date(past_year1, past_months1, past_dayy)
    pastDay2 = date(past_year2, past_months2, past_day2)

    dayCount = pastDay - pastDay2

    #print result

    Input = 401

    if Input == 401:

            turtle.color('cyan')
            Style = ('Courier', 18, 'bold')

            turtle.write( dayCount,' days',font=Style, align='center')
            turtle.done()

            
#count from present date

def autoCount():

    #user input

    turtle.bgcolor("black")

    previous_year = int(turtle.numinput("Enter previous year:  ","previous year"))
    previous_months = int(turtle.numinput("Enter previous month:  ","pervious Month"))
    previous_day = int(turtle.numinput("Enter previous date:  ","previous Date"))

    # days calculation process

    today = datetime.now()
    previous_date = date(previous_year, previous_months, previous_day)
    present_date = today.date()

    #math driver code
    Day_count = present_date - previous_date

    #print result

    turtle.color('cyan')
    Style = ('Courier', 18, 'bold')

    turtle.write( Day_count,' days',font=Style, align='center')
    turtle.done()


                                                                # Graphic Driver code

                                    
    #define pop up window scaling

window = Tk()
window.title('Day counter' )
window.geometry('430x300')
window.config(background="#000000")
 
# define lable text

lable = Label(window,text="Please choice your desire method 😊",height=1, width=50, font=('Arial',12),bg="cyan")
lable.pack()

#button

autocount_button = Button(window,text='Day count from Today',height=1,width=24,font=('Arial',14),bg= 'white',command=autoCount)
autocount_button.pack()

manualcount_button = Button(window,text="Day count from any year",height=1,width=24,font=('Arial',14),bg= 'white',command=manualCount)
manualcount_button.pack()

window.mainloop()


#created by 
# Tasnimul Hasan