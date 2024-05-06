# Implemented Python Libraries:
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from time import ctime
from random import randint
from datetime import datetime
import math


# Create the main class for the ExamTimer
class ExamTimer():

    # Initializing the main window
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("800x600")
        self.main_window.title("ExamTimer")

        self.main_canvas = tk.Canvas(self.main_window, width=700, height=600, bg="white")
        self.main_canvas.pack(side=tk.LEFT)

        temp_bg = Image.open("clock.png")
        resized_bg = temp_bg.resize((307, 307))
        bg = ImageTk.PhotoImage(resized_bg)
        self.main_canvas.create_image(351, 47, image = bg, anchor = "n")
        self.main_canvas.create_oval(344, 194, 356, 206, fill="black", width=2)

        # Timer Label
        self.timer_label = tk.Label(self.main_canvas, text="Time Remaining:", font=('Helvetica Bold', 35), bg="white", 
                              fg="black", borderwidth=3, relief="groove").place(relx=0.5, rely=0.8, anchor="n")

        # Create the canvas for the controls (start, stop, reset, settings)
        self.timing_canvas = tk.Canvas(self.main_window, width=100, height=100)
        self.timing_canvas.pack(side=tk.RIGHT)

        #  Create the buttons for the controls
        self.start_button = tk.Button(self.timing_canvas, text="Start", bg="Green", width=100, height=5).pack(pady=5)

        self.stop_button = tk.Button(self.timing_canvas, text="Stop", bg="Red", width=100, height=5).pack(pady=5)

        self.reset_button = tk.Button(self.timing_canvas, text="Reset", width=100, height=5).pack(pady=5)

        self.settings_button = tk.Button(self.timing_canvas, text="Settings", width=100, height=5).pack(pady=5)
        
        # Create analog clock face
        def Analog_Clock():      

            def update_hands():
                local_time = ctime()

                def update_seconds():
                    # Update Second Hand Every 1 sec
                    seconds = int(local_time[17:19])
                    seconds_radians = math.radians(seconds)
                    seconds_radians = (seconds_radians * 6) - 1.5708
                    second_hand = self.main_canvas.create_line(350, 200, 350 + 140 * math.cos(seconds_radians), 200 + 140 * math.sin(seconds_radians), fill="red", width=3)
                    # self.main_canvas.after(1000, self.main_canvas.delete, second_hand)
                    self.main_window.after(1000, update_hands)
                    
                def update_minutes():
                    # Update Minute Hand Every 60 sec (1min)
                    minutes = int(local_time[14:16])
                    minutes_radians = math.radians(minutes)
                    minutes_radians = (minutes_radians * 6) - 1.5708
                    minute_hand = self.main_canvas.create_line(350, 200, 350 + 130 * math.cos(minutes_radians), 200 + 130 * math.sin(minutes_radians), fill="black", width=3)
                    # self.main_canvas.after(60000, self.main_canvas.delete, minute_hand)
                    self.main_window.after(60000, update_hands)
                    
                def update_hours():
                    # Update Hour Hand Every 3600 sec (1hr)
                    hours = int(local_time[11:13])
                    hours_radians = math.radians(hours)
                    hours_radians = (hours_radians * 30) - 1.5708
                    hour_hand = self.main_canvas.create_line(350, 200, 350 + 90 * math.cos(hours_radians), 200 + 100 * math.sin(hours_radians), fill="black", width=6)
                    # self.main_canvas.after(3600000, self.main_canvas.delete, hour_hand)
                    self.main_window.after(3600000, update_hands)
                    
                update_seconds()
                update_minutes()
                update_hours()

            update_hands()

        # Contains both the digital and analog clocks that display the computer's local time (ctime())
        def Digital_Clock():
            self.digi_clock_display = tk.Label(self.main_canvas, text=ctime(), font=('Helvetica Bold', 50), bg="white", 
                              fg="black", borderwidth=3, relief="groove")
            self.digi_clock_display.place(relx=0.5, rely=0.65, anchor="n")

            local_time = ctime()
            displayed_time = local_time[11:19]
            hours = int(local_time[11:13])
            
            # Convert Local Computer Time to 12-Hour Time:
            if hours > 12:
                new_hours = hours - 12
                displayed_time = displayed_time.replace(local_time[11:13], str(new_hours), 1)
                displayed_time += " pm"

            elif hours == 12:
                displayed_time += " pm"

            elif hours == 0:
                new_hours = hours + 12
                displayed_time = displayed_time.replace(local_time[11:13], str(new_hours), 1)
                displayed_time += " am"
            
            elif hours < 12:
                displayed_time += " am"

            # Update the Clock(s) every second
            self.digi_clock_display['text'] = displayed_time
            self.main_window.after(1000, Digital_Clock)

        # stub
        def exam_timer():
            # Timer/Countdown for the exam:
                # Maybe implement an alarm/noise when the timer reaches 0
                    # Do not make noise too loud, but loud enough to be heard
                        # Assists with accessibility for those who are triggered by loud noises
            pass

        Analog_Clock()
        Digital_Clock()

        # Run the main window
        self.main_window.mainloop()

# Run the program through the class 'ExamTimer'
ExamTimer()