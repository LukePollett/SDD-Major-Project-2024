import tkinter as tk
from tkinter import *
from time import time, ctime, sleep

# OFFICIAL IDEA: Make the HSC Clock thingo better

# Create the main window
root = tk.Tk()
root.geometry("700x500")
root.title("HSC Timer")

# Create the canvas for displaying the grid
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack(side=tk.LEFT)
clock = tk.Label(canvas, text=ctime(), bg="white", fg="black")
clock.place(relx=0.5, rely=0.5, anchor="center")

# Create the frame for the controls
controls_frame = tk.Frame(root, padx=10, pady=10)
controls_frame.pack(side=tk.RIGHT)

# Create the controls
start_button = tk.Button(controls_frame, text="Start")
start_button.pack(pady=5)

stop_button = tk.Button(controls_frame, text="Stop")
stop_button.pack(pady=5)

reset_button = tk.Button(controls_frame, text="Reset")
reset_button.pack(pady=5)

# Start the main loop
root.mainloop()

# This makes a working, ticking clock in the terminal
# while True:
#     print(ctime())
#     sleep(1)


