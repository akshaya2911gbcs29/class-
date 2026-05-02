class Employee:
    def employee_salary(self):
        self.name = input("Enter employee name: ")
        self.id = input("Enter ID: ")
        self.basic=float(input("Enter basic salary: "))
        da=0.10*self.basic
        hra=0.20*self.basic
        self.gross=self.basic+da+hra
        print("\n--- Employee Salary Details ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Basic salary: {self.basic}")
        print(f"Gross salary: {self.gross}")
employee = Employee()
employee.employee_salary()
