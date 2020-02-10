#!/usr/bin/env python3

#Kyla Johnson
#COP2002.0M1
#February 9, 2020
#Area and Perimeter
#This program retrieves input from the user to calculate the area and
#perimeter of a rectangle

#retrieve the user's name
name = input("Enter your name: ")
print()

# display a welcome message
print("Area and Perimeter Program")
print()

# get input from the user
length = float(input("Enter the length:\t"))
width = float(input("Enter the width:\t"))

# calculate area and perimeter
area = round(length * width, 2)
perimeter = round((2 * width) + (2 * length), 2)
            
# format and display the result
print()
print("Area: ", area,
    "\nPerimeter:", perimeter)
print()

#goodbye message
print(name + "," + " thank you for using this program!")
