import pygame
import tkinter as tk

# IDEA FOR MAJOR WORK:
    # Create a grid of squares
    # Each square is either a wall or a path
    # The user can click on a square to toggle it between a wall and a path
    # The user can place a starting and destination square
    # Use pythagoras' theorem to determine the distance between start and destination
    # Check all squares around the start square and determine the distance between them and the destination
    # Move to the square with the lowest distance, then check again from that square

# FURTHER IDEAS (difficult but worth it to implement if you have time)  
    # Maybe turn the project into a game?
    # Try and get it to work with real-world cities
    # Try and implement public transport routs as well as driving routes
    # Create a function that determines the time it takes to travel between two points
    # Create a function that determines the cost of travelling between two points
    # Create a function that can determine traffic conditions
    # Create a function that can determine the weather
    # Create a function that can determine travel times for different times of day

# Create the main window
root = tk.Tk()
root.title("Pathfinding API Simulator")

# Create the canvas for displaying the grid
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(side=tk.LEFT)

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
