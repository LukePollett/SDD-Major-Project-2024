import tkinter as tk
from tkinter import *
from time import ctime, sleep
from random import randint

# OFFICIAL IDEA: Make the HSC Clock thingo better

# Create the main window
main_window = tk.Tk()
main_window.geometry("700x500")
main_window.title("HSC Timer")

# Create the canvas for displaying the grid
canvas = tk.Canvas(main_window, width=500, height=500, bg="white")
canvas.pack(side=tk.LEFT)
clock = tk.Label(canvas, text=ctime(), font=('Arial', 25), bg="white", 
                 fg="black", borderwidth=3, relief="solid")
clock.place(relx=0.5, rely=0.5, anchor="center")

# Create the frame for the controls
controls_frame = tk.Frame(main_window, padx=10, pady=10)
controls_frame.pack(side=tk.RIGHT)

# Create the controls
start_button = tk.Button(controls_frame, text="Start")
start_button.pack(pady=5)

stop_button = tk.Button(controls_frame, text="Stop")
stop_button.pack(pady=5)

reset_button = tk.Button(controls_frame, text="Reset")
reset_button.pack(pady=5)

def update_time():
    clock['text'] = ctime()
    main_window.after(1000, update_time)

update_time()

main_window.mainloop()


