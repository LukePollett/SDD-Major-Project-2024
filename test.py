"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)

Some code written here will be AI generated,
This is just because i may be stuck and/or need suggestions on how to do a certain aspect of my program.
I will not implement AI code word for word as this is big nono :(
"""
import tkinter as tk
from tkinter import *
import time
from PIL import Image,ImageTk
import math

class LabelFrameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LabelFrame Example")
        
        # Create and place some LabelFrames with automatic labels
        self.create_labelframe("Frame 1", "Label 1", 0, 0)
        self.create_labelframe("Frame 2", "Label 2", 1, 0)
        self.create_labelframe("Frame 3", "Label 3", 2, 0)

    def create_labelframe(self, frame_text, label_text, row, column):
        labelframe = LabelFrame(self.root, text=frame_text)
        labelframe.grid(row=row, column=column, padx=10, pady=10)
        
        # Automatically add a label to the labelframe
        label = Label(labelframe, text=label_text)
        label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelFrameApp(root)
    root.mainloop()

# class LabelFrame(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.pack()

#     def add_label(self, text, **kwargs):
#         label = LabelWidget(self, text, **kwargs)
#         label.pack()


# class LabelWidget(tk.Label):
#     def __init__(self, parent, text, *args, **kwargs):
#         super().__init__(parent, text=text, *args, **kwargs)


# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("OOP Tkinter Example")

#         # Create a frame
#         self.frame = LabelFrame(self)
        
#         # Add labels to the frame
#         self.frame.add_label("Label 1")
#         self.frame.add_label("Label 2")
#         self.frame.add_label("Label 3")
#         self.frame.add_label("Label 4")


# if __name__ == "__main__":
#     app = Application()
#     app.mainloop()
