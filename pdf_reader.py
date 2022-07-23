#import module

from tkinter import *

   #variable define

Input = ''

#input number calculation

def data(symbol):

    global Input
    Input += str(symbol)
    lable.delete(1.0,'end')
    lable.insert(1.0,Input)

# input Number evalution

def evalution():

    try:
        global Input
        result = str(eval(Input))
        
        lable.delete(1.0,'end')
        lable.insert(1.0, '-> Cashout charge: ' + result + ' Tk')
    except:
         clear_feild()
         lable.insert(1.0, 'error')

#clear input number

def clear_feild():
    
    global Input
    Input =''
    lable.delete(1.0,'end')


                                            #Geaphics Driver Code

# window scaling

window = Tk()
window.title(" MFS Calculator ")
window.geometry("431x530")
window.config(background="#000000")

#window labte

lable = Text(window,height=4, width=40, font=('Arial',14),bg="white")
lable.grid(columnspan=5)

#Button define

button1 = Button(window,text="1",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(1))
button1.grid(row=2,column=1)

button2= Button(window,text="2",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(2))
button2.grid(row=2,column=2)

button3 = Button(window,text="3",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(3))
button3.grid(row=2,column=3)

button4 = Button(window,text="4",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(4))
button4.grid(row=2,column=4)

button5 = Button(window,text="5",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(5))
button5.grid(row=3,column=1)

button6= Button(window,text="6",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(6))
button6.grid(row=3,column=2)

button7 = Button(window,text="7",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(7))
button7.grid(row=3,column=3)

button8 =Button(window,text="8",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(8))
button8.grid(row=3,column=4)

buttonMulti =Button(window,text="*",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data('*'))
buttonMulti.grid(row=4,column=1)

buttonPlus= Button(window,text="+",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data('+'))
buttonPlus.grid(row=5,column=1)

buttonMinus= Button(window,text="-",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data('-'))
buttonMinus.grid(row=5,column=2)

buttonDivide= Button(window,text="/",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data('/'))
buttonDivide.grid(row=5,column=3)

button9 = Button(window,text="9",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(9))
button9.grid(row=4,column=3)

button0= Button(window,text="0",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(0))
button0.grid(row=4,column=2)

buttonEnter = Button(window,text='Enter',height=3, width=7, font=('Arial',14),bg='light pink',command=evalution)
buttonEnter.grid(row=6,column=3)

buttonEnter1 = Button(window,text='',height=3, width=7, font=('Arial',14),bg='light pink')
buttonEnter1.grid(row=7,column=3)

button_clear=Button(window,text="Clear",height=3, width=7, font=('Arial',14),bg="light pink",command=clear_feild)
button_clear.grid(row=5,column=4)

button_clear1=Button(window,text=" ",height=3, width=7, font=('Arial',14),bg="light pink")
button_clear1.grid(row=6,column=4)

button_clear2=Button(window,text=" ",height=3, width=7, font=('Arial',14),bg="light pink")
button_clear2.grid(row=7,column=4)

Dot_button = Button(window,text=".",height=2, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data('.'))
Dot_button.grid(row=4,column=4)

nagad_button =Button(window,text=" Nagad App ",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(' * 0.01150'))
nagad_button.grid(row=6,column=1)

bkash_button2= Button(window,text=" Nagad ",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(' * 0.0150'))
bkash_button2.grid(row=6,column=2)

bkash_button2= Button(window,text=" Bkash ",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(' * 0.0185'))
bkash_button2.grid(row=7,column=2)

nagad_button =Button(window,text=" Bkash App ",height=3, width=7, font=('Arial',14),bg="#D1EDEF",command=lambda:data(' * 0.014'))
nagad_button.grid(row=7,column=1)

window.mainloop()



#Created by:
#Tasnimul Hasan