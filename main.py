# Implemented Python Libraries:
import tkinter as tk
from time import time, ctime
from random import randint
from datetime import datetime


class ExamTimer:
    
    """
    Aspects of the program:
    - main_window: tk.Tk()
        The main window of the program

    - canvas: tk.Canvas()
        The canvas on which the local time & the exam timer is displayed
        This will be the the only window that is displayed to the students during the exam along with the controls
            ^ this avoids confusion and prevents the students from getting distracted

    - clock: tk.Label()
        The label that displays the local time

    - timing_canvas: tk.Canvas()
        The canvas on which the controls are displayed

    - start_button: tk.Button()
        The button that starts the timer

    - stop_button: tk.Button()
        The button that stops/pauses the timer

    - reset_button: tk.Button()
        The button that resets the timer

    - settings_button: tk.Button()
        The button that opens the settings window for the NESA official/Administrator supervising the exam

    - local_time_clock(): function 
        Updates the local time every second, displayed on the canvas

    """

    # Initialize the main window
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("800x500")
        self.main_window.title("ExamTimer")

        # Create the canvas for displaying the grid
        self.canvas = tk.Canvas(self.main_window, width=700, height=600, bg="white")
        self.canvas.pack(side=tk.LEFT)
        self.clock = tk.Label(self.canvas, text=ctime(), font=('Helvetica Bold', 50), bg="white", 
                              fg="black", borderwidth=3, relief="groove")
        self.clock.place(relx=0.5, rely=0.1, anchor="n")

        # Create the canvas for the controls (start, stop, reset, settings)
        self.timing_canvas = tk.Canvas(self.main_window, width=100, height=100)
        self.timing_canvas.pack(side=tk.RIGHT)

        self.start_button = tk.Button(self.timing_canvas, text="Start", bg="Green", width=100, height=5).pack()

        self.stop_button = tk.Button(self.timing_canvas, text="Stop", bg="Red", width=100, height=5).pack()

        self.reset_button = tk.Button(self.timing_canvas, text="Reset", width=100, height=5).pack()

        self.settings_button = tk.Button(self.timing_canvas, text="Settings", width=100, height=5).pack()

        def local_time_clock():
            local_time = ctime()
            digital_clock = local_time[11:19]
            hours = int(local_time[11:13])

            if hours > 12:
                new_hours = hours - 12
                digital_clock = digital_clock.replace(local_time[11:13], str(new_hours), 1)
                digital_clock += " pm"

            elif hours == 12:
                digi_clock += " pm"

            elif hours == 0:
                new_hours = hours + 12
                digital_clock = digital_clock.replace(local_time[11:13], str(new_hours), 1)
                digital_clock += " am"


            self.clock['text'] = digital_clock
            self.main_window.after(1000, local_time_clock)

        def exam_timer():
            pass

        local_time_clock()

        # Run the main window
        self.main_window.mainloop()

# Run the program through the class 'ExamTimer'
ExamTimer()




