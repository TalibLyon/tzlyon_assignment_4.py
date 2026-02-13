"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: Talib Lyon
GitHub Username: TalibLyon
Date: 2/13/2026
Description: This game simulates a semester at a prestigious school for sorcerers where the player must balance GPA, stress, study time, and social life while taking on missions and strengthening cursed skills.
AI Usage: Used for debugging and clarification of assignment instructions.
"""

# ========================================
# Initial Student Setup
# ========================================

student_name = "Talib"
current_gpa = 3.2
study_hours = 11
social_points = 10
stress_level = 43

print("Welcome to College Life Adventure,", student_name + "!")
print("Here are your starting stats:")
print("GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)

# ========================================
# Decision 1: Course Load Selection
# ========================================

print("\nMission Planning Time!")
print("Choose your mission load:")
print("B. Light")
print("A. Standard")
print("S. Heavy")

choice = input("Enter S, A, or B: ")

# Check course load choice and adjust stats
if choice == "B":
    study_hours -= 2
    stress_level -= 5
    print("You chose a Light mission load. Low stress, Easy pass")

elif choice == "A":
    study_hours += 2
    stress_level += 5
    print("You chose a Standard mission load. Balanced approach.")

elif choice == "S":
    study_hours += 5
    
    # Students with lower GPA struggle more with heavy loads
    if current_gpa >= 3.0:
        stress_level += 10
    else:
        stress_level += 25  # Low GPA + heavy load = much more stress
    
    print("You chose a Heavy mission load. Huge curse ahead!")

else:
    print("Invalid option. No changes were made.")



