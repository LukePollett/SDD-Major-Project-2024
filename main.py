# Implemented Python Libraries:
import tkinter as tk
import time
from PIL import Image,ImageTk
import math

# Create the main class for the ExamTimer
class ExamTimer():

    # Initializing the main window
    def __init__(self):

        # Window Properties
        self.main_window = tk.Tk()

        # Making the window fullscreen (ish)
        width = self.main_window.winfo_screenwidth() 
        height = self.main_window.winfo_screenheight()
        self.main_window.state('zoomed')
        self.main_window.geometry("%dx%d" % (width, height))

        self.main_window.title("ExamTimer")

        # Create the canvas for the main window
        self.main_canvas = tk.Canvas(self.main_window, width=width, height=height, bg="white")
        self.main_canvas.pack(side=tk.LEFT)

        # Create the settings button
        temp_img = Image.open("menu.png")
        resized_bg = temp_img.resize((75, 75))
        button_image = ImageTk.PhotoImage(resized_bg)

        self.settings_button = tk.Button(self.main_canvas, image=button_image, borderwidth=0)
        self.settings_button.place(relx=0.997, rely=0.005, anchor="ne")
        
        # Create analog clock face
        def Analog_Clock():      

            def draw_clock():
                # Remove the previous sets of hands
                self.main_canvas.delete("all")

                # Get current time
                current_time = time.localtime()

                # Extracting hrs, mins, secs from current_time
                second = current_time.tm_sec
                minute = current_time.tm_min
                hour = current_time.tm_hour

                # Calculate angles for hour, minute, and second hands
                second_angle = math.radians(second * 6) # the * 6 is because there are 360 degrees in a circle and 60 seconds in a minute, so 360 / 60 = 6, hence one second is 6 degrees
                minute_angle = math.radians(minute * 6 + second / 10) # the + second / 10 makes the minute hand move slightly as the second hand moves
                hour_angle = math.radians((hour % 12) * 30 + minute / 2) # the + minute / 2 does the same ^ for the hour hand

                # Draw Clock Face (add numbers and notches, etc. below here)
                self.main_canvas.create_oval(40, 40, 360, 360, outline="black" , width=5)
                self.main_canvas.create_oval(45, 45, 355, 355, outline="black")
                self.main_canvas.create_oval(195, 195, 205, 205, fill="black")

                # Draw numbers and notches, et.c below here
                # ______

                # Draw The Hands:
                hour_x = 200 + 80 * math.sin(hour_angle)
                hour_y = 200 - 80 * math.cos(hour_angle)
                self.main_canvas.create_line(200, 200, hour_x, hour_y, fill="black", width=6)

                minute_x = 200 + 110 * math.sin(minute_angle)
                minute_y = 200 - 110 * math.cos(minute_angle)
                self.main_canvas.create_line(200, 200, minute_x, minute_y, fill="black", width=3)

                second_x = 200 + 120 * math.sin(second_angle)
                second_y = 200 - 120 * math.cos(second_angle)
                self.main_canvas.create_line(200, 200, second_x, second_y, fill="red", width=2)

                # Update the clock every 1000 ms (1 second)
                self.main_canvas.after(1000, draw_clock)

            draw_clock()

        # Create the Digital Clock
        def Digital_Clock():

            # Create the digital clock display
            self.digi_clock_display = tk.Label(self.main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                              fg="black", borderwidth=3, relief="groove")
            self.digi_clock_display.place(relx=0.25, rely=0.7, anchor="n")

            # Get the current time
            current_time = time.strftime('%I:%M:%S %p')
            # %I auto-converts to 12-hour time
            # %M is minutes, %S is seconds, %p is AM/PM

            # Update the clock display with new time
            self.digi_clock_display.config(text=current_time)

            # Update the clock every 1000 ms (1 second)
            self.main_window.after(1000, Digital_Clock)

        """
        def exam_timer():
            # Timer/Countdown for the exam:
                # Maybe implement an alarm/noise when the timer reaches 0
                    # Do not make noise too loud, but loud enough to be heard
                        # Assists with accessibility for those who are triggered by loud noises
        """

        # Create/Draw Both Clocks
        Analog_Clock()
        Digital_Clock()

        # Run the main window
        self.main_window.mainloop()

# Run the program through the class 'ExamTimer'
ExamTimer()