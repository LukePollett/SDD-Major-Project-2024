# Implemented Python Libraries:
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from PIL import Image,ImageTk
import math

# Invigilation Software for the HSC

# Create the main class for the ExamTimer
class BetterHSCTimer():

    # Initializing the main window
    def __init__(self):

        # Defining Main Window
        self.root = tk.Tk()
        self.root.title("BetterHSCTimer - Examination Management and Timing")

        # Making the window zoom to fit screen (not fullscreen, but maximized)
        width = self.root.winfo_screenwidth() # MacBook Resolution = 1440 x 900
        height = self.root.winfo_screenheight()
        self.root.state('zoomed')
        self.root.geometry("%dx%d" % (width, height))

        # Create the canvas for the main window
        self.main_canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.main_canvas.pack(side=tk.LEFT)

        # Create the settings button
        temp_img = Image.open("menu.png")
        resized_bg = temp_img.resize((75, 75))
        button_image = ImageTk.PhotoImage(resized_bg)

        def open_settings():   
            # get main window position
            root_x = self.root.winfo_rootx()
            root_y = self.root.winfo_rooty()

            # add offset
            win_x = root_x + 704
            win_y = root_y + 10

            settings_window = tk.Toplevel()
            settings_window.geometry("700x700")
            settings_window.geometry(f'+{win_x}+{win_y}')  

            settings_window.wm_attributes('-topmost', 'True')
            settings_window.overrideredirect(True)

            settings_canvas = tk.Canvas(settings_window, width=700, height=700, bg="light grey")
            settings_canvas.pack()
            
            back_btn = tk.Button(settings_canvas, text="X", font=('Helvetica Bold', 50), width=2, height=1, bg="white", fg="black", command=settings_window.destroy)
            back_btn.place(relx=1, rely=0, anchor="ne")

            """
            ISSUE: When pressing the confirm button, nothing is stopping the user from pressing it multiple times,
            meaning that they can essentially add the same exam to the exam_total_length, exam_working, and exam_reading lists
            over and over and over again.

            I tried solving this by adding the PRESS_COUNT seen above/below, but this didnt work because if
            the user wanted to switch from just one exam to 4 exams after they'd already pressed confirm,
            it just wouldn't let them press it again.

            This is the software equivalent to a softlock in video games.
            """



            """
            ============================ STUFF I GOTTA DO ============================
            - Add a check to see if the user has already pressed the confirm button (and if they have, don't let them press it again, unless they've changed the number of exams they're managing)
            - Add a check to see if the user has selected the same exam multiple times (OPTIONAL)
            - GET THE TIMER TO ACTUALLY COUNT DOWN
                - MAKE THE BUTTONS WORK
            - Format the timer to make it obvious when the reading time is over
            =========================================================================

            """

            global CLICKED1, CLICKED2, CLICKED3, CLICKED4
            CLICKED1 = StringVar()
            CLICKED2 = StringVar()
            CLICKED3 = StringVar()
            CLICKED4 = StringVar() 

            global TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4
            TIME_VAR_1=StringVar()
            TIME_VAR_2=StringVar()
            TIME_VAR_3=StringVar()
            TIME_VAR_4=StringVar()

            def show():
                # global PRESS_COUNT
                # PRESS_COUNT += 1
                # if PRESS_COUNT <= 1:
                    if VAR.get() == 0:
                        if CLICKED1.get()== "<< Select a Subject >>": 
                            messagebox.showerror('Exam Selection Error', 'Error: Please Select At Least One Valid Subject')
                        else:
                            clicked_var = 0
                            get_exam_times(clicked_var)

                    elif VAR.get() == 1:
                        if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>": 
                            messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
                        else:
                            clicked_var = 1
                            get_exam_times(clicked_var)

                    elif VAR.get() == 2:
                        if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>" or CLICKED3.get()== "<< Select a Subject >>": 
                            messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
                        else:
                            clicked_var = 2
                            get_exam_times(clicked_var)

                    elif VAR.get() == 3:
                        if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>" or CLICKED3.get()== "<< Select a Subject >>" or CLICKED4.get()== "<< Select a Subject >>": 
                            messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
                        else:
                            clicked_var = 3
                            get_exam_times(clicked_var)

                # else:
                #     messagebox.showerror('Exam Selection Error', 'Error: Please Only Press The Confirm Button Once')

            exam_names = []
            exam_clocks = []
            exam_total_length = []
            exam_working = []
            exam_reading = []

            time_var_list = [TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4]
            clicked_var_list = [CLICKED1, CLICKED2, CLICKED3, CLICKED4]

            def get_exam_times(clicked_var):
                i = 0
                while i <= clicked_var:
                    index = Stage_6_Subjects.index(str(clicked_var_list[i].get()))
                    exam_names.append(str(clicked_var_list[i].get()))
                    
                    working_time = str(Exam_working_times[index])
                    hr, min, sec = working_time.split(":")
                    working_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
                    exam_working.append(working_seconds)

                    reading_time = str(Exam_reading_times[index])
                    hr, min, sec = reading_time.split(":")
                    reading_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
                    exam_reading.append(reading_seconds)

                    total_time = working_seconds + reading_seconds
                    
                    global NEW_STRING
                    NEW_STRING = f"{(total_time // 3600) % 3600:02}:{(total_time // 60) % 60:02}:{total_time % 60:02}"
                    exam_clocks.append(NEW_STRING)
                    
                    exam_total_length.append(total_time)

                    def transfer_subjects ():
                        j = 0

                        while j <= (len(time_var_list) - 1):
                            string = time_var_list[j].get()

                            if len(string) == 8 and string[:2].isdigit() and string[3:5].isdigit() and string[6:].isdigit() and string[2] == ":" and string[5] == ":":
                                if clicked_var_list[j].get() == "<< Select a Subject >>":
                                        break
                                        
                                else:
                                    ExamFrames()
                            else:
                                messagebox.showerror('Exam Selection Error', 'Error: Please Enter A Valid Exam Time In The Format "HH:MM:SS"')
                                break
                            
                            j += 1
                        
                        start_btn.place(relx=0.67, rely=0.89, anchor="center")

                    transfer_subjects()


                    ########### EXAMS ARENT BEING PUT ON CORRECTLY
                    if i == 0:
                        TIME_VAR_1.set(NEW_STRING)
                    elif i == 1:
                        TIME_VAR_2.set(NEW_STRING)
                    elif i == 2:
                        TIME_VAR_3.set(NEW_STRING)
                    elif i == 3:
                        TIME_VAR_4.set(NEW_STRING)
                
                    i += 1

                # longest_exam_length = max(exam_total_length)
                # LONGEST_EXAM_STRING = "{:02}:{:02}:{:02}".format((longest_exam_length // 3600) % 3600, (longest_exam_length // 60) % 60, longest_exam_length % 60)

                first_timeEntry.config(state="normal")
                second_timeEntry.config(state="normal")
                third_timeEntry.config(state="normal")
                fourth_timeEntry.config(state="normal")

            # ======================Getting HSC Subjects==================================

            def get_subjects():
                global Stage_6_Subjects, Exam_working_times, Exam_reading_times
                with open("HSC Subjects", "r") as subjects:
                    lines = subjects.readlines()

                Stage_6_Subjects = []

                for l in lines:
                    list1 = l.split(", ")
                    Stage_6_Subjects.append(list1[0].replace("\n", ""))

                # ======================Getting Exam Working Times============================

                with open("Exam Working Times", "r") as working_times:
                    lines = working_times.readlines()

                Exam_working_times = []

                for l in lines:
                    list2 = l.split(", ")
                    Exam_working_times.append(list2[0].replace("\n", ""))
                
                # ======================Getting Exam Reading Times============================

                with open("Exam Reading Times", "r") as reading_times:
                    lines = reading_times.readlines()

                Exam_reading_times = []
                        
                for l in lines:
                    list3 = l.split(", ")
                    Exam_reading_times.append(list3[0].replace("\n", ""))

            get_subjects()

            # ========================================================

            CLICKED1.set("<< Select a Subject >>")
            CLICKED2.set("<< Select a Subject >>")
            CLICKED3.set("<< Select a Subject >>")
            CLICKED4.set("<< Select a Subject >>")

            dropdown_width = len(max(Stage_6_Subjects, key=len))
                
            def num_of_exams():
                if check_box_variable.get() == 1:
                    two.place(relx=0.35, rely=0.15, anchor = E)
                    three.place(relx=0.5, rely=0.15, anchor = CENTER)
                    four.place(relx=0.65, rely=0.15, anchor = W)
                else:
                    VAR.set(0)
                    two.place_forget()
                    three.place_forget()
                    four.place_forget()
                    second_dropdown.config(state="disabled")
                    third_dropdown.config(state="disabled")
                    fourth_dropdown.config(state="disabled")

            def place_exams():
                if VAR.get() == 1:
                    second_dropdown.config(state="normal")
                    third_dropdown.config(state="disabled")
                    fourth_dropdown.config(state="disabled")
                
                elif VAR.get() == 2:
                    second_dropdown.config(state="normal")
                    third_dropdown.config(state="normal")
                    fourth_dropdown.config(state="disabled")
             
                elif VAR.get() == 3:
                    second_dropdown.config(state="normal")
                    third_dropdown.config(state="normal")
                    fourth_dropdown.config(state="normal")
              
                else:
                    second_dropdown.config(state="disabled")
                    third_dropdown.config(state="disabled")
                    fourth_dropdown.config(state="disabled")

            global VAR
            VAR = IntVar()
            two = Radiobutton(settings_canvas, text="Two Exams", font=("Helvetica Bold", 20), bg="light grey", 
                              fg="black", variable=VAR, value=1, command=place_exams)
            three = Radiobutton(settings_canvas, text="Three Exams", font=("Helvetica Bold", 20), bg="light grey", 
                                fg="black", variable=VAR, value=2, command=place_exams)
            four = Radiobutton(settings_canvas, text="Four Exams", font=("Helvetica Bold", 20), bg="light grey", 
                               fg="black", variable=VAR, value=3, command=place_exams)

            check_box_variable = IntVar()
            multiple_exams_checkbox = tk.Checkbutton(settings_canvas, text='Multiple Exams', font=("Helvetica Bold", 20), 
                                                     bg="light grey", fg="black", variable=check_box_variable, onvalue=1, 
                                                     offvalue=0, command=num_of_exams)
            multiple_exams_checkbox.place(relx=0.5, rely=0.1, anchor="center")

            first_dropdown = OptionMenu(settings_canvas, CLICKED1, *Stage_6_Subjects)
            first_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            first_dropdown.place(relx=0.1, rely=0.2, anchor="w")

            # Create button, it will change label text 
            conf_button = Button(settings_canvas , text = "Confirm Subject Choices", font=("Helvetica Bold", 30), bg="light grey", border=0, command = show)
            conf_button.place(relx=0.5, rely=0.9, anchor="center")

            second_dropdown = OptionMenu(settings_canvas, CLICKED2, *Stage_6_Subjects)
            second_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            third_dropdown = OptionMenu(settings_canvas, CLICKED3, *Stage_6_Subjects)
            third_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            
            fourth_dropdown = OptionMenu(settings_canvas, CLICKED4, *Stage_6_Subjects)
            fourth_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            second_dropdown.place(relx=0.1, rely=0.375, anchor="w")
            third_dropdown.place(relx=0.1, rely=0.55, anchor="w")
            fourth_dropdown.place(relx=0.1, rely=0.725, anchor="w")

            second_dropdown.config(state="disabled")
            third_dropdown.config(state="disabled")
            fourth_dropdown.config(state="disabled")

            TIME_VAR_1.set("00:00:00")
            TIME_VAR_2.set("00:00:00")
            TIME_VAR_3.set("00:00:00")
            TIME_VAR_4.set("00:00:00")

            first_timeLabel = Label(settings_canvas, text="Examination Length:", font=("Helvetica Bold", 20), 
                              bg="light grey", fg="black")
            first_timeLabel.place(relx=0.1, rely=0.25, anchor="w")

            first_timeEntry= Entry(settings_canvas, width=9, font=("Arial",18,""),
                                textvariable=TIME_VAR_1, bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
            first_timeEntry.place(relx=0.4, rely=0.25, anchor="w")

            second_timeLabel = Label(settings_canvas, text="Examination Length:", font=("Helvetica Bold", 20), 
                              bg="light grey", fg="black")
            second_timeLabel.place(relx=0.1, rely=0.425, anchor="w")

            second_timeEntry= Entry(settings_canvas, width=9, font=("Arial",18,""),
                                textvariable=TIME_VAR_2, bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
            second_timeEntry.place(relx=0.4, rely=0.425, anchor="w")

            third_timeLabel = Label(settings_canvas, text="Examination Length:", font=("Helvetica Bold", 20), 
                              bg="light grey", fg="black")
            third_timeLabel.place(relx=0.1, rely=0.6, anchor="w")

            third_timeEntry= Entry(settings_canvas, width=9, font=("Arial",18,""),
                                textvariable=TIME_VAR_3, bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
            third_timeEntry.place(relx=0.4, rely=0.6, anchor="w")

            fourth_timeLabel = Label(settings_canvas, text="Examination Length:", font=("Helvetica Bold", 20), 
                              bg="light grey", fg="black")
            fourth_timeLabel.place(relx=0.1, rely=0.775, anchor="w")

            fourth_timeEntry= Entry(settings_canvas, width=9, font=("Arial",18,""),
                                textvariable=TIME_VAR_4, bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
            fourth_timeEntry.place(relx=0.4, rely=0.775, anchor="w")

        labelframe = tk.LabelFrame(self.main_canvas, text="Examinations", font=('Helvetica Bold', 20), 
                                   width=600, height=700, fg="black", bg="white", borderwidth=6)
        labelframe.place(relx=0.67, rely=0.433, anchor="center")
        labelframe.pack_propagate(False)

        class ExamFrames():
            def __init__(self):
                for widget in labelframe.winfo_children():
                    widget.destroy()
                if VAR.get() == 0:
                    self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get())

                elif VAR.get() == 1:
                    self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get())
                    self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get())

                elif VAR.get() == 2:
                    self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get())
                    self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get())
                    self.create_exam_frames("Exam #3", str(CLICKED3.get()), TIME_VAR_3.get())

                elif VAR.get() == 3:
                    self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get())
                    self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get())
                    self.create_exam_frames("Exam #3", str(CLICKED3.get()), TIME_VAR_3.get())
                    self.create_exam_frames("Exam #4", str(CLICKED4.get()), TIME_VAR_4.get())
        
            def create_exam_frames(self, frame_text, label_text, timer_text):
                exam_frame = tk.LabelFrame(labelframe, text=frame_text, font=('Helvetica Bold', 17), fg="black", bg="white", width = 540, height = 125,borderwidth=0, foreground="gray63")
                exam_frame.pack(pady=20)
                exam_frame.grid_propagate(False)

                # Automatically add a label to the labelframe
                label = Label(exam_frame, text=label_text, font=('Helvetica Bold', 25), bg="white", fg="black",)# width=len(max(Stage_6_Subjects, key=len)))
                label.grid(row=0, column=0, padx=10, pady=5, sticky="w", columnspan=3)

                time_remaining = Label(exam_frame, text="Time Remaining:", font=('Helvetica Bold', 20), bg="white", fg="gray")
                time_remaining.grid(row=1, column=0, padx=10, pady=5, sticky="w")

                timer = Label(exam_frame, text=timer_text, font=('Helvetica Bold', 30), bg="white", fg="black", width=9, borderwidth=5, relief="groove")
                timer.grid(row=1, column=1, padx=15, pady=5, sticky="w")

                ########## ADD PAUSE BUTTON FOR EACH SUBJECT?????

        def start_exam():
            start_btn.place_forget()
            end_btn.place(relx=0.67, rely=0.89, anchor="center")

        start_btn = Button(self.root , text = "Begin Exams", font=("Helvetica Bold", 40), bg="light grey", border=0, width=10, command = start_exam)
        end_btn = Button(self.root , text = "End All Exams", font=("Helvetica Bold", 40), bg="light grey", border=0, width=12, command=None)

        # The settings is where the exam supervisor can change the different exams taking place,
        # and the time for each exam. There will be no interactable widgets on the main display,
        # except for the settings button itself, + exam timer controls (start, stop, clear, etc.)
        self.settings_button = tk.Button(self.main_canvas, image=button_image, borderwidth=0, command=open_settings)
        self.settings_button.place(relx=0.975, rely=0.043, anchor="ne")

        clock_frame = tk.Frame(self.main_canvas, width=550, height=500, bg="white")
        clock_frame.place(relx=0.213, rely=0.37, anchor="center")
            
        frame_canvas = tk.Canvas(clock_frame, width=600, height=600, bg="white")
        frame_canvas.place(relx=0.5, rely=0.5, anchor="center") 

        # Create the digital clock display
        digi_clock_display = tk.Label(self.main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                        fg="black", borderwidth=10, relief="groove")
        digi_clock_display.place(relx=0.245, rely=0.75, anchor="n")  

        # Draw Clock Face using tkinter-imbedded oval tool
        frame_canvas.create_oval(140, 80, 570, 510, outline="black" , width=8)
        frame_canvas.create_oval(150, 90, 560, 500, outline="lavender", width=5)
        frame_canvas.create_oval(350, 290, 360, 300, fill="black")
        # self.main_canvas.create_oval(x0, y0, x1, y1, details ->...)

        # Draw numbers on the clock face
        for i in range(1, 13):
            angle = math.radians(i * 30) # 360 (degrees) / 12 (unique hours) = 30 (degrees per hour)

            # the below code generates the x and y coordinates for where the number/text will be placed:
            # for the clock, we are using the sin/cosine maths functions which refers to the UNIT CIRCLE
            x = 355 + 180 * math.sin(angle)
            y = 295 - 180 * math.cos(angle)

            # Draw the numbers using tkinter text tool
            frame_canvas.create_text(x, y, text=str(i), font=("Helvetica", 25, "bold"), fill="black")
            # text=str(i) auto-fills the textbox with the number (1,2,3,...,12) as the for loop operates

        # Draw notches
        for i in range(60):
            if i % 5 == 0:
                angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
                x1 = 355 + 215 * math.sin(angle)
                y1 = 295 - 215 * math.cos(angle)
                x2 = 355 + 195 * math.sin(angle)
                y2 = 295 - 195 * math.cos(angle)
                frame_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
                
            else:
                angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
                # edit these numbers to make them not slightly goofy??
                x1 = 355 + 213 * math.sin(angle)
                y1 = 295 - 213 * math.cos(angle)
                x2 = 355 + 205 * math.sin(angle)
                y2 = 295 - 205 * math.cos(angle)
                frame_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")

        def draw_clocks():

            # Remove the previous sets of hands
            frame_canvas.delete("hand")

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

            # Draw The Hands:
            hour_x = 355 + 120 * math.sin(hour_angle)
            hour_y = 295 - 120 * math.cos(hour_angle)
            frame_canvas.create_line(355, 295, hour_x, hour_y, fill="black", width=8, tags=("hand",))

            minute_x = 355 + 150 * math.sin(minute_angle)
            minute_y = 295 - 150 * math.cos(minute_angle)
            frame_canvas.create_line(355, 295, minute_x, minute_y, fill="black", width=4, tags=("hand",))

            second_x = 355 + 165 * math.sin(second_angle)
            second_y = 295 - 165 * math.cos(second_angle)
            frame_canvas.create_line(355, 295, second_x, second_y, fill="red", width=2, tags=("hand",))

            # Get the current time
            current_time = time.strftime('%I:%M:%S %p')
            # %I auto-converts to 12-hour time
            # %M is minutes, %S is seconds, %p is AM/PM

            # Update the clock display with new time
            digi_clock_display.config(text=current_time)

            # Update the clock every 1000 ms (1 second)
            frame_canvas.after(1000, draw_clocks)

        draw_clocks()

        # Run the main window
        self.root.mainloop()

# Run the program through the class 'BetterHSCTimer'
BetterHSCTimer()