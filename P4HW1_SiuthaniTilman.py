# Tilman Siuthani
# 03/34/2025
# P4HW1
#  This program allows users to input multiple scores, validates them, calculates the average after removing the lowest score, and assigns a letter grade


# Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store valid scores
grades = []

# Loop to collect scores from user
for score in range(num_scores):
    grade = float(input(f"Enter score #{score + 1}: "))

    # While loop to check if the score is invalid
    while grade < 0 or grade > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        grade = float(input(f"Enter score #{score + 1} again: "))

    # Add valid score to the list
    grades.append(grade)

# Find the lowest score
lowest_score = min(grades)

# Create a modified list and remove the lowest score
modified_grades = grades.copy()
modified_grades.remove(lowest_score)

# Calculate the average of the modified list
average_score = sum(modified_grades) / len(modified_grades)

# Determine the letter grade
if average_score >= 90:
    grade_letter = "A"
elif average_score >= 80:
    grade_letter = "B"
elif average_score >= 70:
    grade_letter = "C"
elif average_score >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"

# Display the results
print("\n------------Results------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {modified_grades}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade_letter}")
print("--------------------------------")
