"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)
"""

import tkinter as tk
import time
import math


def create_clock():
    root = tk.Tk()
    root.title("Analog Clock")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    def draw_clock():
        canvas.delete("all")

        # Get current time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Calculate angles for hour, minute, and second hands
        hour_angle = math.radians((hour % 12) * 30 + minute / 2)
        minute_angle = math.radians(minute * 6 + second / 10)
        second_angle = math.radians(second * 6)

        # Draw clock face
        canvas.create_oval(50, 50, 350, 350)

        # Draw hour hand
        hour_x = 200 + 60 * math.sin(hour_angle)
        hour_y = 200 - 60 * math.cos(hour_angle)
        canvas.create_line(200, 200, hour_x, hour_y, width=6)

        # Draw minute hand
        minute_x = 200 + 80 * math.sin(minute_angle)
        minute_y = 200 - 80 * math.cos(minute_angle)
        canvas.create_line(200, 200, minute_x, minute_y, width=4)

        # Draw second hand
        second_x = 200 + 90 * math.sin(second_angle)
        second_y = 200 - 90 * math.cos(second_angle)
        canvas.create_line(200, 200, second_x, second_y, width=2)

        # Update clock every 1000 milliseconds (1 second)
        canvas.after(1000, draw_clock)

    draw_clock()
    root.mainloop()

create_clock()