# Tilman Siuthani
# 03/19/2025
# P4LAB1
# Turtle graphics program to draw traingle and square

import turtle
win = turtle.Screen()
win.bgcolor('yellow')
timmy = turtle.Turtle()

# Set the way timmy looks
timmy.pensize (6)
timmy.pencolor('purple')
timmy.shape('arrow')

# Test 
# timmy.forward(100)

# for loop that runs 4 times
for i in range(4): 
    timmy.forward(100)
    timmy.right(90)

# while loop that runs 3 times
this_run = 0

while this_run < 3:
    timmy.forward(100)
    timmy.left(120)
    this_run += 1


# Keeps the window open after shape is drawn
win.mainloop()

