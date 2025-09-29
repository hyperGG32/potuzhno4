"""
Task 3 — Class Exam Results 📊

Requirements:
  - grades = [45, 72, 88, 91, 60, 55]
  - Compute average using a loop (avoid sum())
  - Gather grades strictly above the average into a new list
  - Print the average and the list

Practice: loop aggregation, conditional filtering

OUTPUT EXAMPLE
--------------
Average: 68.50
Above average: [72, 88, 91]
"""

grades = [45, 72, 88, 91, 60, 55]
print("(Starter) Grades:", grades)

s = 0
for grade in grades:
    s += grade
average = s/len(grades)

aboveav = [grade for grade in grades if grade > average]
print("Average grades:", average)
print("Above average grades:",  aboveav)
