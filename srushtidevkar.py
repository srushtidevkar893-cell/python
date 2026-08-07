student_name = input("Enter student name: ")
student_class = input("Enter student class: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))


total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3


print("==============================")
print(f"=     FINAL SCORE CARD      =")
print("==============================")
print(f"Student Name : {student_name}")
print("------------------------------")
print(f"Subject 1    : {subject1:.2f}")
print(f"Subject 2    : {subject2:.2f}")
print(f"Subject 3    : {subject3:.2f}")
print("------------------------------")
print(f"Total Marks  : {total_marks:.2f}")
print(f"Average      : {average_marks:.2f}")
