#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Experiment 2.3: Student Record Keeper
students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student already exists.")
        return
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    attendance = input("Enter Attendance (%): ")
    
    students[roll_no] = {
        "Name": name,
        "Grade": grade,
        "Attendance": attendance
    }
    print("Student added successfully.")

def update_student():
    roll_no = input("Enter Roll Number to update: ")
    if roll_no in students:
        print("Leave blank to keep current value.")
        name = input(f"Enter new name ({students[roll_no]['Name']}): ")
        grade = input(f"Enter new grade ({students[roll_no]['Grade']}): ")
        attendance = input(f"Enter new attendance ({students[roll_no]['Attendance']}): ")
        
        if name: students[roll_no]['Name'] = name
        if grade: students[roll_no]['Grade'] = grade
        if attendance: students[roll_no]['Attendance'] = attendance
        print("Student record updated.")
    else:
        print("Student not found.")

def view_students():
    if not students:
        print("No records found.")
    else:
        print("\n--- Student Records ---")
        print(f"{'Roll No':<10} {'Name':<15} {'Grade':<10} {'Attendance':<10}")
        print("-" * 50)
        for roll, data in students.items():
            print(f"{roll:<10} {data['Name']:<15} {data['Grade']:<10} {data['Attendance']:<10}")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student record deleted.")
    else:
        print("Student not found.")

def record_keeper():
    while True:
        print("\n--- Student Record Keeper ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    record_keeper()