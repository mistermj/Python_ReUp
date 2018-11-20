

# No keyword replacement for abstract but it tells that interp. dah 
# its gonna be implement in subclass and not here. daeway it works.
# thing to notice for polymorphism is that the employee 
# creating an abstract base class
class Employee:

    def determine_weekly_salary(self, weeklyHours, wage):
        raise NotImplementedError("This method is not implemented by subclass.")

# Inherit from base class and define calculations for permanent employee
class Permanent(Employee):
    #definition of method starts here

    def determine_weekly_salary(self, weeklyHours, wage):
        salary = 40 * wage
        print(f"This employee worked for {weeklyHours} hours and the wage is {wage}")
class Contractor(Employee):
    def determine_weekly_salary(self, weeklyHours, wage):
        salary = 45 * wage
        print(f"This Happy employee worked for {weeklyHours} hours and the wage is {wage}")
def get_employees():
    some_perm_emp = Permanent()
    some_cont_emp = Contractor()
    both_emp = [some_perm_emp, some_cont_emp]
    return both_emp
def main():
     #employee = Employee()
     # returns an exception.
    hours = 50; wage = 70
    employees = get_employees()

    for emp in employees:
        emp.determine_weekly_salary(hours, wage)

if __name__ == "__main__":
    main()
