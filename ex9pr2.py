# Student Score Filter

# Accept a list of grades
grades = [75, 82, 68, 91, 79]

print("Current grades:", grades)

# Ask the user for the index position
index = int(input("Enter the index position to update (0-4): "))

# Ask for the new grade
new_grade = float(input("Enter the new grade: "))

# Update the selected grade
grades[index] = new_grade

# Display the corrected list
print("Corrected grades:", grades)
