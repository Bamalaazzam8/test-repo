import csv

class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.employees[row["ID"]] = row
        except FileNotFoundError:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
                writer.writeheader()

    def save_data(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
            writer.writeheader()
            for emp in self.employees.values():
                writer.writerow(emp)

    def add_employee(self):
        emp_id = input("Enter Employee ID: ").strip()
        if emp_id in self.employees:
            print("Employee with this ID already exists.")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()
        if not salary.isdigit():
            print("Invalid salary. Must be a number.")
            return
        email = input("Enter Email: ").strip()

        self.employees[emp_id] = {
            "ID": emp_id,
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }
        self.save_data()
        print("Employee added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees.values():
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Salary: {emp['Salary']}, Email: {emp['Email']}")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()
        if emp_id not in self.employees:
            print("Employee not found.")
            return

        emp = self.employees[emp_id]
        name = input(f"Enter new Name ({emp['Name']}): ").strip()
        position = input(f"Enter new Position ({emp['Position']}): ").strip()
        salary = input(f"Enter new Salary ({emp['Salary']}): ").strip()
        email = input(f"Enter new Email ({emp['Email']}): ").strip()

        if name:
            emp["Name"] = name
        if position:
            emp["Position"] = position
        if salary:
            if salary.isdigit():
                emp["Salary"] = salary
            else:
                print("Invalid salary. Keeping old value.")
        if email:
            emp["Email"] = email

        self.save_data()
        print("Employee updated successfully.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ").strip()
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_data()
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ").strip()
        if emp_id in self.employees:
            emp = self.employees[emp_id]
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Salary: {emp['Salary']}, Email: {emp['Email']}")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Search Employee")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_employee()
              elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                self.search_employee()
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")


if name == "__main__":
    manager = EmployeeManager()
    manager.menu()
