from emp_operations import add_employee, get_employee, update_employee, delete_employee

print("## Employee Management System by Amey ##")
print("You can use this app to Add, View, Update, or Delete employees from your Database")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Get Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            ph_number = input("Enter your phone number: ")
            job = input("Enter your job profile: ")
            add_employee(first_name, last_name, email, ph_number, job)
            print("Employee added successfully")

        elif choice == "2":
            try:
                emp_id = int(input("Enter employee ID: "))
                employee = get_employee(emp_id)
                if employee:
                    print(f"Employee details: {employee}")
                else:
                    print("Employee not found")
            except ValueError:
                print("Invalid input. Please enter a valid employee ID.")

        elif choice == "3":
            try:
                emp_id = int(input("Enter employee ID: "))
                print("Enter details to be updated (leave blank to keep current value):")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                ph_number = input("Enter phone number: ")
                job = input("Enter job profile: ")
                update_employee(emp_id, first_name or None, last_name or None, email or None, ph_number or None, job or None)
                print("Employee details updated successfully")
            except ValueError:
                print("Invalid input. Please enter a valid employee ID.")

        elif choice == "4":
            try:
                emp_id = int(input("Enter employee ID: "))
                delete_employee(emp_id)
                print("Employee deleted successfully")
            except ValueError:
                print("Invalid input. Please enter a valid employee ID.")

        elif choice == "5":
            break

        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()
