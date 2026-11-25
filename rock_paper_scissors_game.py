from tkinter import *
import tkinter.font as font
import random

window = Tk()
window.geometry("700x500")
window.title("rock paper scissors game")

player_score = 0
computer_score = 0
def onbuttonpress():
    get_computer_choice()
    get_player_choice()

def get_computer_choice():
    computer_choice =random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def get_player_choice(player_input):

    computer_input = get_computer_choice()
    computer_select_label.config(text=f"computer selected : {computer_input}")
    player_select_label.config(text=f"player selected : {player_input}")
    if player_input == computer_input:
        tie()
    
    print(player_input)
    print(computer_input)
    

def player_wins():
    global player_score,computer_score
    player_score += 1
    winner_label.config(text="You win!!!")
    player_score_label.config(text=f"your score : {player_score}")
    computer_score_label(text=f"computer score : {computer_score}")

def computer_wins():
    global player_score,computer_score
    computer_score += 1
    winner_label.config(text="Computer wins!!!")
    player_score_label.config(text=f"your score : {player_score}")
    computer_score_label(text=f"computer score : {computer_score}")
    
def tie():
    global player_score,computer_score
    winner_label.config(text="Tie!!!")
    player_score_label.config(text=f"your score : {player_score}")
    computer_score_label(text=f"computer score : {computer_score}")

title_label = Label(window,text= "Rock paper scissors",width=20,height=10,font=font.Font(size=25),fg="grey")
title_label.place(x=150,y=-165)

winner_label = Label(window,text="lets start the game...",fg="green",font=font.Font(size=20))
winner_label.place(x=210,y=75)

options = Label(window,text="your options : ",font=font.Font(size=20))
options.place(x=20,y=150)

rock_button = Button(window,text="rock",fg="white",bg="red",width=7,height=1,font=font.Font(size=15),command=onbuttonpress)
rock_button.place(x=215,y=150)

paper_button = Button(window,text="paper",fg="white",bg="green",width=7,height=1,font=font.Font(size=15),command=onbuttonpress)
paper_button.place(x=375,y=150)

scissors_button = Button(window,text="scissors",fg="white",bg="blue",width=7,height=1,font=font.Font(size=15),command=onbuttonpress)
scissors_button.place(x=525,y=150)

score_label = Label(window,text="your score : ",font=font.Font(size=20))
score_label.place(x=20,y=250)

player_select_label = Label(window,text="you selected : ",font=font.Font(size=15))
player_select_label.place(x=200,y=280)

player_score_label = Label(window,text="your score : ",font=font.Font(size=15))
player_score_label.place(x=475,y=280)

computer_select_label = Label(window,text="computer selected : ",font=font.Font(size=15))
computer_select_label.place(x=200,y=320)

computer_score_label = Label(window,text="computer score : ",font=font.Font(size=15))
computer_score_label.place(x=475,y=320)

window.mainloop()
