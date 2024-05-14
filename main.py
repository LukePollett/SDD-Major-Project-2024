# Implemented Python Libraries:
import tkinter as tk
from tkinter import *
import time
from PIL import Image,ImageTk
import math

# Invigilation Software for the HSC (+ maybs other exams)

# Create the main class for the ExamTimer
class ClockwiseScholar():

    # Initializing the main window
    def __init__(self):

        # Window Properties
        self.main_window = tk.Tk()

        # Making the window fullscreen (ish)
        width = self.main_window.winfo_screenwidth() # MacBook Resolution = 1440 x 900
        height = self.main_window.winfo_screenheight()
        self.main_window.state('zoomed')
        self.main_window.geometry("%dx%d" % (width, height))

        self.main_window.title("Clockwise Scholar - Examination Management and Timing")

        # Create the canvas for the main window
        self.main_canvas = tk.Canvas(self.main_window, width=width, height=height, bg="white")
        self.main_canvas.pack(side=tk.LEFT)

        # Create the settings button
        temp_img = Image.open("menu.png")
        resized_bg = temp_img.resize((75, 75))
        button_image = ImageTk.PhotoImage(resized_bg)

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

            settings_canvas = tk.Canvas(settings_window, width=700, height=700, bg="light grey")
            settings_canvas.pack()

            b = tk.Button(settings_canvas, text="Done", font=('Helvetica Bold', 50), bg="white", fg="black", command=settings_window.destroy)
            b.place(relx=0.5, rely=0.9, anchor="center")

            # Displaying the selected option as a label (temporary, will implement more widgets)
            # Also check if the selected option is a valid subject
                # (this excludes stuff like "<< Select an Option >>", "-- Mandatory Courses --", and "-- Elective Courses --")
            def show():
                if clicked.get() == "<< Select an Option >>": 
                    pass
                elif clicked.get() == "-- Mandatory Courses --":
                    pass
                elif clicked.get() == "-- Elective Courses --":
                    pass
                else:
                    selected_subject.config(text = clicked.get()) 

            # Subject Exam Selection for Stages 4 and 5 are kinda just there for placeholder purposes.
            # This program is mainly for Stage 6, but I added the other stages just in case in the future,
            # i want to have options to switch between year groups.

            # Subject Exam Selection for Years 7 and 8
            Stage_4_Subjects = [
                "<< Select an Option >>",
                "English",
                "Geography",
                "History",
                "Chinese",
                "Italian", 
                "Japanese",
                "Mathematics",
                "Music",
                "PDHPE",
                "Religious Education",
                "Science",
                "Technology",
                "Visual Arts"
            ]

            # Subject Exam Selection for Years 9 and 10
            Stage_5_Subjects = [
                "<< Select an Option >>",
                "-- Mandatory Courses --",
                "English",
                "Geography",
                "History",
                "Mathematics",
                "PDHPE",
                "Religious Education",
                "Science",
                "-- Elective Courses --",
                "Chinese",
                "Chinese Native",
                "Commerce",
                "Design and Technology",
                "Drama",
                "History Elective",
                "Industrial Technology - Engineering",
                "Industrial Technology - Timber",
                "Information and Software Technology",
                "Chinese",
                "Italian",
                "Japanese",
                "Music",
                "Photographic and Digital Media",
                "Physical Activity and Sports Studies",
                "Visual Arts"
            ]

            # Subject Exam Selection for Years 11 and 12 (Preliminary and HSC)(State-Wide)
            Stage_6_Subjects = [ 
                "Aboriginal Studies", # 3hrs working, 5 mins reading
                "Agriculture", # 3hrs working, 5 mins reading
                "Ancient History", # 3hrs working, 5 mins reading
                "Arabic Continuers", # 2hrs 50 mins working, 10 mins reading
                "Arabic Extension", # 1hr 50 mins working, 10 mins reading
                "Armenian Continuers", # 2hrs 30 mins working, 10 mins reading
                "Automotive", # 2hrs working, 5 mins reading
                "Biology", # 3hrs working, 5 mins reading
                "Business Services", # 2hrs working, 5 mins reading
                "Business Studies", # 3hrs working, 5 mins reading
                "Chemistry", # 3hrs working, 5 mins reading
                "Chinese Beginners", # 2hrs 30 mins working, 10 mins reading
                "Chinese Continuers", # 2hrs 50 mins working, 10 mins reading
                "Chinese Extension", # 1hr 50 mins working, 10 mins reading
                "Chinese & Literature", # 2hrs 50 mins working, 10 mins reading
                "Chinese in Context", # 2hrs 30 mins working, 10 mins reading
                "Classical Greek Continuers", # 3hrs working, 5 mins reading
                "Classical Greek Extension", # 1hr 50 mins working, 10 mins reading
                "Classical Hebrew Continuers", # 3hrs working, 5 mins reading
                "Classical Hebrew Extension", # 1hr 50 mins working, 10 mins reading
                "Community & Family Studies", # 3hrs working, 5 mins reading
                "Construction", # 2hrs working, 5 mins reading
                "Croatian Continuers", # 2hrs 30 mins working, 10 mins reading
                "Design & Technology", # 1hr 30 mins working, 5 mins reading
                "Drama", # 1hr 30 mins working, 5 mins reading
                "Earth & Environmental Science", # 3hrs working, 5 mins reading
                "Economics", # 3hrs working, 5 mins reading
                "Electrotechnology", # 2hrs working, 5 mins reading
                "Engineering Studies", # 3hrs working, 5 mins reading
                "English Advanced Paper 1", # 1hr 30 mins working, 10 mins reading
                "English Advanced Paper 2", # 2hrs working, 5 mins reading
                "English EAL/D Paper 1", # 1hr 30 mins working, 10 mins reading
                "English EAL/D Paper 2", # 1 hr working, 5 mins reading
                "English EAL/D Listening Paper", # 30 minutes working, including reading time
                "English Extension 1", # 2hrs working, 10 mins reading
                "English Standard Paper 1", # 1hr 30 mins working, 10 mins reading
                "English Standard Paper 2", # 2hrs working, 5 mins reading
                "English Studies", # 2hrs 30 mins working, 10 mins reading
                "Entertainment Industry", # 2hrs working, 5 mins reading
                "Filipino Continuers", # 2hrs 30 mins working, 10 mins reading
                "Financial Services", # 2hrs working, 5 mins reading
                "Food Technology", # 3hrs working, 5 mins reading
                "French Beginners", # 2hrs 30 mins working, 10 mins reading
                "French Continuers", # 2hrs 50 mins working, 10 mins reading
                "French Extension", # 1hr 50 mins working, 10 mins reading
                "Geography", # 3hrs working, 5 mins reading
                "German Beginners", # 2hrs 30 mins working, 10 mins reading
                "German Continuers", # 2hrs 50 mins working, 10 mins reading
                "German Extension", # 1hr 50 mins working, 10 mins reading
                "History Extension", # 2hrs working, 10 mins reading
                "Hospitality - Food & Beverage", # 2hrs working, 5 mins reading
                "Hospitality - Kitchen Operations & Cookery", # 2hrs working, 5 mins reading
                "Human Services", # 2hrs working, 5 mins reading
                "Indonesian Beginners", # 2hrs 30 mins working, 10 mins reading
                "Indonesian Continuers", # 2hrs 50 mins working, 10 mins reading
                "Indonesian Extension", # 1hr 50 mins working, 10 mins reading
                "Indonesian & Literature", # 2hrs 50 mins working, 10 mins reading
                "Industrial Technology - Automotive", # 1hr 30 mins working, 5 mins reading
                "Industrial Technology - Electronics", # 1hr 30 mins working, 5 mins reading
                "Industrial Technology - Graphics", # 1hr 30 mins working, 5 mins reading
                "Industrial Technology - Metal & Engineering", # 1hr 30 mins working, 5 mins reading
                "Industrial Technology - Multimedia", # 1hr 30 mins working, 5 mins reading
                "Industrial Technology - Timber & Furniture", # 1hr 30 mins working, 5 mins reading
                "Information Processes & Technology", # 3hrs working, 5 mins reading
                "Information & Digital Technology", # 2hrs working, 5 mins reading
                "Investigating Science", # 3hrs working, 5 mins reading
                "Italian Beginners", # 2hrs 30 mins working, 10 mins reading
                "Italian Continuers", # 2hrs 50 mins working, 10 mins reading
                "Italian Extension", # 1hr 50 mins working, 10 mins reading
                "Japanese Beginners", # 2hrs 30 mins working, 10 mins reading
                "Japanese Continuers", # 2hrs 50 mins working, 10 mins reading
                "Japanese Extension", # 1hr 50 mins working, 10 mins reading
                "Japanese in Context", # 2hrs 30 mins working, 10 mins reading
                "Korean Beginners", # 2hrs 30 mins working, 10 mins reading
                "Korean Continuers", # 2hrs 50 mins working, 10 mins reading
                "Korean & Literature", # 2hrs 50 mins working, 10 mins reading
                "Korean in Context", # 2hrs 30 mins working, 10 mins reading
                "Latin Continuers", # 3hrs working, 5 mins reading
                "Latin Extension", # 2hrs working, 10 mins reading
                "Legal Studies", # 3hrs working, 5 mins reading
                "Mathematics Advanced", # 3hrs working, 10 mins reading
                "Mathematics Extension 1", # 2hrs working, 10 mins reading
                "Mathematics Extension 2", # 3hrs working, 10 mins reading
                "Mathematics Standard 1", # 2hrs working, 10 mins reading
                "Mathematics Standard 2", # 2hrs 30 mins working, 10 mins reading
                "Modern Greek Beginners", # 2hrs 30 mins working, 10 mins reading
                "Modern Greek Continuers", # 2hrs 50 mins working, 10 mins reading
                "Modern Greek Extension", # 1hr 50 mins working, 10 mins reading
                "Modern Hebrew Continuers", # 2hrs 50 mins working, 10 mins reading
                "Modern History", # 3hrs working, 5 mins reading
                "PDHPE", # 3hrs working, 5 mins reading
                "Physics", # 3hrs working, 5 mins reading
                "Primary Industries", # 2hrs working, 5 mins reading
                "Retail Services", # 2hrs working, 5 mins reading
                "Serbian Continuers", # 2hrs 30 mins working, 10 mins reading
                "Society and Culture", # 2hrs working, 5 mins reading
                "Software Design and Development", # 3hrs working, 5 mins reading
                "Spanish Beginners", # 2hrs 30 mins working, 10 mins reading
                "Spanish Continuers", # 2hrs 50 mins working, 10 mins reading
                "Spanish Extension", # 1hr 50 mins working, 10 mins reading
                "Studies of Religion 1", # 1hr 30 mins working, 5 mins reading
                "Studies of Religion 2", # 3hrs working, 5 mins reading
                "Swedish Continuers", # 2hrs 30 mins working, 10 mins reading
                "Textiles and Design", # 1hr 30 mins working, 5 mins reading
                "Tourism, Travel and Events", # 2hrs working, 5 mins reading
                "Vietnamese Continuers", # 2hrs 50 mins working, 10 mins reading
                "Visual Arts", # 1hr 30 mins working, 5 mins reading
            ]

            clicked = StringVar()
            clicked2 = StringVar()
            clicked3 = StringVar()
            clicked4 = StringVar() 

            clicked.set("<< Select an Option >>")
            clicked2.set("<< Select an Option >>")
            clicked3.set("<< Select an Option >>")
            clicked4.set("<< Select an Option >>")

            dropdown_width = len(max(Stage_6_Subjects, key=len))

            def selected_num_of_exams():
                class Examination():
                    pass
                
            def num_of_exams():
                if check_box_variable.get() == 1:
                    two.place(relx=0.35, rely=0.15, anchor = E)
                    three.place(relx=0.5, rely=0.15, anchor = CENTER)
                    four.place(relx=0.65, rely=0.15, anchor = W)
                else:
                    two.place_forget()
                    three.place_forget()
                    four.place_forget()
                    second_dropdown.place_forget()
                    third_dropdown.place_forget()
                    fourth_dropdown.place_forget()

            def place_exams():
                    if var.get() == 1:
                        second_dropdown.place(relx=0.5, rely=0.4, anchor="center")
                        third_dropdown.place_forget()
                        fourth_dropdown.place_forget()
                    elif var.get() == 2:
                        second_dropdown.place(relx=0.5, rely=0.4, anchor="center")
                        third_dropdown.place(relx=0.5, rely=0.5, anchor="center")
                        fourth_dropdown.place_forget()
                    elif var.get() == 3:
                        second_dropdown.place(relx=0.5, rely=0.4, anchor="center")
                        third_dropdown.place(relx=0.5, rely=0.5, anchor="center")
                        fourth_dropdown.place(relx=0.5, rely=0.6, anchor="center")
                    else:
                        second_dropdown.place_forget()
                        third_dropdown.place_forget()
                        fourth_dropdown.place_forget()

            var = IntVar()
            two = Radiobutton(settings_canvas, text="Two Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=var, value=1, command=place_exams)
            three = Radiobutton(settings_canvas, text="Three Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=var, value=2, command=place_exams)
            four = Radiobutton(settings_canvas, text="Four Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=var, value=3, command=place_exams)

            check_box_variable = IntVar()
            multiple_exams_checkbox = tk.Checkbutton(settings_canvas, text='Multiple Exams', font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=check_box_variable, onvalue=1, offvalue=0, command=num_of_exams)
            multiple_exams_checkbox.place(relx=0.5, rely=0.1, anchor="center")

            dropdown = OptionMenu(settings_canvas, clicked, *Stage_6_Subjects)
            dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            dropdown.place(relx=0.5, rely=0.2, anchor="center")

            # Create button, it will change label text 
            button = Button(settings_canvas , text = "Confirm", font=("Helvetica Bold", 20), bg="light grey", border=0, command = show)
            button.place(relx=0.1, rely=0.25, anchor="w")

            second_dropdown = OptionMenu(settings_canvas, clicked2, *Stage_6_Subjects)
            second_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            third_dropdown = OptionMenu(settings_canvas, clicked3, *Stage_6_Subjects)
            third_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            
            fourth_dropdown = OptionMenu(settings_canvas, clicked4, *Stage_6_Subjects)
            fourth_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            # Create Label 
            selected_subject = Label(settings_canvas , text = " ",  font=("Helvetica Bold", 20), bg="light grey", fg="black") 
            selected_subject.place(relx=0.3, rely=0.25, anchor="w")
            
        # The settings is where the exam supervisor can change the different exams taking place,
        # and the time for each exam. There will be no interactable widgets on the main display,
        # except for the settings button itself, + exam timer controls (start, stop, clear, etc.)
        self.settings_button = tk.Button(self.main_canvas, image=button_image, borderwidth=0, command=open_settings)
        self.settings_button.place(relx=0.975, rely=0.043, anchor="ne")

        # Placeholder Stuff for Exam Timer and Subject Info
        self.labelframe = tk.LabelFrame(self.main_canvas, text="Examination Details", font=('Helvetica Bold', 20), width=1000, height=100, fg="black", bg="white", borderwidth=6)
        self.labelframe.place(relx=0.5, rely=0.5, anchor="w")

        # Variable Names Below Are Temorary, just to simulate multiple exams
        self.labelframe_text1 = tk.Label(self.labelframe, text="Subject/Exam Details Will Go Here eeeeeeeeeeeeeeee", font=('Helvetica Bold', 20), fg="black", bg="white")
        self.labelframe_text1.pack(padx=15, pady=50)

        self.labelframe_text2 = tk.Label(self.labelframe, text="Subject/Exam Details Will Go Here eeeeeeeeeeeeeeee", font=('Helvetica Bold', 20), fg="black", bg="white")
        self.labelframe_text2.pack(padx=15, pady=50)

        self.labelframe_text3 = tk.Label(self.labelframe, text="Subject/Exam Details Will Go Here eeeeeeeeeeeeeeee", font=('Helvetica Bold', 20), fg="black", bg="white")
        self.labelframe_text3.pack(padx=15, pady=50)

        self.labelframe_text4 = tk.Label(self.labelframe, text="Subject/Exam Details Will Go Here eeeeeeeeeeeeeeee", font=('Helvetica Bold', 20), fg="black", bg="white")
        self.labelframe_text4.pack(padx=15, pady=50)

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

                # Draw Clock Face using tkinter-imbedded oval tool
                self.main_canvas.create_oval(140, 80, 570, 510, outline="black" , width=8)
                self.main_canvas.create_oval(150, 90, 560, 500, outline="lavender", width=5)
                self.main_canvas.create_oval(350, 290, 360, 300, fill="black")
                # self.main_canvas.create_oval(x0, y0, x1, y1, details ->...)

                # Draw numbers on the clock face
                for i in range(1, 13):
                    angle = math.radians(i * 30) # 360 (degrees) / 12 (unique hours) = 30 (degrees per hour)

                    # the below code generates the x and y coordinates for where the number/text will be placed:
                    # for the clock, we are using the sin/cosine maths functions which refers to the UNIT CIRCLE
                    x = 355 + 180 * math.sin(angle)
                    y = 295 - 180 * math.cos(angle)

                    # Draw the numbers using tkinter text tool
                    self.main_canvas.create_text(x, y, text=str(i), font=("Helvetica", 25, "bold"), fill="black")
                    # text=str(i) auto-fills the textbox with the number (1,2,3,...,12) as the for loop operates

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
                        # edit these numbers to make them not slightly goofy??
                        x1 = 355 + 213 * math.sin(angle)
                        y1 = 295 - 213 * math.cos(angle)
                        x2 = 355 + 205 * math.sin(angle)
                        y2 = 295 - 205 * math.cos(angle)
                        self.main_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")

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
ClockwiseScholar()