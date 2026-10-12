#Q1
import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Python": [85, 70, 90, 65, 80],
    "DBMS": [80, 75, 85, 70, 90],
    "Mathematics": [90, 80, 95, 60, 85]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print("Complete DataFrame:")
print(df)

print("\nStudents with average above 75:")
print(df[df["Average"] > 75])

#Q2
data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Neha", "Raj", "Priya", "Karan"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [45000, 60000, 55000, 75000, 40000],
    "Experience": [2, 5, 3, 8, 4]
}

df = pd.DataFrame(data)

print("Employees with salary above 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])

#Q5
data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Neha", "Raj", "Priya", "Karan"],
    "Product": ["Laptop", "Phone", "Mouse", "Monitor", "Keyboard"],
    "Quantity": [1, 2, 5, 1, 3],
    "Price": [60000, 20000, 500, 12000, 1500],
    "Discount": [5000, 2000, 200, 1000, 300]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:", df["Final_Amount"].mean())

#Q6
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Neha", "Raj", "Priya", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [80, 65, 90, 70, 75]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])

#Q8
data = {
    "Amit": 85,
    "Rahul": 70,
    "Sneha": 92,
    "Priya": 78,
    "Rohan": 65
}

s = pd.Series(data)

print("Student Marks:")
print(s)

print("\nMarks of Amit:", s["Amit"])
print("Maximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())

print("\nStudents scoring above 75:")
print(s[s > 75])

#Q10
data = {
    101: 45,
    102: 65,
    103: 72,
    104: 30,
    105: 61
}

s = pd.Series(data)

print("Average Age:", s.mean())
print("Oldest Patient ID:", s.idxmax())
print("Oldest Age:", s.max())
print("Youngest Patient ID:", s.idxmin())
print("Youngest Age:", s.min())

print("\nPatients above 60 years:")
print(s[s > 60])

#Q12
df = pd.read_csv("students.csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("\nTotal and Average Marks:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with Average above 75:")
print(df[df["Average"] > 75])

print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage Marks of Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())

