# Today's Python Challenge
# Student Marks Analyzer

students = {
    "Bhagyashree": {"Python": 85, "SQL": 78, "Maths": 90},
    "Poorvi": {"Python": 92, "SQL": 88, "Maths": 84},
    "Sukanya": {"Python": 76, "SQL": 81, "Maths": 79}
}

print("===== STUDENT MARKS ANALYZER =====")

for name, marks in students.items():

    total = sum(marks.values())
    average = total / len(marks)

    print("\nStudent:", name)

    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("Total:", total)
    print("Average:", round(average, 2))

    if average >= 85:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)

# Find topper
topper = ""
highest_average = 0

for name, marks in students.items():
    average = sum(marks.values()) / len(marks)

    if average > highest_average:
        highest_average = average
        topper = name

print("\n===== RESULT =====")
print("Topper:", topper)
print("Highest Average:", round(highest_average, 2))