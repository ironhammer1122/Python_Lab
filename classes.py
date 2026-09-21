#Q1
class Student:
    def __init__(self, rno, name, marks):
        self.rno = rno
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Roll Number: {self.rno}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
obj1 = Student(101, "Yash", 90)
obj1.display()

#Q2
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
obj2 = Rectangle(5, 3)
print("Area of rectangle: ", obj2.area())
print("Perimeter of rectangle: ", obj2.perimeter())

#Q3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius
obj3 = Circle(5)
print("Area of circle: ", obj3.area())
print("Circumference of circle: ", obj3.circumference())

#Q4
class Book:
    def __init__(self, bid, title, author, price):
        self.bid = bid
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f"Book ID: {self.bid}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
obj4 = Book(1, "Python Programming", "John Doe", 500)
obj4.display()

#Q5
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Price: ${self.price}")
    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.price
        self.price -= discount_amount
obj5 = MobilePhone("Apple", "iPhone 13", 128, 999999)
obj5.apply_discount(10)
obj5.display()        

#Q6
class Patient:
    def __init__(self, pid, name, age, disease, fee):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee
    def display(self):
        print(f"Patient ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
        print(f"Fee: {self.fee}")
    def total_fee(self, additional_fee):
        self.fee += additional_fee
obj6 = Patient(1, "Alice", 30, "Flu", 100)
obj6.total_fee(50)
obj6.display()

#Q7
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability
    def rent(self):
        if self.availability:
            self.availability = False
            return True
        else:
            return False
    def return_vehicle(self):
        self.availability = True
    def calculate_rental_charges(self, days):
        return self.rental_rate * days
obj7 = Vehicle("MH12AB1234", "Toyota Camry", 1000, True)
if obj7.rent():
    print("Vehicle rented successfully.")
    charges = obj7.calculate_rental_charges(5)
    print(f"Rental charges for 5 days: {charges}")
    obj7.return_vehicle()
    print("Vehicle returned successfully.")

#Q8
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks should be a list of five subjects
    def total(self):
        return sum(self.marks)
    def percentage(self):
        return (self.total() / 500) * 100  # Assuming each subject is out of 100
    def grade(self):
        perc = self.percentage()
        if perc >= 90:
            return 'A'
        elif perc >= 80:
            return 'B'
        elif perc >= 70:
            return 'C'
        elif perc >= 60:
            return 'D'
        else:
            return 'F'
    def __del__(self):
        print(f"Student {self.name}'s result processing is complete.")
obj8 = StudentResult("Bob", [85, 90, 78, 92, 88])
print(f"Total Marks: {obj8.total()}")
print(f"Percentage: {obj8.percentage():.2f}%")
print(f"Grade: {obj8.grade()}")