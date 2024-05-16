#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     17/09/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import time
import sys

pi = 3.1415
prompt = ">>"
length = int(input("Enter the length: "))
width = int(input("Enter the width"))
rad = int(input("Enter the readius"))
side1 = int(input("Enter the first side"))
side2 = int(input("Enter the second side"))
side3 = int(input("Enter the third side"))
side4 = int(input("Enter the fourth side"))

def areaRect(a, b):
	return(a* b)

def perRect(a, b, c, d):
	return(a + b + c + d)

def areaCir(x):
	return(pi(x^2))

def cirCircle(x):
	return(2 * pi * x)

def delayPrint(x):
	for i in x:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.1)

# Ask the person for their name
delayPrint("\nWhat is your name")
name = input(prompt)
delayPrint("\nIt is nice to meet you " + name)
ready = False

# Asking what thing to they want to find
anotherShape = True
while anotherShape == True:
	delayPrint("\nWhat do you want to find? What type of shape would you like to find something about? Either a rectangle or a circle?")
	choice = input(prompt).lower()
	validChoice = False
	while validChoice == False:
		if choice.lower() == "circle" or choice.lower() == "a circle":
			delayPrint("\nWhat would you like to find out about a circle? The area or the circumference")
			if choice.lower() == "the area" or choice.lower() == "area":
				delayPrint("\n" pi , " * " rad, "^2 ", " = ", areacir(rad))
			elif choice.lower() == "the circumference" or choice.lower() == "circumference":
				delayPrint("\n2 * ", pi, " * ", rad, " = ", cirCircle(rad))
			else:
				delayPrint("\nInvalid Input. Type circumference or area.")
		elif choice.lower() == "rectangle" or choice.lower() == "a rectangle":
			if choice.lower() == "area" or choice.lower() == "the area":
				delayPrint("\n"length, " * " width, " = ", areaRect(length, width))
			elif choice.lower() == "the perimeter" or choice.lower() == "perimeter":
				delayPrint("\n"side1, " + ", side2, " + ", side3, " + ", side4, " = ", perRect(side1, side2, side3, side4))
			else:
				delayPrint("\nInvalid Input. Type area or preimeter.")
		else:
				delayPrint("\nInvalid Input")
	delayPrint("\nDo you want to calculate another shape?")
		if choice.lower() == "no":
			anotherShape = False
		else choice.lower() == "yes":
		else:
			delayPrint("\nInvaild Input")
delayPrint("\nSee you later.")

