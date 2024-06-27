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

# setting the width and height of the application window to the user's devide resolutio
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.state('zoomed')
root.geometry("%dx%d" % (width, height))

# Main canvas for the application
main_canvas = tk.Canvas(root, width=width, height=height, bg="white")
main_canvas.pack(side=tk.LEFT)

# Make the settings button a menu icon
temp_img = Image.open("menu.png")
resized_bg = temp_img.resize((75, 75))
button_image = ImageTk.PhotoImage(resized_bg)

# Settings_Menu Function includes subject selection process, opens settings topview window
def settings_menu():   
    # Get main window position
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()

    # place the settings window at a specific point on the screen
    win_x = root_x + 675
    win_y = root_y + 10

    # definining the settings window
    settings_window = tk.Toplevel()
    settings_window.geometry("730x700")
    settings_window.geometry(f'+{win_x}+{win_y}')  

    settings_window.wm_attributes('-topmost', 'True')
    settings_window.overrideredirect(True)

    # canvas for settings widgets
    settings_canvas = tk.Canvas(settings_window, width=730, height=700, bg="light grey")
    settings_canvas.pack()
    
    # Button to exit the settings window
    back_btn = tk.Button(settings_canvas, text="X", font=('Helvetica Bold', 50), width=2, height=1, bg="white", fg="black", command=settings_window.destroy)
    back_btn.place(relx=1, rely=0, anchor="ne")

    # Variables below are associated with the NAME of the subject chosen
    global CLICKED1, CLICKED2, CLICKED3, CLICKED4
    CLICKED1 = StringVar()
    CLICKED2 = StringVar()
    CLICKED3 = StringVar()
    CLICKED4 = StringVar() 

    # Variables below are associated with the LENGTH of the chosen exam
    global TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4
    TIME_VAR_1 = StringVar()
    TIME_VAR_2 = StringVar()
    TIME_VAR_3 = StringVar()
    TIME_VAR_4 = StringVar()

    # show() is run When the user has chosen all of their subjects
    def show():
        # Immediately performs a check to see if all subjects have been selected based on how many they exams they chose
        # VAR is the value of the radio button(s) on the settings window
        # if a subject has been left blank (has the option '<< Select a Subject >>'), the application displays a popup error message box

        # if all of the exams chosen are valid, it then prepares the 'begin exams' button and calls the get_exam_times() 
        # function with the number of subjects the user chose as a parameter

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
    exam_total_length = [] # holds the TOTAL LENGTH of each selected exam, in SECONDS
    exam_working = [] # holds the WORKING time of each selected exam in SECONDS
    exam_reading = [] # holds the READING time of each selected exam in SECONDS

    # list of exam timer VALUES
    time_var_list = [TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4]

    # list of exam  NAMES
    clicked_var_list = [CLICKED1, CLICKED2, CLICKED3, CLICKED4]

    # get_exam_times(clicked_var) uses the number of exams the user has chosen as a parameter
    # the function loops through each subject and calculates its total time (working + reading) and adds it to the list exam_total_length
    # it then automatically updates a label on the settings window that displays that specific subject's exam length in the format "HH:MM"SS"
    def get_exam_times(clicked_var):
        i = 0
        # repeat until all exams have been processed
        while i <= clicked_var:
            # index is used to associate the subject name with their working and reading times
            index = Stage_6_Subjects.index(str(clicked_var_list[i].get()))
            
            # convert working time in format HH:MM:SS to an integer (seconds)
            working_time = str(Exam_working_times[index])
            hr, min, sec = working_time.split(":")
            working_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
            exam_working.append(working_seconds)

            # convert reading time in format HH:MM:SS to an integer (seconds)
            reading_time = str(Exam_reading_times[index])
            hr, min, sec = reading_time.split(":")
            reading_seconds = int(hr) * 3600 + int(min) * 60 + int(sec)
            exam_reading.append(reading_seconds)

            # calculates total time in the exam
            total = working_seconds + reading_seconds

            # adds the total time of that exam to a list (as long as the list isn't already too long)
            if len(exam_total_length) <= clicked_var:
                exam_total_length.append(total)
            
            # NEW_STRING converts total (integer in seconds) to the format "HH:MM:SS"
            global NEW_STRING
            NEW_STRING = f"{(total // 3600) % 3600:02}:{(total // 60) % 60:02}:{total % 60:02}"

            # automatically update the subject's exam label(s)
            if i == 0:
                TIME_VAR_1.set(NEW_STRING)
            elif i == 1:
                TIME_VAR_2.set(NEW_STRING)
            elif i == 2:
                TIME_VAR_3.set(NEW_STRING)
            elif i == 3:
                TIME_VAR_4.set(NEW_STRING)

            ################ Exams start being transferred to the main window here ################
            j = 0
            # loop through each subject
            while j <= clicked_var:
                string = time_var_list[j].get()
                
                # check if timer is in the right format
                # this is juts a failsafe in case a value in the text file(s) gets altered
                if len(string) == 8 and string[:2].isdigit() and string[3:5].isdigit() and string[6:].isdigit() and string[2] == ":" and string[5] == ":":
                    if clicked_var_list[j].get() == "<< Select a Subject >>":
                            break
                    else:
                        # add a new 'Examination' to the main window
                        ExamFrames(labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4)
                else:
                    messagebox.showerror('Exam Selection Error', 'Error: Please Enter A Valid Exam Time In The Format "HH:MM:SS"')
                    break
                
                j += 1
        
            i += 1

    # ======================Getting HSC Subjects==================================
    # reads the text file 'HSC Subjects' and adds all subjects to an array
    def get_subjects():
        global Stage_6_Subjects, Exam_working_times, Exam_reading_times
        with open("HSC Text Files/HSC Subjects", "r") as subjects:
            lines = subjects.readlines()

        Stage_6_Subjects = []

        for l in lines:
            list1 = l.split(", ")
            Stage_6_Subjects.append(list1[0].replace("\n", ""))

        # ======================Getting Exam Working Times============================
        # reads the text file 'HSC Subjects' and adds all subjects to an array
        with open("HSC Text Files/Exam Working Times", "r") as working_times:
            lines = working_times.readlines()

        Exam_working_times = []

        for l in lines:
            list2 = l.split(", ")
            Exam_working_times.append(list2[0].replace("\n", ""))
        
        # ======================Getting Exam Reading Times============================
        # reads the text file 'HSC Subjects' and adds all subjects to an array
        with open("HSC Text Files/Exam Reading Times", "r") as reading_times:
            lines = reading_times.readlines()

        Exam_reading_times = []
                
        for l in lines:
            list3 = l.split(", ")
            Exam_reading_times.append(list3[0].replace("\n", ""))

    get_subjects()

    # ========================================================

    # set the default value of all the dropdowns to "<< Select a Subject >>"
    CLICKED1.set("<< Select a Subject >>")
    CLICKED2.set("<< Select a Subject >>")
    CLICKED3.set("<< Select a Subject >>")
    CLICKED4.set("<< Select a Subject >>")

    # ensures all the names of the subjects can fit on the dropdown menu
    dropdown_width = len(max(Stage_6_Subjects, key=len))
        
    def num_of_exams():
        # check if the user has selected the option to have multiple exams
        # if they have, it reveals the radio buttons to let them choose how many EXTRA exams that want from 1 - 3
        if check_box_variable.get() == 1:
            two.place(relx=0.35, rely=0.15, anchor = E)
            three.place(relx=0.5, rely=0.15, anchor = CENTER)
            four.place(relx=0.65, rely=0.15, anchor = W)

        # if the user hasn't ticked multiple exam tickbox (i.e. they dont want multiple exams)
        # ^ it then disbales all dropdowns besides the first one
        else:
            VAR.set(0)
            two.place_forget()
            three.place_forget()
            four.place_forget()
            exam_total_length.clear()
            CLICKED1.set("<< Select a Subject >>")
            CLICKED2.set("<< Select a Subject >>")
            CLICKED3.set("<< Select a Subject >>")
            CLICKED4.set("<< Select a Subject >>")
            second_dropdown.config(state="disabled")
            third_dropdown.config(state="disabled")
            fourth_dropdown.config(state="disabled")

    # following def function determines how many exams the user selected and disables the subsequent dropdown menus
    def place_exams():
        # if the user changes their mind on how many exams they want, reset all of their choices
        exam_total_length.clear()
        CLICKED1.set("<< Select a Subject >>")
        CLICKED2.set("<< Select a Subject >>")
        CLICKED3.set("<< Select a Subject >>")
        CLICKED4.set("<< Select a Subject >>")

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

    # VAR is the value associated with the multiple exam radio buttons
    global VAR
    VAR = IntVar()

    # defining the radio buttons
    two = Radiobutton(settings_canvas, text="Two Exams", font=("Helvetica Bold", 20), bg="light grey", 
                        fg="black", variable=VAR, value=1, command=place_exams)
    three = Radiobutton(settings_canvas, text="Three Exams", font=("Helvetica Bold", 20), bg="light grey", 
                        fg="black", variable=VAR, value=2, command=place_exams)
    four = Radiobutton(settings_canvas, text="Four Exams", font=("Helvetica Bold", 20), bg="light grey", 
                        fg="black", variable=VAR, value=3, command=place_exams)

    # defining the multiple exam checkbox
    check_box_variable = IntVar()
    multiple_exams_checkbox = tk.Checkbutton(settings_canvas, text='Multiple Exams', font=("Helvetica Bold", 20), 
                                                bg="light grey", fg="black", variable=check_box_variable, onvalue=1, 
                                                offvalue=0, command=num_of_exams)
    multiple_exams_checkbox.place(relx=0.5, rely=0.1, anchor="center")

    # define and place the first subject dropdown manu
    first_dropdown = OptionMenu(settings_canvas, CLICKED1, *Stage_6_Subjects)
    first_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
    first_dropdown.place(relx=0.1, rely=0.2, anchor="w")

    # confirms the user's subject choices
    show_exam_times = Button(settings_canvas, text="Show Exam Times", font=("Helvetica Bold", 30), bg="light grey", fg="black", command=show)
    show_exam_times.place(relx=0.5, rely=0.9, anchor="center") 

    # once the user confirms the subjects it returns them to the main screen
    def confirm():
        settings_window.destroy()
        clear_btn.place_forget()
        start_btn.place(relx=0.67, rely=0.89, anchor="center")   

    # conf_button exits the settings window
    conf_button = Button(settings_canvas , text = "Confirm Subject Choices", font=("Helvetica Bold", 30), bg="light grey", border=0, command=confirm)

    # define and place the second subject dropdown manu
    second_dropdown = OptionMenu(settings_canvas, CLICKED2, *Stage_6_Subjects)
    second_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

    # define and place the third subject dropdown manu
    third_dropdown = OptionMenu(settings_canvas, CLICKED3, *Stage_6_Subjects)
    third_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")
    
    # define and place the fourth subject dropdown manu
    fourth_dropdown = OptionMenu(settings_canvas, CLICKED4, *Stage_6_Subjects)
    fourth_dropdown.config(width=dropdown_width, font=('Helvetica Bold', 20), bg="light grey", fg="black")

    # place all 3 of the additionaldropdowns
    second_dropdown.place(relx=0.1, rely=0.375, anchor="w")
    third_dropdown.place(relx=0.1, rely=0.55, anchor="w")
    fourth_dropdown.place(relx=0.1, rely=0.725, anchor="w")

    # ensure all 3 of the additionaldropdowns dropdowns start off disabled, as the user hasn't chosen multiple exams 
    second_dropdown.config(state="disabled")
    third_dropdown.config(state="disabled")
    fourth_dropdown.config(state="disabled")

    # set the default timer display for every subject dropdown to "00:00:00"
    TIME_VAR_1.set("00:00:00")
    TIME_VAR_2.set("00:00:00")
    TIME_VAR_3.set("00:00:00")
    TIME_VAR_4.set("00:00:00")

    # y coordinates references for placing subject timer labels
    rely_positions = [0.25, 0.425, 0.6, 0.775]
    time_var_list = [TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4]

    # create_label_and_timer() creates a timer label and associates titshe text with a variable
    def create_label_and_timer(canvas, label_text, entry_var, relx_label, rely_label, relx_entry, rely_entry):
        label = Label(canvas, text=label_text, font=("Helvetica Bold", 20), bg="light grey", fg="black")
        label.place(relx=relx_label, rely=rely_label, anchor="w")

        timer = Label(canvas, width=9, font=("Helvetica Bold", 25, "bold"), textvariable=entry_var, 
                    bg="white", fg="black", borderwidth=5, relief="groove", justify="center")
        timer.place(relx=relx_entry, rely=rely_entry, anchor="w")

    # Loop through all exams chosen and Create Exam Labels and Timer Displays 
    for i in range(len(time_var_list)):
        create_label_and_timer(settings_canvas, "Examination Length:", time_var_list[i], relx_label=0.1, rely_label=rely_positions[i], relx_entry=0.4, rely_entry=rely_positions[i])  

