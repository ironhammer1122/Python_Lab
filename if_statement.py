#Q1
n = int(input("Enter a number: "))
if n == 0:
    print("The number is zero.")
else:
    print("The number is not zero.")
    
#Q2
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
if a > b:
    print("The first number is greater.")
else:
    print("The second number is greater.")
    
#Q3
c = int(input("Enter a number: "))
if c >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")
    
#Q4
ch = input("Enter a character: ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")
    
#Q5
per = float(input("Enter percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")
    
#Q6
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The first number is the largest.")
elif num2 >= num1 and num2 >= num3:
    print("The second number is the largest.")
else:
    print("The third number is the largest.")
    
#Q7
num4 = int(input("Enter first number: "))
num5 = int(input("Enter second number: "))
num6 = int(input("Enter third number: "))
if num4 <= num5 and num4 <= num6:
    print("The first number is the smallest.")
elif num5 <= num4 and num5 <= num6:
    print("The second number is the smallest.")
else:
    print("The third number is the smallest.")
    
#Q8
num7 = int(input("Enter a number: "))
if num7 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
#Q9
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
#Q10
married = input("Married? (yes/no): ")
gender = input("Gender (male/female): ")
age = int(input("Enter age: "))

if married == "yes":
    print("Driver is Insured")
elif married == "no" and gender == "male" and age > 30:
    print("Driver is Insured")
elif married == "no" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")