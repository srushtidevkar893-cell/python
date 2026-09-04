# Student Marks Management System

print("----- Student Marks Management System -----")

marks = []

# Taking marks from user
n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = int(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

while True:

    print("\n--------- MENU ---------")
    print("1. Display Marks")
    print("2. Insert New Mark")
    print("3. Update Mark")
    print("4. Delete Mark")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nOriginal Marks:")
        for mark in marks:
            print(mark)

    elif choice == 2:
        position = int(input("Enter position: "))
        mark = int(input("Enter new mark: "))

        marks.insert(position, mark)

        print("After Insertion:")
        print(marks)

    elif choice == 3:
        position = int(input("Enter position to update: "))
        mark = int(input("Enter new mark: "))

        marks[position] = mark

        print("After Updating:")
        print(marks)

    elif choice == 4:
        mark = int(input("Enter mark to delete: "))

        if mark in marks:
            marks.remove(mark)
            print("After Deletion:")
            print(marks)
        else:
            print("Mark not found!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")