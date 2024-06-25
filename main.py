# Implemented Python Libraries:
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from PIL import Image,ImageTk
import math
from datetime import datetime, timedelta

# Defining Main Window
root = tk.Tk()
root.title("BetterHSCTimer - Examination Management and Timing")

# Making the window zoom to fit screen (not fullscreen, but maximized)
width = root.winfo_screenwidth() # MacBook Resolution = 1440 x 900
height = root.winfo_screenheight()
root.state('zoomed')
root.geometry("%dx%d" % (width, height))

# Create the canvas for the main window
main_canvas = tk.Canvas(root, width=width, height=height, bg="white")
main_canvas.pack(side=tk.LEFT)

# Create the settings button
temp_img = Image.open("menu.png")
resized_bg = temp_img.resize((75, 75))
button_image = ImageTk.PhotoImage(resized_bg)

def settings_menu():   
    # get main window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()

    # add offset
    win_x = root_x + 675
    win_y = root_y + 10

    settings_window = tk.Toplevel()
    settings_window.geometry("730x700")
    settings_window.geometry(f'+{win_x}+{win_y}')  

    settings_window.wm_attributes('-topmost', 'True')
    settings_window.overrideredirect(True)

    settings_canvas = tk.Canvas(settings_window, width=730, height=700, bg="light grey")
    settings_canvas.pack()
    
    back_btn = tk.Button(settings_canvas, text="X", font=('Helvetica Bold', 50), width=2, height=1, bg="white", fg="black", command=settings_window.destroy)
    back_btn.place(relx=1, rely=0, anchor="ne")

    global CLICKED1, CLICKED2, CLICKED3, CLICKED4
    CLICKED1 = StringVar()
    CLICKED2 = StringVar()
    CLICKED3 = StringVar()
    CLICKED4 = StringVar() 

    global TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4
    TIME_VAR_1 = StringVar()
    TIME_VAR_2 = StringVar()
    TIME_VAR_3 = StringVar()
    TIME_VAR_4 = StringVar()

    def show():
        if VAR.get() == 0:
            if CLICKED1.get()== "<< Select a Subject >>": 
                messagebox.showerror('Exam Selection Error', 'Error: Please Select At Least One Valid Subject')
            else:
                clicked_var = 0
                get_exam_times(clicked_var)
                show_exam_times.place_forget()
                conf_button.place(relx=0.5, rely=0.9, anchor="center")

        elif VAR.get() == 1:
            if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>": 
                messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
            else:
                clicked_var = 1
                get_exam_times(clicked_var)
                show_exam_times.place_forget()
                conf_button.place(relx=0.5, rely=0.9, anchor="center")

        elif VAR.get() == 2:
            if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>" or CLICKED3.get()== "<< Select a Subject >>": 
                messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
            else:
                clicked_var = 2
                get_exam_times(clicked_var)
                show_exam_times.place_forget()
                conf_button.place(relx=0.5, rely=0.9, anchor="center")

        elif VAR.get() == 3:
            if CLICKED1.get()== "<< Select a Subject >>" or CLICKED2.get()== "<< Select a Subject >>" or CLICKED3.get()== "<< Select a Subject >>" or CLICKED4.get()== "<< Select a Subject >>": 
                messagebox.showerror('Exam Selection Error', 'Error: Please Ensure All Subjects Are Selected')
            else:
                clicked_var = 3
                get_exam_times(clicked_var)
                show_exam_times.place_forget()
                conf_button.place(relx=0.5, rely=0.9, anchor="center")

    global exam_total_length, exam_working, exam_reading
    exam_total_length = []
    exam_working = []
    exam_reading = []

    time_var_list = [TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4]
    clicked_var_list = [CLICKED1, CLICKED2, CLICKED3, CLICKED4]

    def get_exam_times(clicked_var):
        i = 0
        while i <= clicked_var:
            index = Stage_6_Subjects.index(str(clicked_var_list[i].get()))
            
            working_time = str(Exam_working_times[index])
            hr, min, sec = working_time.split(":")
            working_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
            exam_working.append(working_seconds)

            reading_time = str(Exam_reading_times[index])
            hr, min, sec = reading_time.split(":")
            reading_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
            exam_reading.append(reading_seconds)

            total = working_seconds + reading_seconds

            if len(exam_total_length) <= clicked_var:
                exam_total_length.append(total)
            
            global NEW_STRING
            NEW_STRING = f"{(total // 3600) % 3600:02}:{(total // 60) % 60:02}:{total % 60:02}"

            if i == 0:
                TIME_VAR_1.set(NEW_STRING)
            elif i == 1:
                TIME_VAR_2.set(NEW_STRING)
            elif i == 2:
                TIME_VAR_3.set(NEW_STRING)
            elif i == 3:
                TIME_VAR_4.set(NEW_STRING)

            ################ Exams start being transferred to main screen here ################
            j = 0
            while j <= clicked_var:
                string = time_var_list[j].get()

                if len(string) == 8 and string[:2].isdigit() and string[3:5].isdigit() and string[6:].isdigit() and string[2] == ":" and string[5] == ":":
                    if clicked_var_list[j].get() == "<< Select a Subject >>":
                            break
                    else:
                        ExamFrames(labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4)
                else:
                    messagebox.showerror('Exam Selection Error', 'Error: Please Enter A Valid Exam Time In The Format "HH:MM:SS"')
                    break
                
                j += 1
        
            i += 1

        clear_btn.place_forget()
        start_btn.place(relx=0.67, rely=0.89, anchor="center")

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
            exam_total_length.clear()
            second_dropdown.config(state="normal")
            third_dropdown.config(state="disabled")
            fourth_dropdown.config(state="disabled")
        
        elif VAR.get() == 2:
            exam_total_length.clear()
            second_dropdown.config(state="normal")
            third_dropdown.config(state="normal")
            fourth_dropdown.config(state="disabled")
        
        elif VAR.get() == 3:
            exam_total_length.clear()
            second_dropdown.config(state="normal")
            third_dropdown.config(state="normal")
            fourth_dropdown.config(state="normal")
        
        else:
            exam_total_length.clear()
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

    show_exam_times = Button(settings_canvas, text="Show Exam Times", font=("Helvetica Bold", 30), bg="light grey", fg="black", command=show)
    show_exam_times.place(relx=0.5, rely=0.9, anchor="center")    

    conf_button = Button(settings_canvas , text = "Confirm Subject Choices", font=("Helvetica Bold", 30), bg="light grey", border=0, command=settings_window.destroy)

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

    rely_positions = [0.25, 0.425, 0.6, 0.775]
    time_var_list = [TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4]

    def create_label_and_timer(canvas, label_text, entry_var, relx_label, rely_label, relx_entry, rely_entry):
        label = Label(canvas, text=label_text, font=("Helvetica Bold", 20), bg="light grey", fg="black")
        label.place(relx=relx_label, rely=rely_label, anchor="w")

        timer = Label(canvas, width=9, font=("Helvetica Bold", 25, "bold"), textvariable=entry_var, 
                    bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
        timer.place(relx=relx_entry, rely=rely_entry, anchor="w")

    # Create Exam Labels and Timer Displays
    for i in range(len(time_var_list)):
        create_label_and_timer(settings_canvas, "Examination Length:", time_var_list[i], relx_label=0.1, rely_label=rely_positions[i], relx_entry=0.4, rely_entry=rely_positions[i])  

labelframe = tk.LabelFrame(main_canvas, text="Examinations", font=('Helvetica Bold', 20), 
                            width=600, height=700, fg="black", bg="white", borderwidth=6)
labelframe.place(relx=0.67, rely=0.433, anchor="center")
labelframe.pack_propagate(False)

# timer_list = []

class ExamFrames():
    def __init__(self, labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4):
        self.timers = {}
        self.start_times = {}
        self.end_times = {}

        for widget in labelframe.winfo_children():
            widget.destroy()
        if VAR.get() == 0:
            self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get(), "Exam1")

        elif VAR.get() == 1:
            self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get(), "Exam1")
            self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get(), "Exam2")

        elif VAR.get() == 2:
            self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get(), "Exam1")
            self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get(), "Exam2")
            self.create_exam_frames("Exam #3", str(CLICKED3.get()), TIME_VAR_3.get(), "Exam3")

        elif VAR.get() == 3:
            self.create_exam_frames("Exam #1", str(CLICKED1.get()), TIME_VAR_1.get(), "Exam1")
            self.create_exam_frames("Exam #2", str(CLICKED2.get()), TIME_VAR_2.get(), "Exam2")
            self.create_exam_frames("Exam #3", str(CLICKED3.get()), TIME_VAR_3.get(), "Exam3")
            self.create_exam_frames("Exam #4", str(CLICKED4.get()), TIME_VAR_4.get(), "Exam4")

    def create_exam_frames(self, frame_text, label_text, timer_text, exam_key):
        exam_frame = tk.LabelFrame(labelframe, text=frame_text, font=('Helvetica Bold', 17), fg="black", bg="white", width = 540, height = 155,borderwidth=0, foreground="gray63")
        exam_frame.pack(pady=4)
        exam_frame.grid_propagate(False)

        # Automatically add a label to the labelframe
        label = Label(exam_frame, text=label_text, font=('Helvetica Bold', 25), bg="white", fg="black",) # width=len(max(Stage_6_Subjects, key=len)))
        label.grid(row=0, column=0, padx=10, pady=3, sticky="w", columnspan=3)

        time_remaining = Label(exam_frame, text="Time Remaining:", font=('Helvetica Bold', 20), bg="white", fg="black")
        time_remaining.grid(row=1, column=0, padx=10, pady=3, sticky="w")

        timer = Label(exam_frame, text=timer_text, font=('Helvetica Bold', 40), bg="white", fg="blue", width=9, borderwidth=5, relief="groove")
        timer.grid(row=1, column=1, padx=15, pady=2, sticky="w")

        start_time = Label(exam_frame, text=f"Start: ", font=('Helvetica Bold', 20), bg="white", fg="black")
        start_time.grid(row=2, column=0, padx=10, pady=3, sticky="w")

        end_time = Label(exam_frame, text=f"End: ", font=('Helvetica Bold', 20), bg="white", fg="black")
        end_time.grid(row=2, column=1, padx=10, pady=3, sticky="w")

        self.timers[exam_key] = timer
        self.start_times[exam_key] = start_time
        self.end_times[exam_key] = end_time

    def update_timers(self, exam_key, new_text, colour):
        if exam_key in self.timers:
            self.timers[exam_key].config(text="")
            self.timers[exam_key].config(text=new_text, fg=colour)
    
    def update_start_end_times(self, exam_key, time_now, end_of_exam):
        if exam_key in self.start_times:
            self.start_times[exam_key].config(text="")
            self.start_times[exam_key].config(text=f"Start: {time_now}")
            
        if exam_key in self.end_times:
            self.end_times[exam_key].config(text="")
            self.end_times[exam_key].config(text=f"End: {end_of_exam}")