# labelframe is where all of the examination details are placed for when the actual exams start
labelframe = tk.LabelFrame(main_canvas, text="Examinations", font=('Helvetica Bold', 20), 
                            width=600, height=700, fg="black", bg="white", borderwidth=6)
labelframe.place(relx=0.67, rely=0.433, anchor="center")

# stop the labelframe from shrinking to the size of the widgets inside of it
labelframe.pack_propagate(False)

# class ExamFrames() creates an 'Exam Group' for EVERY SUBJECT chosen by the user
# Each 'Exam Group' consists of the name of the subject, the time remaining as well as the start and finish times of the exam
class ExamFrames():
    def __init__(self, labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4):
        self.timers = {}
        self.start_times = {}
        self.end_times = {}

        # if there are already exam groups in thee delete them and then add them from scratch (removes possibility for accidentally duplicating exam groups)
        for widget in labelframe.winfo_children():
            widget.destroy()

        # Get the amount of exams selected by the user and create appropriate amount of exam groups based on this
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

# create_exam_frames with the parameters: self, title of 'exam group', text to be displayed on the label (Subject name), 
#                                         text to displayed on the timer (Subject total time), unique label identifier (helps 
#                                         distinguish between labels as they were all created by the same class)
    # 
    def create_exam_frames(self, frame_text, label_text, timer_text, exam_key):
        
        # define the frame where all widgets will be placed in 'exam group'
        exam_frame = tk.LabelFrame(labelframe, text=frame_text, font=('Helvetica Bold', 17), fg="black", bg="white", width = 540, height = 155,borderwidth=0, foreground="gray63")
        exam_frame.pack(pady=4)
        exam_frame.grid_propagate(False)

        # Add the Subject Label to the exam frame
        label = Label(exam_frame, text=label_text, font=('Helvetica Bold', 25), bg="white", fg="black",) # width=len(max(Stage_6_Subjects, key=len)))
        label.grid(row=0, column=0, padx=10, pady=3, sticky="w", columnspan=3)

        time_remaining = Label(exam_frame, text="Time Remaining:", font=('Helvetica Bold', 20), bg="white", fg="black")
        time_remaining.grid(row=1, column=0, padx=10, pady=3, sticky="w")

        # Add the Subject's totla time (remaining) to the exam frame
        timer = Label(exam_frame, text=timer_text, font=('Helvetica Bold', 40), bg="white", fg="blue", width=9, borderwidth=5, relief="groove")
        timer.grid(row=1, column=1, padx=15, pady=2, sticky="w")

        # Add the Subject's exam start time to exam frame
        start_time = Label(exam_frame, text=f"Start: ", font=('Helvetica Bold', 20), bg="white", fg="black")
        start_time.grid(row=2, column=0, padx=10, pady=3, sticky="w")

        # Add the Subject's exam start time to exam frame
        end_time = Label(exam_frame, text=f"End: ", font=('Helvetica Bold', 20), bg="white", fg="black")
        end_time.grid(row=2, column=1, padx=10, pady=3, sticky="w")

        # attribute specific components of the label to a unique exam key
        self.timers[exam_key] = timer
        self.start_times[exam_key] = start_time
        self.end_times[exam_key] = end_time

    # updates the timer to display the time remaining in the exam as well as change the colour depending on how much time is left
    def update_timers(self, exam_key, new_text, colour):
        if exam_key in self.timers:
            self.timers[exam_key].config(text="")
            self.timers[exam_key].config(text=new_text, fg=colour)
    
    # Add the calculated start and end times to the exam frame
    def update_start_end_times(self, exam_key, time_now, end_of_exam):
        if exam_key in self.start_times:
            self.start_times[exam_key].config(text="")
            self.start_times[exam_key].config(text=f"Start: {time_now}")
            
        if exam_key in self.end_times:
            self.end_times[exam_key].config(text="")
            self.end_times[exam_key].config(text=f"End: {end_of_exam}")

