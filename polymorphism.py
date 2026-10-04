#Q1
class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def area(self):
        radius = 5
        print("Circle Area:", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Rectangle Area:", length * width)


class Triangle(Shape):
    def area(self):
        base = 8
        height = 6
        print("Triangle Area:", 0.5 * base * height)


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()
    
#Q2
class Employee:
    def calculate_salary(self):
        print("Employee salary")


class Manager(Employee):
    def calculate_salary(self):
        salary = 50000
        allowance = salary * 0.30
        print("Manager Salary:", salary + allowance)


class Developer(Employee):
    def calculate_salary(self):
        salary = 40000
        allowance = salary * 0.20
        print("Developer Salary:", salary + allowance)


class Tester(Employee):
    def calculate_salary(self):
        salary = 35000
        allowance = salary * 0.15
        print("Tester Salary:", salary + allowance)


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    employee.calculate_salary()
    
#Q3
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a large engine")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    
#Q4
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()
    
#Q8
class Report:
    def generate(self):
        print("Generating report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def create_report(report):
    report.generate()


create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())

#Q10
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student("Rahul", 85)
student2 = Student("Amit", 75)

if student1 > student2:
    print(student1.name, "has higher marks")

if student1 < student2:
    print(student1.name, "has lower marks")
    
#Q11
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 30000)

if product1 == product2:
    print("Both products have the same price")
else:
    print("Products have different prices")

if product1 > product2:
    print(product1.name, "is more expensive")
    
#Q13
class Person:
    def display_role(self):
        print("Person")


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()
    