def start_exam():
    start_btn.place_forget()
    clear_btn.place(relx=0.67, rely=0.89, anchor="center")
    global examination_frames, exam_key_list
    examination_frames = ExamFrames(labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4)
    exam_key_list = ["Exam1", "Exam2", "Exam3", "Exam4"]
    calculate_start_end_times()
    countdown_timer()

def update_exam_timers(exam_frames_instance, exam_key, new_text, colour):
    exam_frames_instance.update_timers(exam_key, new_text, colour)

def update_exam_info(exam_frames_instance, exam_key, time_now, end_of_exam):
    exam_frames_instance.update_start_end_times(exam_key, time_now, end_of_exam)

def calculate_start_end_times():
    i = 0
    while i < len(exam_total_length):
        current_time = datetime.now()
        time_after_exam = current_time + timedelta(hours=((exam_total_length[i] // 3600) % 3600), minutes=((exam_total_length[i] // 60) % 60), seconds=(exam_total_length[i] % 60))
        formatted_start_time = format(current_time, '%I:%M:%S %p')
        formatted_end_time = format(time_after_exam, '%I:%M:%S %p')
        update_exam_info(examination_frames, exam_key_list[i], formatted_start_time, formatted_end_time)
        i += 1

def countdown_timer():
    i = 0
    while i < len(exam_total_length):
        try:
            if exam_total_length[i] == "Stopped":
                return
            elif exam_total_length[i] > 0:
                exam_total_length[i] -= 1
                if exam_total_length[i] <= exam_working[i] and exam_total_length[i] > 0:
                    text_colour = "black"
                    update_exam_timers(examination_frames, exam_key_list[i], f"{(exam_total_length[i] // 3600) % 3600:02}:{(exam_total_length[i] // 60) % 60:02}:{exam_total_length[i] % 60:02}", text_colour)
                elif exam_total_length[i] == 0:
                    text_colour = "red"
                    update_exam_timers(examination_frames, exam_key_list[i], "Time's Up!", text_colour)
                else:
                    text_colour = "blue"
                    update_exam_timers(examination_frames, exam_key_list[i], f"{(exam_total_length[i] // 3600) % 3600:02}:{(exam_total_length[i] // 60) % 60:02}:{exam_total_length[i] % 60:02}", text_colour)
        except:
            break
            
        i += 1
        
    root.after(1000, countdown_timer)

def clear_exams():
    clear_btn.place_forget()
    for i in range(len(exam_total_length)):
        exam_total_length[i] = "Stopped"
    for widget in labelframe.winfo_children():
            widget.destroy()

start_btn = Button(root , text = "Begin Exams", font=("Helvetica Bold", 40), bg="light grey", border=0, width=10, command = start_exam)
clear_btn = Button(root , text = "Clear", font=("Helvetica Bold", 40), bg="light grey", border=0, width=10, command=clear_exams)

# The settings is where the exam supervisor can change the different exams taking place,
# and the time for each exam. There will be no interactable widgets on the main display,
# except for the settings button itself, + exam timer controls (start, stop, clear, etc.)
settings_button = tk.Button(main_canvas, image=button_image, borderwidth=0, command=settings_menu)
settings_button.place(relx=0.975, rely=0.043, anchor="ne")

clock_frame = tk.Frame(main_canvas, width=550, height=500, bg="white")
clock_frame.place(relx=0.213, rely=0.37, anchor="center")
    
frame_canvas = tk.Canvas(clock_frame, width=600, height=600, bg="white")
frame_canvas.place(relx=0.5, rely=0.5, anchor="center") 

# Create the digital clock display
digi_clock_display = tk.Label(main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                fg="black", borderwidth=10, relief="groove")
digi_clock_display.place(relx=0.245, rely=0.75, anchor="n")  

# Draw Clock Face using tkinter-imbedded oval tool
frame_canvas.create_oval(140, 80, 570, 510, outline="black" , width=8)
frame_canvas.create_oval(150, 90, 560, 500, outline="lavender", width=5)
frame_canvas.create_oval(350, 290, 360, 300, fill="black")
# main_canvas.create_oval(x0, y0, x1, y1, details ->...)

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
root.mainloop()