"""
Purpose: Importance of Class Variables
"""


class Employee:
    emp_count = 0  # class variable
    emp_id = 0  # Class variable

    def __init__(self, name, salary=20_000):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    # def total_employees_count(self):
    #     """This method is used to display the count of employees"""
    #     print(f"Total Employees count(before): {self.emp_count}")
        
    #     self.emp_count += 1
    #     print(f"self.emp_count               : {self.emp_count}")
        
        
    #     print(f"Total Employees count(after): {self.emp_count}")

    # def total_employees_count(self):
    #     """This method is used to display the count of employees"""
    #     print(f"Total Employees count(before): {Employee.emp_count}")
        
    #     Employee.emp_count += 1
    #     print(f"Employee.emp_count     : {Employee.emp_count}")
        
        
    #     print(f"Total Employees count(after): {Employee.emp_count}")


    # def total_employees_count(cls):  # class Method
    #     """This method is used to display the count of employees"""
    #     print(f"Total Employees count(before): {cls.emp_count}")
        
    #     cls.emp_count += 1
    #     print(f"cls.emp_count     : {cls.emp_count}")
        
        
    #     print(f"Total Employees count(after): {cls.emp_count}")


    def __del__(self):
        """
        This is destructor method - defaulty called,
        when the instance is deleted
        :return:
        """
        print("\nDestructor is called")
        Employee.emp_count -= 1


# e1 = Employee()
# TypeError: Employee.__init__() missing 1 required positional argument: 'name'


empl_1 = Employee("Udhay", 10879879)
print(vars(empl_1))
# empl_1.total_employees_count()
print(f"{Employee.emp_count = }")
print()

del empl_1

empl_2 = Employee("Prakash")
print(vars(empl_2))
# empl_2.total_employees_count()
print(f"{Employee.emp_count = }")


empl_3 = Employee("Akhila")
print(vars(empl_3))
print(f"{Employee.emp_count = }")


"""
NOTE: class variables can be modified at instance level,
    by the changes will reflect only to that instance
"""
