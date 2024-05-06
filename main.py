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

        # Messing around with popups

        def open_settings():

            # get main window position
            root_x = self.main_window.winfo_rootx()
            root_y = self.main_window.winfo_rooty()

            # add offset
            win_x = root_x + 625
            win_y = root_y + 10

            settings_window = tk.Toplevel()
            settings_window.geometry("700x700")
            settings_window.geometry(f'+{win_x}+{win_y}')  

            settings_window.wm_attributes('-topmost', 'True', )
            settings_window.overrideredirect(True)

            settings_canvas = tk.Canvas(settings_window, width=700, height=700, bg="white")
            settings_canvas.pack()

            l = tk.Label(settings_canvas, text="Edit Exam Details Here", font=('Helvetica Bold', 50), bg="white", fg="black")
            l.place(relx=0.5, rely=0.5, anchor="center")

            b = tk.Button(settings_canvas, text="Done", font=('Helvetica Bold', 50), bg="white", fg="black", command=settings_window.destroy)
            b.place(relx=0.5, rely=0.6, anchor="center")

        # The settings is where the exam supervisor can change the different exams taking place,
        # and the time for each exam. There will be no interactable widgets on the main display,
        # except for the settings button itself, + exam timer controls (start, stop, clear, etc.)
        self.settings_button = tk.Button(self.main_canvas, image=button_image, borderwidth=0, command=open_settings)
        self.settings_button.place(relx=0.975, rely=0.043, anchor="ne")

        # Placeholder Stuff for Exam Timer and Subject Info
        self.labelframe = tk.LabelFrame(self.main_canvas, text="Examination Details", font=('Helvetica Bold', 20), width=600, height=100, fg="black", bg="white", borderwidth=6)
        self.labelframe.place(relx=0.7, rely=0.5, anchor="center")

        self.labelframe_text = tk.Label(self.labelframe, text="Subject/Exam Details Will Go Here", font=('Helvetica Bold', 20), fg="black", bg="white")
        self.labelframe_text.pack(padx=15, pady=15)

        class Examination():
            pass

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
                self.main_canvas.create_oval(140, 80, 570, 510, outline="black" , width=8)
                self.main_canvas.create_oval(150, 90, 560, 500, outline="lavender", width=5)
                self.main_canvas.create_oval(350, 290, 360, 300, fill="black")

                # Draw numbers
                for i in range(1, 13):
                    angle = math.radians(i * 30) # 360 (degrees) / 12 (unique hours) = 30 (degree per hour)
                    x = 355 + 180 * math.sin(angle)
                    y = 295 - 180 * math.cos(angle)
                    self.main_canvas.create_text(x, y, text=str(i), font=("Helvetica", 25, "bold"), fill="black")

                # Draw notches
                for i in range(60):
                    if i % 5 == 0:
                        angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
                        x1 = 355 + 215 * math.sin(angle)
                        y1 = 295 - 215 * math.cos(angle)
                        x2 = 355 + 195 * math.sin(angle)
                        y2 = 295 - 195 * math.cos(angle)
                        self.main_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
                        
                    else:
                        angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
                        x1 = 355 + 211 * math.sin(angle)
                        y1 = 295 - 211 * math.cos(angle)
                        x2 = 355 + 203 * math.sin(angle)
                        y2 = 295 - 203 * math.cos(angle)
                        self.main_canvas.create_line(x1, y1, x2, y2, width=3, fill="grey")

                # Draw numbers and notches, et.c below here
                # ______

                # Draw The Hands:
                hour_x = 355 + 120 * math.sin(hour_angle)
                hour_y = 295 - 120 * math.cos(hour_angle)
                self.main_canvas.create_line(355, 295, hour_x, hour_y, fill="black", width=8)

                minute_x = 355 + 150 * math.sin(minute_angle)
                minute_y = 295 - 150 * math.cos(minute_angle)
                self.main_canvas.create_line(355, 295, minute_x, minute_y, fill="black", width=4)

                second_x = 355 + 165 * math.sin(second_angle)
                second_y = 295 - 165 * math.cos(second_angle)
                self.main_canvas.create_line(355, 295, second_x, second_y, fill="red", width=2)

                # Update the clock every 1000 ms (1 second)
                self.main_canvas.after(1000, draw_clock)

            draw_clock()

        # Create the Digital Clock
        def Digital_Clock():

            # Create the digital clock display
            digi_clock_display = tk.Label(self.main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                              fg="black", borderwidth=10, relief="groove")
            digi_clock_display.place(relx=0.25, rely=0.75, anchor="n")

            # Get the current time
            current_time = time.strftime('%I:%M:%S %p')
            # %I auto-converts to 12-hour time
            # %M is minutes, %S is seconds, %p is AM/PM

            # Update the clock display with new time
            digi_clock_display.config(text=current_time)

            # Update the clock every 1000 ms (1 second)
            self.main_window.after(1000, Digital_Clock)

        """
        def timer():
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