# Tilman Siuthani
# 02/12/2025
# P2LAB1
# Using imported libary, math, and f-string

import math

# Get Radius from user

radius = float(input("What is the radius of the circle? "))
print("------------------------------------------------------------------------------")
print()

# Caluclate diameter
diameter = 2 * radius

# Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calulate the Circumference
pi = math.pi
Circumference = 2 * pi * radius
print(f"The circumference of the circle is {Circumference:.2f}\n")

# Calulate the area
area = pi * radius**2
print (f"The area of the circle is {area:.3f}") 