# ------------------------------------------
# Python Marks Percentage Calculator
# Author: Tech With Rabeea
# Part of: Python Full Course for Beginners
# ------------------------------------------

# Step 1: Intro message
print("🎓 Welcome to the Marks Percentage Calculator!")
print("Let's calculate your total marks and percentage.\n")

# Step 2: Taking input from user
name = input("Enter your name: ")

# Asking total number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Step 3: Initialize total variable
total_marks = 0

# Step 4: Take marks for each subject
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

# Step 5: Ask total marks per subject
max_marks_per_subject = float(input("\nEnter maximum marks per subject: "))
max_total = max_marks_per_subject * num_subjects

# Step 6: Calculate percentage
percentage = (total_marks / max_total) * 100

# Step 7: Display result
print("\n--------------------------------------")
print(f"Student Name: {name}")
print(f"Total Marks Obtained: {total_marks} / {max_total}")
print(f"Percentage: {percentage:.2f}%")
print("--------------------------------------")

# Step 8: Optional message
if percentage >= 90:
    print("Excellent work! 🎉 Keep it up!")
elif percentage >= 75:
    print("Great job! 👍 You're doing really well.")
elif percentage >= 50:
    print("Good effort! 💪 Keep improving.")
else:
    print("Don't give up! Practice makes perfect! 💡")
