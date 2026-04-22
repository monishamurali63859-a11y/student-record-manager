students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    dept = input("Enter department: ")

    student = {
        "name": name,
        "age": age,
        "dept": dept
    }

    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return

    print("\n📋 Student Records:")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Dept: {s['dept']}")
    print()

def search_student():
    name = input("Enter name to search: ")
    found = False

    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: {s}")
            found = True
            break

    if not found:
        print("❌ Student not found.\n")

def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("🗑️ Student deleted.\n")
            return

    print("❌ Student not found.\n")

while True:
    print("===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
