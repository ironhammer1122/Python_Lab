#Q1
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m = Manager(101, "Yash", 50000, "IT")
m.display_manager()

#Q2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display_vehicle()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self):
        discount = self.price * 0.10
        final_price = self.price - discount
        print("Discounted Price:", final_price)


c = Car("Toyota", "Fortuner", "Diesel", 3000000)
c.display_car()
c.discounted_price()

#Q4
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = Employee("Yash", 25, 101, "Developer", 50000)
e.display()

#Q7
class Shape:
    def display(self):
        print("This is a shape")


class Circle(Shape):
    def area(self, radius):
        print("Circle Area:", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self, length, width):
        print("Rectangle Area:", length * width)


class Triangle(Shape):
    def area(self, base, height):
        print("Triangle Area:", 0.5 * base * height)


c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(10, 5)

t = Triangle()
t.display()
t.area(10, 6)

#Q8
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance


class Developer(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance


class Tester(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.15
        return self.basic_salary + allowance


m = Manager(101, "Amit", 50000)
d = Developer(102, "Rahul", 40000)
t = Tester(103, "Rohan", 35000)

print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())

#Q10
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def display(self):
        print("Sports Car")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Type: High Performance")


class ElectricBike(Bike):
    def display(self):
        print("Electric Bike")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Type: Electric")


s = SportsCar("BMW", "M4")
s.display()

print()

e = ElectricBike("Ather", "450X")
e.display()

#Q11
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


r = Result(101, "Rahul", "CSE", 80, 75, 90)
r.calculate_result()

#Q14
class Camera:
    def take_photo(self):
        print("Taking photograph...")


class Phone:
    def make_call(self):
        print("Making phone call...")


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and phone features")


s = Smartphone()

s.display()
s.take_photo()
s.make_call()

#Q17
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo")


d = Dog("Dog")
d.eat()
d.sound()

print()

c = Cat("Cat")
c.eat()
c.sound()

print()

co = Cow("Cow")
co.eat()
co.sound()