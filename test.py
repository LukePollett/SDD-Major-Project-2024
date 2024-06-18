"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)

Some code written here will be AI generated,
This is just because i may be stuck and/or need suggestions on how to do a certain aspect of my program.
I will not implement AI code word for word as this is big nono :(
"""
import tkinter as tk
from tkinter import *
import time


root = Tk()
root.title('                                      COUNT-DOWN TIMER')
#root.geometry("800x400")
root['background']='#2F4F4F'

total_time = 0

rest = 0

pause = "No"

#####ADD/MINUS/RESET FUNCTIONS

def add_time_hour():
    global total_time
    total_time += 3600
    countdown_label.config(text=f"{total_time//3600:02}:{(total_time//60)%60:02}:{total_time%60:02}",fg = '#00FF00',font=("Arial", 24))

def add_time_min():
    global total_time
    total_time += 60
    countdown_label.config(text=f"{total_time//3600:02}:{(total_time//60)%60:02}:{total_time%60:02}",fg= "#00FF00",font=("Arial", 24))

def add_time_sec():
    global total_time
    total_time += 1
    countdown_label.config(text=f"{total_time//3600:02}:{(total_time//60)%60:02}:{total_time%60:02}",fg= "#00FF00",font=("Arial", 24))

def add_rest_min():
    global rest
    rest += 60
    rest_label.config(text=f"{(rest // 3600) % 3600:02}:{(rest // 60) % 60:02}:{rest % 60:02}",fg= "#00FF00",font=("Arial", 24))

def reset():
    global total_time, rest,pause
    pause = "No"
    total_time = 0
    rest = 0
    countdown_label.config(text=f"{total_time//3600:02}:{(total_time//60)%60:02}:{total_time%60:02}",fg= "#00FF00",font=("Arial", 24))
    rest_label.config(text=f"{(rest // 3600) % 3600:02}:{(rest // 60) % 60:02}:{rest % 60:02}",fg= "#00FF00",font=("Arial", 24))

############TIME FUNCTIONS#############################################

def countdown():
    global total_time,rest, pause
    if total_time > 0 and pause == "No":
        total_time -= 1
        countdown_label.config(text=f"{(total_time // 3600) % 3600:02}:{(total_time // 60) % 60:02}:{total_time % 60:02}",fg="#00FF00", font=("Arial", 24))
        root.after(1000,countdown)
        if total_time == 0:
            countdown_label.config(
                text=f"{(total_time // 3600) % 3600:02}:{(total_time // 60) % 60:02}:{total_time % 60:02}", fg="red",
                font=("Arial", 24))

    elif total_time == 0 and rest > 0 and pause == "No":
        rest -= 1
        rest_label.config(text=f"{(rest// 3600) % 3600:02}:{(rest // 60) % 60:02}:{rest % 60:02}", fg="#00FF00", font=("Arial", 24))
        root.after(1000,countdown)
        if rest == 0:
            rest_label.config(text=f"{(rest // 3600) % 3600:02}:{(rest // 60) % 60:02}:{rest % 60:02}", fg="red",
                              font=("Arial", 24))

def countdown_pause():
    global pause
    pause = "Yes"

def countdown_unpause():
    global pause
    pause = "No"
    countdown()

#############LABELS####################
countdown_label = tk.Label(text = "00:00:00",fg="#00FF00",bg='#2F4F4F', font=("Arial", 24))
countdown_label.grid(row= 0, column = 2, columnspan=2)

countdown_label_title = tk.Label(text = "RUNNING: ",fg="#00FF00",bg='#2F4F4F', font=("Arial", 24))
countdown_label_title.grid(row= 0, column = 0, columnspan=2)

rest_label = tk.Label(text = "00:00:00", fg= "#00FF00",bg='#2F4F4F',font=("Arial", 24))
rest_label.grid(row= 1, column = 2, columnspan=2)

rest_label_title = tk.Label(text = "RESTING: ",fg="#00FF00",bg='#2F4F4F', font=("Arial", 24))
rest_label_title.grid(row= 1, column = 0, columnspan= 2)

#BUTTONS###
add_button = tk.Button(root, text="START", command=countdown, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 3, column = 1)

add_button = tk.Button(root, text="+HOUR", command=add_time_hour, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 2, column = 0)

add_button = tk.Button(root, text="+MNTS", command=add_time_min, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 2, column = 1)

add_button = tk.Button(root, text="+SCND", command=add_time_sec, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 2, column = 2)

add_button = tk.Button(root, text="RESET ", command=reset, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 3, column = 0)

add_button = tk.Button(root, text="RST-MIN", command=add_rest_min, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 2, column = 3)

add_button = tk.Button(root, text="PAUSE", command=countdown_pause, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 3, column = 2)

add_button = tk.Button(root, text="RESUME", command=countdown_unpause, bg='#36648B', font=("Arial", 18))
add_button.grid(row= 3, column = 3)

root.mainloop()