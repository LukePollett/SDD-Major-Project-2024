import tkinter as tk

"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)
"""

def add_widget():
    # Create a new widget
    new_widget = tk.Label(root, text="New Widget")
    new_widget.pack()

def remove_widget():
    # Remove the last widget
    if len(root.pack_slaves()) > 0:
        root.pack_slaves()[-1].destroy()

root = tk.Tk()

# Create a button to add widgets
add_button = tk.Button(root, text="Add Widget", command=add_widget)
add_button.pack()

# Create a button to remove widgets
remove_button = tk.Button(root, text="Remove Widget", command=remove_widget)
remove_button.pack()

root.mainloop()