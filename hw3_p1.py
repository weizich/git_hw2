n = int(input("Enter the total number of students: "))
students = list(range(1, n + 1))  # Create a list of student IDs

index = 0  # Start with the first student
while len(students) > 1:  # Continue until only one student remains
    index = (index + 2) % len(students)  # Move to the next student who reports 3
    students.pop(index)  # Remove the student who reports 3

print("The student ID of the last one seating on the round table is:", students[0])