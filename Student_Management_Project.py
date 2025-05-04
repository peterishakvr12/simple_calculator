# class student:
#     def __init__(self, name, tariffnumber, age, rate):
#         self.name = name
#         self.tariffnumber = tariffnumber
#         self.age = age
#         self.rate = rate
# class studentmanger:
#     def __init__(self):
#         self.student = []

#     def add_student(self, name, tariffnumber, age, rate):
#         new_student = student(name, tariffnumber, age, rate)
#         self.student.append(new_student) 
#         print(f"student {name} adedd successfully !")

#     def edit_student(self, old_name, new_name):
#         for student in self.student:
#             if student.name == old_name:
#                 student.name = new_name
#                 print(f"student name update to {new_name} !")
#                 return
#         print(f"student {old_name} not found !")

#     def delete_student(self, name):
#         for student in self.student:
#             if student.name == name :
#                 self.student.remove(student)
#                 print(f"student {name} deleted successfully !")               
#                 return
#         print(f"student {name} not found !")

#     def search_student(self, name):
#         for student in self.student:
#             if student.name == name:
#                 print(f"found student: {student.name}, tariff: {student.tariffnumber}, age: {student.age}, rate: {student.rate}")    
#         print(f"student {name} not found")

# manager = studentmanger()
# new_name1 = input("please write the name: ")
# manager.add_student(new_name1, "12345", 20, 85)

# edit_name2 = input("what the name to edit")
# new_name2 = input("Enter the new name: ")
# manager.edit_student(edit_name2, new_name2)

# delete_name = input("write the name to delete: ")
# manager.delete_student(delete_name)

# search_name = input("write the name to search: ")
# manager.search_student_student(search_name)


class Student:
    def __init__(self, name, tariffnumber, age, rate):
        self.name = name
        self.tariffnumber = tariffnumber
        self.age = age
        self.rate = rate

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        tariffnumber = input("Enter student number: ")
        age = input("Enter student age: ")
        rate = input("Enter student rate: ")
        new_student = Student(name, tariffnumber, int(age), float(rate))
        self.students.append(new_student)
        print(f"Student {name} added successfully!\n")

    def edit_student(self):
        old_name = input("Enter the current name of the student: ")
        new_name = input("Enter the new name: ")
        for student in self.students:
            if student.name == old_name:
                student.name = new_name
                print(f"Student name updated to {new_name}!\n")
                return
        print(f"Student {old_name} not found!\n")

    def delete_student(self):
        name = input("Enter the name of the student to delete: ")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted successfully!\n")
                return
        print(f"Student {name} not found!\n")

    def search_student(self):
        name = input("Enter the name of the student to search: ")
        for student in self.students:
            if student.name == name:
                print(f"Found student: Name: {student.name}, Tariff: {student.tariffnumber}, Age: {student.age}, Rate: {student.rate}\n")
                return
        print(f"Student {name} not found!\n")

def main():
    manager = StudentManager()
    
    while True:
        print("Choose an action:")
        print("1 - Add new student ")
        print("2 - Edit student name")
        print("3 - Delete student")
        print("4 - Search for student")
        print("5 - Exit the program")
        
        choice = input("Enter the action number: ")
        
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.edit_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.search_student()
        elif choice == "5":
            print("Program ended. Goodbye!")
            break
        else:
            print("Please enter a valid number from the options!\n")

if __name__ == "__main__":
    main()
    