from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("700x300")
window.title("rock paper scissors game")

title_label = Label(window,text= "Rock paper scissors",width=20,height=10,font=font.Font(size=25),fg="grey")
title_label.place(x=200,y=-165)

options = Label(window,text="your options : ",font=font.Font(size=12))
options.place(x=75,y=75)

#rock_button = Button(window,text="rock",fg="white",bg="red")
#rock_button.place()

window.mainloop()