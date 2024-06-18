# Implemented Python Libraries:
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from PIL import Image,ImageTk
import math

# Invigilation Software for the HSC (+ maybs other exams)

# Create the main class for the ExamTimer
class BetterHSCTimer(tk.Tk):

    # Initializing the main window
    def __init__(self):

        # Window Properties
        self.root = tk.Tk()

        # Making the window fullscreen (ish)
        width = self.root.winfo_screenwidth() # MacBook Resolution = 1440 x 900
        height = self.root.winfo_screenheight()
        self.root.state('zoomed')
        self.root.geometry("%dx%d" % (width, height))

        self.root.title("BetterHSCTimer - Examination Management and Timing")

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

            done_btn = tk.Button(settings_canvas, text="Done", font=('Helvetica Bold', 25), bg="white", fg="black", command=transfer_subjects)
            done_btn.place(relx=0.5, rely=0.9, anchor="center")

            # Check if the selected option is a valid subject and display the subject's exam timer on a label
            def show():
                if VAR.get() == 0:
                    if CLICKED1.get()== "<< Select a Subject >>": 
                        messagebox.showerror('Exam Selection Error', 'Error: Please Select At Least One Valid Subject')
                    else:
                        temp = 0
                        get_exam_times(temp)
                elif VAR.get() == 1:
                    if CLICKED1.get() or CLICKED2.get()== "<< Select a Subject >>": 
                        messagebox.showerror('Exam Selection Error', 'Error: Please Select Valid Subjects')
                    else:
                        temp = 1
                        get_exam_times(temp)
                elif VAR.get() == 2:
                    if CLICKED1.get() or CLICKED2.get() or CLICKED3.get()== "<< Select a Subject >>": 
                        messagebox.showerror('Exam Selection Error', 'Error: Please Select Valid Subjects')
                    else:
                        temp = 2
                        get_exam_times(temp)
                elif VAR.get() == 3:
                    if CLICKED1.get() or CLICKED2.get() or CLICKED3.get() or CLICKED4.get()== "<< Select a Subject >>": 
                        messagebox.showerror('Exam Selection Error', 'Error: Please Select Valid Subjects')
                    else:
                        temp = 3
                        get_exam_times(temp)

            # TURN THE THINGO BELOW INTO A DEF FUNCTION WITH PARAMETERS OF CLICKED1, CLICKED2, CLICKED3, CLICKED4
            # if CLICKED1...if CLICKED2... etc.
            #   def_function(CLICKED1/CLICKED2)
            # PUT ALL OUTPUT RESULTS (NEWSTRING) INTO A LIST/LISTS (separate reading and writing time?)
            exam_string_list = []

            def get_exam_times(clicked_var):
                clicked_var_list = [CLICKED1, CLICKED2, CLICKED3, CLICKED4]
                i = 0
                while i <= clicked_var:
                    # variable = clicked_var_list[i]
                    index = Stage_6_Subjects.index(str(clicked_var_list[i].get()))
                    working_time = str(Exam_working_times[index])
                    working_minutes = int(working_time[3:5])

                    reading_time = str(Exam_reading_times[index])
                    reading_minutes = int(reading_time[3:5])

                    total = working_minutes + reading_minutes

                    global NEW_STRING
                    if total > 60:
                        NEW_STRING = working_time.replace(working_time[1], str((int(working_time[1]) + 1)), 1)
                        if len(str(total % 60)) == 2:
                            NEW_STRING = NEW_STRING.replace(NEW_STRING[3:5], str(total % 60), 1)

                    elif total == 60:
                        NEW_STRING = working_time.replace(working_time[1], str((int(working_time[1]) + 1)), 1)
                        NEW_STRING = NEW_STRING.replace(NEW_STRING[3:5], "00", 1)

                    else:
                        if len(str(total % 60)) == 2:
                            NEW_STRING = working_time.replace(working_time[3:5], str(total % 60), 1)
                        else:
                            NEW_STRING = working_time.replace(working_time[3:5], "0" + str(total % 60), 1)
                    
                    i += 1
                    exam_string_list.append(NEW_STRING)
                    print(exam_string_list)
                        
                    HOUR.set(NEW_STRING[:2])
                    MINUTE.set(NEW_STRING[3:5])
                    SECOND.set(NEW_STRING[6:8])

            # ======================Getting HSC Subjects==================================

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

            # ========================================================

            global CLICKED1, CLICKED2, CLICKED3, CLICKED4
            CLICKED1 = StringVar()
            CLICKED2 = StringVar()
            CLICKED3 = StringVar()
            CLICKED4 = StringVar() 

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
            two = Radiobutton(settings_canvas, text="Two Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=VAR, value=1, command=place_exams)
            three = Radiobutton(settings_canvas, text="Three Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=VAR, value=2, command=place_exams)
            four = Radiobutton(settings_canvas, text="Four Exams", font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=VAR, value=3, command=place_exams)

            check_box_variable = IntVar()
            multiple_exams_checkbox = tk.Checkbutton(settings_canvas, text='Multiple Exams', font=("Helvetica Bold", 20), bg="light grey", fg="black", variable=check_box_variable, onvalue=1, offvalue=0, command=num_of_exams)
            multiple_exams_checkbox.place(relx=0.5, rely=0.1, anchor="center")

            dropdown = OptionMenu(settings_canvas, CLICKED1, *Stage_6_Subjects)
            dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            dropdown.place(relx=0.1, rely=0.2, anchor="w")

            # Create button, it will change label text 
            conf_button = Button(settings_canvas , text = "Confirm", font=("Helvetica Bold", 20), bg="light grey", border=0, command = show)
            conf_button.place(relx=0.77, rely=0.2, anchor="w")

            second_dropdown = OptionMenu(settings_canvas, CLICKED2, *Stage_6_Subjects)
            second_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            third_dropdown = OptionMenu(settings_canvas, CLICKED3, *Stage_6_Subjects)
            third_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
            
            fourth_dropdown = OptionMenu(settings_canvas, CLICKED4, *Stage_6_Subjects)
            fourth_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

            second_dropdown.place(relx=0.1, rely=0.4, anchor="w")
            third_dropdown.place(relx=0.1, rely=0.6, anchor="w")
            fourth_dropdown.place(relx=0.1, rely=0.8, anchor="w")

            second_dropdown.config(state="disabled")
            third_dropdown.config(state="disabled")
            fourth_dropdown.config(state="disabled")

            colons = Label(settings_canvas, width=10, font=("Arial", 32,""), 
                            text="    :      :    ", fg="black", bg="light grey")
            colons.place(relx=0.095, rely=0.25, anchor="w")

            global HOUR, MINUTE, SECOND
            HOUR=StringVar()
            MINUTE=StringVar()
            SECOND=StringVar()

            HOUR.set("00")
            MINUTE.set("00")
            SECOND.set("00")

            global hourEntry, minuteEntry, secondEntry
            hourEntry= Entry(settings_canvas, width=3, font=("Arial",18,""),
                                textvariable=HOUR, bg="white", fg="black", borderwidth=5, relief="groove")
            hourEntry.place(relx=0.1, rely=0.25, anchor="w")

            minuteEntry= Entry(settings_canvas, width=3, font=("Arial",18,""),
                                textvariable=MINUTE, bg="white", fg="black", borderwidth=5, relief="groove")
            minuteEntry.place(relx=0.19, rely=0.25, anchor="w")

            secondEntry= Entry(settings_canvas, width=3, font=("Arial",18,""),
                            textvariable=SECOND, bg="white", fg="black", borderwidth=5, relief="groove")
            secondEntry.place(relx=0.28, rely=0.25, anchor="w")

        labelframe = tk.LabelFrame(self.main_canvas, text="Examinations", font=('Helvetica Bold', 20), width=600, height=500, fg="black", bg="white", borderwidth=6)
        labelframe.place(relx=0.67, rely=0.33, anchor="center")
        labelframe.pack_propagate(False)

        class ExamFrames():
            def __init__(self):
                # if CLICKED1.get() == "<< Select a Subject >>":
                #     messagebox.showerror('Exam Selection Error', 'Error: Please Select At Least One Valid Subject')
                # else:
                    for widget in labelframe.winfo_children():
                        widget.destroy()
                    if VAR.get() == 0:
                        self.create_exam_frames("Exam #1", f"HSC {str(CLICKED1.get())}2024")

                    elif VAR.get() == 1:
                        self.create_exam_frames("Exam #1", f"HSC {str(CLICKED1.get())}2024")
                        self.create_exam_frames("Exam #2", f"HSC {str(CLICKED2.get())}2024")

                    elif VAR.get() == 2:
                        self.create_exam_frames("Exam #1", f"HSC {str(CLICKED1.get())}2024")
                        self.create_exam_frames("Exam #2", f"HSC {str(CLICKED2.get())}2024")
                        self.create_exam_frames("Exam #3", f"HSC {str(CLICKED3.get())}2024")

                    elif VAR.get() == 3:
                        self.create_exam_frames("Exam #1", f"HSC {str(CLICKED1.get())}2024")
                        self.create_exam_frames("Exam #2", f"HSC {str(CLICKED2.get())}2024")
                        self.create_exam_frames("Exam #3", f"HSC {str(CLICKED3.get())}2024")
                        self.create_exam_frames("Exam #4", f"HSC {str(CLICKED4.get())}2024")
        
            def create_exam_frames(self, frame_text, label_text):
                exam_frame = tk.LabelFrame(labelframe, text=frame_text, font=('Helvetica Bold', 17), fg="black", bg="white", borderwidth=0, foreground="gray63")
                exam_frame.pack(padx=10, pady=10)

                # Automatically add a label to the labelframe
                label = Label(exam_frame, text=label_text, font=('Helvetica Bold', 20), bg="white", fg="black", width=590)
                label.pack(pady=20)

        def transfer_subjects ():
            if CLICKED1.get() == "<< Select a Subject >>":
                    messagebox.showerror('Exam Selection Error', 'Error: Please Select At Least One Valid Subject')
            else:
                ExamFrames()
                config_timer()

        reading_time = 0

        working_time = 0

        paused = False

        def config_timer():
            # convert all CLICKED variables into a list, and use .max() function to find exam with longest time
            hr, min, sec = NEW_STRING.split(":")
            total_time = int(hr) * 3600 + int(min) * 60 + int(sec)
            exam_timer_lbl.config(text=f"{total_time//3600:02}:{(total_time//60)%60:02}:{total_time%60:02}")
            print(total_time)

        exam_timer_lbl = Label(self.root, text="00:00:00", font=('Helvetica Bold', 90), bg="white", fg="black", borderwidth=10, relief="groove")
        exam_timer_lbl.place(relx=0.67, rely=0.7, anchor="n")

        start_btn = Button(self.root , text = "Start", font=("Helvetica Bold", 30), bg="light grey", border=0, width=7, command = None)
        start_btn.place(relx=0.507, rely=0.89, anchor="w")

        pause_btn = Button(self.root , text = "Pause", font=("Helvetica Bold", 30), bg="light grey", border=0, width=7, command = None)
        pause_btn.place(relx=0.67, rely=0.89, anchor="center")

        clear_btn = Button(self.root , text = "Clear", font=("Helvetica Bold", 30), bg="light grey", border=0, width=7, command = None)
        clear_btn.place(relx=0.835, rely=0.89, anchor="e")

        # The settings is where the exam supervisor can change the different exams taking place,
        # and the time for each exam. There will be no interactable widgets on the main display,
        # except for the settings button itself, + exam timer controls (start, stop, clear, etc.)
        self.settings_button = tk.Button(self.main_canvas, image=button_image, borderwidth=0, command=open_settings)
        self.settings_button.place(relx=0.975, rely=0.043, anchor="ne")

        # Create analog clock face
        def Analog_Clock():      
        
            def draw_clock():

                clock_frame = tk.Frame(self.main_canvas, width=550, height=500, bg="white")
                clock_frame.place(relx=0.213, rely=0.37, anchor="center")
                
                frame_canvas = tk.Canvas(clock_frame, width=600, height=600, bg="white")
                frame_canvas.place(relx=0.5, rely=0.5, anchor="center")

                # Remove the previous sets of hands
                frame_canvas.delete("all")

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

                # Draw The Hands:
                hour_x = 355 + 120 * math.sin(hour_angle)
                hour_y = 295 - 120 * math.cos(hour_angle)
                frame_canvas.create_line(355, 295, hour_x, hour_y, fill="black", width=8)

                minute_x = 355 + 150 * math.sin(minute_angle)
                minute_y = 295 - 150 * math.cos(minute_angle)
                frame_canvas.create_line(355, 295, minute_x, minute_y, fill="black", width=4)

                second_x = 355 + 165 * math.sin(second_angle)
                second_y = 295 - 165 * math.cos(second_angle)
                frame_canvas.create_line(355, 295, second_x, second_y, fill="red", width=2)

                # Update the clock every 1000 ms (1 second)
                frame_canvas.after(1000, draw_clock)

            draw_clock()

        # Create the Digital Clock
        def Digital_Clock():

            # Create the digital clock display
            digi_clock_display = tk.Label(self.main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                              fg="black", borderwidth=10, relief="groove")
            digi_clock_display.place(relx=0.245, rely=0.75, anchor="n")

            # Get the current time
            current_time = time.strftime('%I:%M:%S %p')
            # %I auto-converts to 12-hour time
            # %M is minutes, %S is seconds, %p is AM/PM

            # Update the clock display with new time
            digi_clock_display.config(text=current_time)

            # Update the clock every 1000 ms (1 second)
            self.root.after(1000, Digital_Clock)

        # Create/Draw Both Clocks
        Analog_Clock()
        Digital_Clock()

        # Run the main window
        self.root.mainloop()

# Run the program through the class 'BetterHSCTimer'
if __name__ == "__main__":
    app = BetterHSCTimer()
    app.mainloop()

