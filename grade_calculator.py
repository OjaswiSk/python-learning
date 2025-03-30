#list to store results
grades = []

# function to calculate letter grade 
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
# Main program
while True:
    name = input("Enter student name (or 'quit' to stop): ")
    if name.lower() == "quit":
        break
    score = int(input(f"Enter {name}'s score (0-100): "))
    grade = calculate_grade(score)
    grades.append({"name": name, "score": score, "grade": grade})
    print(f"{name} got a grade of {grade}")

# Print all results
print("\n--- Final Results ---")
for student in grades:
    print(f"{student['name']}: Score = {student['score']}, Grade = {student['grade']}")
    
