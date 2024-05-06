"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)
"""
# So i essentially want to get the code for the analog clock and implement it into the main program
# Preferrably into a canvas for organisation

import tkinter as tk
import time
import math

# USE FOR MAIN PROGRAM:
print(time.localtime())
# time.localtime() returns a struct_time object in the following form:
# time.struct_time(tm_year=(year int), tm_mon=(month int), tm_mday=(day int), tm_hour=(hour int), tm_min=(min int), tm_sec=(sec int), tm_wday=(which day of the week is it (int form 1 - 7)), tm_yday=(day of the year int), tm_isdst=(is daylight savings time on? (int 0 or 1) maybe idk))

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
        # This is the worst part.
        # Ah so it calculates each hand's angle separately.
        # So the hour hand is calculated by taking the hour and multiplying it by 30 (because there are 360 degrees in a circle and 12 (im guessing unique) hours in a day, so 360 / 12 = 30) and then adding the minute divided by 2 (because there are 60 minutes in an hour and 30 / 60 = 0.5) to account for the hour hand moving slightly as the minute hand moves.
        
        hour_angle = math.radians((hour % 12) * 30 + minute / 2) # the + minute / 2 makes the hour hand move slightly as the minute hand moves
        minute_angle = math.radians(minute * 6 + second / 10) # the + second / 10 makes the minute hand move slightly as the second hand moves
        second_angle = math.radians(second * 6) # the * 6 is because there are 360 degrees in a circle and 60 seconds in a minute, so 360 / 60 = 6, hence one second is 6 degrees

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