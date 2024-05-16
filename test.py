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
from tkinter import ttk 

window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 
  
# label text for title 
ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Select the Month :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = [' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December']
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
window.mainloop() 