import tkinter 
from tkinter import *

#fucnction

val= ""
def button1_isclicked():
    global val
    val=val+"1"
    data.set(val)

def button2_isclicked():
    global val
    val=val+"2"
    data.set(val)

    
root = tkinter.Tk()
root.geometry("250x400+300+300")            #+300+300 so that it opens in the center
root.resizable(0,0)                         #as 0 is a boolean value, it won't be resizable
root.title("Calculator")


#Label
data = StringVar
label = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable = data, background="#ffffff", fg="#000000")  #anchor= SE---> anchor the text in south-east
label.pack(expand=True, fill= "both")

#FRAMES
#frames are containers for child entities. you can fill them in frames and divide the area accordingly.
button_row1 = Frame(root)                       #only one parameter is passed for frames that is where should it belong, here for eg- root
button_row1.pack(expand= True, fill = "both")   #expand allows frames to expand, fill allows to  exapnd in the given direction

button_row2 = Frame(root)
button_row2.pack(expand= True, fill = "both")

button_row3 = Frame(root)
button_row3.pack(expand= True, fill = "both")

button_row4 = Frame(root)
button_row4.pack(expand= True, fill = "both")

#BUTTONS
#Row 1 
button1= Button( button_row1, text= "1", font= ("Verdana", 22), relief = GROOVE, border= 0, command=button1_isclicked)
button1.pack(side= LEFT, expand= True, fill= "both")

button2= Button( button_row1, text= "2", font= ("Verdana", 22), relief = GROOVE, border= 0, command= button2_isclicked)
button2.pack(side= LEFT, expand= True, fill= "both")

button3= Button( button_row1, text= "3", font= ("Verdana", 22), relief = GROOVE, border= 0,)
button3.pack(side= LEFT, expand= True, fill= "both")

button_add= Button( button_row1, text= "+", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_add.pack(side= LEFT, expand= True, fill= "both")

#Row 2
button4= Button( button_row2, text= "4", font= ("Verdana", 22), relief = GROOVE, border= 0)
button4.pack(side= LEFT, expand= True, fill= "both")

button5= Button( button_row2, text= "5", font= ("Verdana", 22), relief = GROOVE, border= 0)
button5.pack(side= LEFT, expand= True, fill= "both")

button6= Button( button_row2, text= "6", font= ("Verdana", 22), relief = GROOVE, border= 0)
button6.pack(side= LEFT, expand= True, fill= "both")

button_sub= Button( button_row2, text= "-", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_sub.pack(side= LEFT, expand= True, fill= "both")

#Row 3
button7= Button( button_row3, text= "7", font= ("Verdana", 22), relief = GROOVE, border= 0)
button7.pack(side= LEFT, expand= True, fill= "both")

button8= Button( button_row3, text= "8", font= ("Verdana", 22), relief = GROOVE, border= 0)
button8.pack(side= LEFT, expand= True, fill= "both")

button9= Button( button_row3, text= "9", font= ("Verdana", 22), relief = GROOVE, border= 0)
button9.pack(side= LEFT, expand= True, fill= "both")

button_mul= Button( button_row3, text= "*", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_mul.pack(side= LEFT, expand= True, fill= "both")

#Row 4
button_clear= Button( button_row4, text= "C", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_clear.pack(side= LEFT, expand= True, fill= "both")

button0= Button( button_row4, text= "0", font= ("Verdana", 22), relief = GROOVE, border= 0)
button0.pack(side= LEFT, expand= True, fill= "both")

button_eq= Button( button_row4, text= "=", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_eq.pack(side= LEFT, expand= True, fill= "both")

button_div= Button( button_row4, text= "/", font= ("Verdana", 22), relief = GROOVE, border= 0)
button_div.pack(side= LEFT, expand= True, fill= "both")



root.mainloop()