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

# ========================================
# Decision 2: Study Strategy Selection
# ========================================

print("\nTime to choose your cursed strategy!")
print("Options: CursedEnergyDrills, SquadTraining, DomainExpansionRush")

# List of valid study strategies
study_options = ["CursedEnergyDrills", "SquadTraining", "DomainExpansionRush"]

strategy = input("Choose your strategy: ")

# Validate using membership operator
if strategy in study_options:
    
    # Cursed Energy Drills: Strong GPA boost, low social gain
    if strategy == "CursedEnergyDrills":
        current_gpa += 0.2
        social_points -= 2
        print("You mastered cursed energy control. GPA increased!")

    # SquadTraining: Balanced growth
    elif strategy == "SquadTraining":
        current_gpa += 0.1
        social_points += 3
        print("Training with your squad improved both skill and bonds!")

    # Domain Expansion Rush: Risky high-pressure training
    elif strategy == "DomainExpansionRush":
        # Logical operators used here
        if stress_level > 50 and study_hours < 10:
            current_gpa -= 0.2
            print("Your domain collapsed under pressure!")
        else:
            current_gpa += 0.05
            print("You barely maintained your domain technique!")
        
        social_points -= 3

else:
    print("Invalid strategy. No changes were made.")

# ========================================
# Final Semester Assessment
# ========================================

print("\nFinal Semester Results...")
print("Final GPA:", current_gpa)
print("Final Study Hours:", study_hours)
print("Final Social Points:", social_points)
print("Final Stress Level:", stress_level)

# Identity operator used for type checking
if type(current_gpa) is float:

    # Nested decision level 1
    if current_gpa >= 3.5 and stress_level < 50:
        
        # Nested decision level 2
        if social_points > 15:
            print("You became a Special Grade Sorcerer! Elite status achieved!")
        else:
            print("You became a powerful Grade 1 Sorcerer, but you walk alone.")

    elif current_gpa >= 2.5:
        
        if stress_level >= 70:
            print("You passed the semester, but barely survived the curses gained...")
        else:
            print("You are a steady Grade 2 Sorcerer. Growth continues.")

    else:
        print("You were overwhelmed and destroyed by the disaster curses... !")

else:
    print("Error: GPA data type incorrect.")

