name = input("Enter your name: ")
print("Welcome to the Management System", name)

number = int(input("Enter number of students: "))
studentsList = []

for i in range(number):
    d = {}
    d['Name'] = input("Enter name: ")
    d['Roll No'] = int(input("Enter roll number: "))
    d['Marks'] = float(input("Enter marks: "))
    studentsList.append(d)

print(studentsList)