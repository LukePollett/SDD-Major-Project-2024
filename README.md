# BetterHSCTimer Application
![alt text](https://github.com/LukePollett/SDD-Major-Project-2024/blob/main/README%20images/App%20Logo.png)
BetterHSCTimer is an application for both the students and the invigilators! Imagine you're sitting your HSC examination and you look up at the projector on stage 
to see an abomination of windows that picasso himself would mistake for one of his masterpieces, an amalgamation of Notepads and a Clock app haunt your eyes for the next 3 hours.
Now, I know what you're thinking... "that doesn't sound like an experience I want to be in for my HSC!". Well you're in luck! BetterHSCTimer is an Exam Invigilation software that
significantly reduces the hassle and disorderly process of setting up the exams and completely eradicates the eyesore that was on thet projector! My program allows exam invigilators
to select the subjects they desire and time up to 4 exams at once! All through the simple but powerful capabilites of one application.



## Table of contents
- [Installation](#installation)
- [How to use](#howtouse)
- [Licence Information](#licenceinformation)
- [Visuals](#visuals)
- [Acknowledgements](#acknowledgements)
- [Author Details](#authordetails)
- [Documentation](#documentation)
- [Additional Details](#additionaldetails)



## Installation
### Download the Necessary Files:

1. Go to this repository's home page

2. Locate the green button title "<> Code" and click on it

3. Select 'Download ZIP' and wait for download to complete

4. After download has finished, extract the files to a location on your device

5. In Visual Studio Code or other IDE's (Integrated Development Environment), navigate to File > Open Folder

### If You Are A Windows User:

1. Open the file titled 'main.py' in the IDE and locate line 194

2. On that line, add the phrase '.txt' to the end of "HSC Subjects", like so: "HSC Subjects.txt"

3. Repeat steps 1 & 2 for lines 205 and 216, as such: "Exam Working Times.txt" and "Exam Reading Times.txt"



## How to use
#### Home Screen:

Currently, The Home screen contains 3 elements, which include: A Local Time Display (Analogue and Digital), An empty exam container, and a button.
Only one of these elements is able to be interacted with...The Settings Button! This button takes you to a new window where you'll be able to select up to 4
Subjects to undertake an Examination. Once you've finished this process your chosen exams will be 'cut and pasted' onto the main window in that previously-empty exam container.
In addition, after the exams have been transferred to the main window you'll be gifted the option to start your exams with the button 'Begin Exams'. When you do this, you'll notice that 
all of your exam timers have begun to tick down every second! However, it's not done yet! Don't like your exams? You can still clear all of them off the main window with a button click!

#### Subject Selection Screen:

I like to call this window the 'heart' of the program; it's where all of the complex features are computed and it sends out processed information back to the main window.
In this settings window, you are granted the opportunity to select up to 4 exams at once using the checkbox at the top which reveals 3 more radio buttons in which each 'unlock'
a previously inaccessible dropdown menu. Next up: after confirming all of your subjects, the program retrieves those subject's exam lengths and displays them clearly on a collection of labels.
Once you are finally happy with your Subjects and exam lengths, you can click 'confirm subject choices' in which it'll 'send off' your choices back to the main window where you continue you journey.



## Licence Information
This program is an open-source public domain, feel free to customise this code to your heart's content 😄👍!



## Visuals
![alt text](https://github.com/LukePollett/SDD-Major-Project-2024/blob/main/README%20images/BHSCT_GUI.png)
![alt text](https://github.com/LukePollett/SDD-Major-Project-2024/blob/main/README%20images/BHSCT_SW.png)
![alt text](https://github.com/LukePollett/SDD-Major-Project-2024/blob/main/README%20images/BHSCT_DD.png)



## Acknowledgements
This program uses the Integrated Python Library; Tkinter

Andrew Fong (andrewfong1988) assisted greatly in the kick-off of this project as well as ongoing development support.

NESA (NSW Education Standards Authority) are responsible for the HSC (Higher School Certificate) subjects and their  Exam Details

Saint Augustines Sydney (Brookvale) for facilitating development through equipment and utlilities



## Author Details
Luke Pollett: High School Student Studying HSC Software Design and Development at St Augustine's College, Sydney


## Documentation
The documentation for this application can be located in this Reposity on the ***home page***
