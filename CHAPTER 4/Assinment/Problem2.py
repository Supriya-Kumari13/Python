# write a program to accept marks of 6 student and display it in sorted manner

marks = [input("Enter the marks of student 1: "),
        input("Enter the marks of student 2: "),
        input("Enter the marks of student 3: "),
        input("Enter the marks of student 4: "),
        input("Enter the marks of student 5: "),
        input("Enter the marks of student 6: ")]
marks.sort()  # Sort the list of marks in ascending order
print(marks)  # Print the sorted list of marks