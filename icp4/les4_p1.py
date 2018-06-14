class Employee(object):
    employee_count=0
    totalsal=0
    avgsal=0

    def __init__(self,name,family,sal,dept): # init method in the class to instantiate the class member variables
        self.name = name
        self.family = family
        self.salary = sal
        self.department = dept
        Employee.employee_count += 1
        Employee.totalsal += sal

    def avgsalary(self):
        avgsal=Employee.totalsal/Employee.employee_count
        print("Average Salary of Employees:",avgsal)

    def calcemployees(self):
        print("Total Employees are:",Employee.employee_count)

    def displayDetails(self):
        print("Name:",self.name,"Family:",self.family,"Salary:",self.salary,"Department:",self.department)


class FullTimeEmployee(Employee): # Created a class which inherits the members of class Employee
    def init(self,n,f,s,d):
        Employee.init(self,n,f,s,d)



e1 = Employee("rajiv","ML",3000,"deep learning") # Created an object and instantiated the members of the class
e2 = Employee("varma","J",4000,"java professional")
fe1=FullTimeEmployee("ca","C",5900,"Cloud") # Created an object of the sub class FullTimeEmployee
fe2=FullTimeEmployee("ram","M",8000,"Management")

e1.displayDetails()
e2.displayDetails()
fe1.displayDetails()
fe2.displayDetails() # Calling the method of the super class using the sub class object

fe2.avgsalary()
fe2.calcemployees()