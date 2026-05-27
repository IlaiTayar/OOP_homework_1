class Employee:

    def __init__(self, name, year_of_joining, salary, address):
        self.name = name
        self.year_of_joining = year_of_joining
        self.salary = salary
        self.address = address


    def print_info(self, emp_1=None, emp_2=None):
        print("  name       year_of_joining       salary         address")
        print(f"  {self.name}            {self.year_of_joining}               {self.salary}        {self.address}")
        if emp_1 is not None:
            print(f"  {emp_1.name}         {emp_1.year_of_joining}               {emp_1.salary}        {emp_1.address}")
        if emp_2 is not None:
            print(f"  {emp_2.name}           {emp_2.year_of_joining}               {emp_2.salary}        {emp_2.address}")