# When the button 'Begin Exam' is pressed
# start_exam() makes window enter 'exam mode' where other (not-needed) buttons are removed
# begins the countdown for the exams
def start_exam():
    settings_button.place_forget()
    start_btn.place_forget()
    clear_btn.place(relx=0.67, rely=0.89, anchor="center")
    global examination_frames, exam_key_list
    examination_frames = ExamFrames(labelframe, VAR, CLICKED1, CLICKED2, CLICKED3, CLICKED4, TIME_VAR_1, TIME_VAR_2, TIME_VAR_3, TIME_VAR_4)
    exam_key_list = ["Exam1", "Exam2", "Exam3", "Exam4"]
    calculate_start_end_times()
    countdown_timer()

# updates the exam timer
def update_exam_timers(exam_frames_instance, exam_key, new_text, colour):
    exam_frames_instance.update_timers(exam_key, new_text, colour)

# updates the exam's start and end times
def update_exam_info(exam_frames_instance, exam_key, time_now, end_of_exam):
    exam_frames_instance.update_start_end_times(exam_key, time_now, end_of_exam)

# performs the calculation to determine the start and end time of the exam
def calculate_start_end_times():
    i = 0

    # loop through all exams and update their corresponding start and end time labels 
    while i < len(exam_total_length):
        # gets the user's local time
        current_time = datetime.now()

        # calculates the time in which the exam will end
        time_after_exam = current_time + timedelta(hours=((exam_total_length[i] // 3600) % 3600), minutes=((exam_total_length[i] // 60) % 60), seconds=(exam_total_length[i] % 60))

        # formats the start and end times into "HH:MM:SS"
        formatted_start_time = format(current_time, '%I:%M:%S %p')
        formatted_end_time = format(time_after_exam, '%I:%M:%S %p')

        # updates the labels with new information
        update_exam_info(examination_frames, exam_key_list[i], formatted_start_time, formatted_end_time)
        i += 1

# countdown_timer() is the main aspect of this program
# every second it gets an exam, checks the time remaining and makes a decision seen below
def countdown_timer():
    i = 0

    # loop through all exams
    while i < len(exam_total_length):
        try:
            # check if the exam has been stopped and if they have exit the def function
            if exam_total_length[i] == "Stopped":
                return
            elif exam_total_length[i] > 0:
            # decreases time remaining in exam by 1 (second)
                exam_total_length[i] -= 1

                # decisions below check to see which phase of the exam the timer is currently in:
                    # if the timer is in readingtime: the text will be blue
                    # if the timer is out of reading time, but not over: the text will be black
                    # if the timer is over: the text will display "Times Up!" in red 

                if exam_total_length[i] <= exam_working[i] and exam_total_length[i] > 0:
                    text_colour = "black"
                    # updates exam timer
                    update_exam_timers(examination_frames, exam_key_list[i], f"{(exam_total_length[i] // 3600) % 3600:02}:{(exam_total_length[i] // 60) % 60:02}:{exam_total_length[i] % 60:02}", text_colour)
                elif exam_total_length[i] == 0:
                    text_colour = "red"
                    # updates exam timer
                    update_exam_timers(examination_frames, exam_key_list[i], "Time's Up!", text_colour)
                else:
                    text_colour = "blue"
                    # updates exam timer
                    update_exam_timers(examination_frames, exam_key_list[i], f"{(exam_total_length[i] // 3600) % 3600:02}:{(exam_total_length[i] // 60) % 60:02}:{exam_total_length[i] % 60:02}", text_colour)
        except:
            break
            
        i += 1
        
    # updates the timers every second
    root.after(1000, countdown_timer)

# when 'Clear' button is pressed
def clear_exams():
    # gets main window out of 'exam mode' by bringing buttons back
    settings_button.place(relx=0.975, rely=0.043, anchor="ne")
    clear_btn.place_forget()

    # changes all of the exam's remaining time to "Stopped", this will in turn cancel the countdown function
    for i in range(len(exam_total_length)):
        exam_total_length[i] = "Stopped"

    # removes all 'exam groups' from the exam display
    for widget in labelframe.winfo_children():
            widget.destroy()

# Defines the start and clear buttons for the exam countdown timers
start_btn = Button(root , text = "Begin Exams", font=("Helvetica Bold", 40), bg="light grey", border=0, width=10, command = start_exam)
clear_btn = Button(root , text = "Clear", font=("Helvetica Bold", 40), bg="light grey", border=0, width=10, command=clear_exams)

# Defines the settings button, this opens the subject selection window
settings_button = tk.Button(main_canvas, image=button_image, borderwidth=0, command=settings_menu)
settings_button.place(relx=0.975, rely=0.043, anchor="ne")

clock_frame = tk.Frame(main_canvas, width=550, height=500, bg="white")
clock_frame.place(relx=0.213, rely=0.37, anchor="center")
    
# canvas inside of a frame where the analogue clock is displayed
frame_canvas = tk.Canvas(clock_frame, width=600, height=600, bg="white")
frame_canvas.place(relx=0.5, rely=0.5, anchor="center") 

# Defines the digital clock display
digi_clock_display = tk.Label(main_canvas, text="", font=('Helvetica Bold', 75), bg="white", 
                fg="black", borderwidth=10, relief="groove")
digi_clock_display.place(relx=0.245, rely=0.75, anchor="n")  

# Draw Clock Face using tkinter-imbedded oval tool
# draw line: first x value, first y value, second x value, second y value
frame_canvas.create_oval(140, 80, 570, 510, outline="black" , width=8)
frame_canvas.create_oval(150, 90, 560, 500, outline="lavender", width=5)
frame_canvas.create_oval(350, 290, 360, 300, fill="black")

# Draw numbers on the clock face
for i in range(1, 13):
    angle = math.radians(i * 30) # 360 (degrees) / 12 (unique hours) = 30 (degrees per hour)

    # the below code generates the x and y coordinates for where the number/text will be placed:
    # (hard-coded numbers were determined by trial and error to see which looked best)

    # for the clock, we are using the sin/cosine maths functions which refers to the UNIT CIRCLE
        # in unit circle: the sine of an angle is the x coordinate along the circumference of the unit circle and the cosine of the angle is the y coordinate
    x = 355 + 180 * math.sin(angle)
    y = 295 - 180 * math.cos(angle)

    # Draw the numbers using tkinter text tool
    frame_canvas.create_text(x, y, text=str(i), font=("Helvetica", 25, "bold"), fill="black")
    # text=str(i) auto-fills the textbox with the number (1,2,3,...,12) as the for loop iterates

# Draws notches on the clock face
# (hard-coded numbers were determined by trial and error to see which looked best)
for i in range(60):
    # places an 'hour' notch every 5 smaller notches
    if i % 5 == 0:
        angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
        x1 = 355 + 215 * math.sin(angle)
        y1 = 295 - 215 * math.cos(angle)
        x2 = 355 + 195 * math.sin(angle)
        y2 = 295 - 195 * math.cos(angle)
        frame_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
        
    else:
        angle = math.radians(i * 6) # 1 notch for every second (360 (degree) / 60 (seconds) = 6 (degrees per second))
        x1 = 355 + 213 * math.sin(angle)
        y1 = 295 - 213 * math.cos(angle)
        x2 = 355 + 205 * math.sin(angle)
        y2 = 295 - 205 * math.cos(angle)
        frame_canvas.create_line(x1, y1, x2, y2, width=3, fill="black")

# updates the local time clocks every second
def draw_clocks():
    # Remove the previous sets of hands if they're not already gone
    try:
        frame_canvas.delete("hand")
    except:
        draw_clocks()

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

    # Drawing The Hands:
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

# draw the clocks immediately upon running application
draw_clocks()

# Run the main window
root.mainloop()