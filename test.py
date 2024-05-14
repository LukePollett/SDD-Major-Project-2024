"""
This python file contains the tests for the ExamTimer program
These may or may not be implemented in the final version of the program
This is just for testing purposes
:)

Some code written here will be AI generated,
This is just because i may be stuck and/or need suggestions on how to do a certain aspect of my program.
I will not implement AI code word for word as this is big nono :(
"""

with open("HSC Subjects", "r") as grilled_cheese:
	lines = grilled_cheese.readlines()
	
Stage_6_Subjects = []
	
for l in lines:
	list1 = l.split(", ")
	Stage_6_Subjects.append(list1[0].replace("\n", ""))
	
# ====================================================================================================
	
with open("Exam Working Times", "r") as waffle:
	lines = waffle.readlines()
	
Exam_working_times = []
	
for l in lines:
	list2 = l.split(", ")
	Exam_working_times.append(list2[0].replace("\n", ""))
	
# ====================================================================================================
	
with open("Exam Reading Times", "r") as pancake:
	lines = pancake.readlines()
	
Exam_reading_times = []
	
for l in lines:
	list3 = l.split(", ")
	Exam_reading_times.append(list3[0].replace("\n", ""))
	
