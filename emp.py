# <think>
# First, the objective is to create a simplified Employee Management System (EMS) using Python. It needs to cover control structures, functions, and OOP concepts, but the steps are more about procedural programming with dictionaries. OOP might come in if we use classes, but the steps don't specify. I'll stick to the plan.


# ## Planning EMS Design  
# - The goal is to build a simplified Employee Management System (EMS) in Python.  
# - It should incorporate control structures, functions, and potentially OOP concepts like classes.  

# ## Evaluating Implementation  
# - The initial focus is on procedural programming using dictionaries for managing data.  
# - OOP might be included if classes are used, but the steps prioritize procedural approaches.
# </think>```python
# Employee Management System (EMS)

# Global dictionary to store employee data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def main_menu():
    while True:
        print("\nEmployee Management System (EMS)")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Thank you for using EMS!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
        except ValueError:
            print("Invalid Employee ID. Please enter a number.")
            continue
        
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            continue
        else:
            break
    
    name = input("Enter Employee Name: ")
    
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            break
        except ValueError:
            print("Invalid age. Please enter a number.")
    
    department = input("Enter Employee Department: ")
    
    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            break
        except ValueError:
            print("Invalid salary. Please enter a number.")
    
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    
    print(f"Employee {name} (ID: {emp_id}) added successfully!")

def view_employees():
    if not employees:
        print("No employees available.")
        return
    
    print("\nEmployee Details:")
    print("-" * 60)
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 60)
    
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} {details['department']:<15} {details['salary']:<10}")
    print("-" * 60)

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid Employee ID. Please enter a number.")
        return
    
    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")

# Run the main menu
if __name__ == "__main__":
    main_menu()