# Implemented Python Libraries:
import tkinter as tk
from time import time, ctime
from random import randint
from datetime import datetime
import math

class ExamTimer():

    # Initialize the main window
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("800x600")
        self.main_window.title("ExamTimer")

        # Create the canvas for displaying the grid
        self.canvas = tk.Canvas(self.main_window, width=700, height=600, bg="white")
        self.canvas.pack(side=tk.LEFT)

        self.clock = tk.Label(self.canvas, text=ctime(), font=('Helvetica Bold', 75), bg="white", 
                              fg="black", borderwidth=3, relief="groove")
        self.clock.place(relx=0.5, rely=0.7, anchor="n")

        # Create the canvas for the controls (start, stop, reset, settings)
        self.timing_canvas = tk.Canvas(self.main_window, width=100, height=100)
        self.timing_canvas.pack(side=tk.RIGHT)

        #  Create the buttons for the controls
        self.start_button = tk.Button(self.timing_canvas, text="Start", bg="Green", width=100, height=5).pack(pady=5)

        self.stop_button = tk.Button(self.timing_canvas, text="Stop", bg="Red", width=100, height=5).pack(pady=5)

        self.reset_button = tk.Button(self.timing_canvas, text="Reset", width=100, height=5).pack(pady=5)

        self.settings_button = tk.Button(self.timing_canvas, text="Settings", width=100, height=5).pack(pady=5)

        # Create the hands of the analog clock
        self.canvas.create_line(350, 200, 350, 35, fill="red", width=5)
        
        # Contains both the digital and analog clocks that display the computer's local time (ctime())
        def local_time_clocks():
            local_time = ctime()
            digital_clock = local_time[11:19]
            hours = int(local_time[11:13])

            # Convert to 12-Hour Time
            if hours > 12:
                new_hours = hours - 12
                digital_clock = digital_clock.replace(local_time[11:13], str(new_hours))
                digital_clock += " pm"

            elif hours == 12:
                digital_clock += " pm"

            elif hours == 0:
                new_hours = hours + 12
                digital_clock = digital_clock.replace(local_time[11:13], str(new_hours))
                digital_clock += " am"
            
            elif hours < 12:
                digital_clock += " am"

            # Update the Digital Clock every second
            self.clock['text'] = digital_clock
            self.main_window.after(1000, local_time_clocks)

            # Create the Analog Clock
            # Extract the seconds part from ctime(), convert it to an integer, and then convert it to radians
            # The seconds hand will be drawn using the radians value
            

        def exam_timer():
            pass

        local_time_clocks()

        # Run the main window
        self.main_window.mainloop()

# Run the program through the class 'ExamTimer'
ExamTimer()




