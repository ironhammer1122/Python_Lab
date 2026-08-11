# Q1
fruits = ["Apple", "Mango", "Orange", "Kiwi", "Pineapple"]
print("Q1 - Fruits:", fruits)


# Q2
numbers = [15, 25, 35, 45, 55]

print("\nQ2 - First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# Q3
colors = ["Red", "Green", "Yellow", "Blue", "White"]

colors[2] = "Purple"

print("\nQ3 - Updated list:", colors)


# Q4
values = [15, 25, 35, 45]

values.append(55)
values.insert(0, 5)
values.insert(3, 30)

print("\nQ4 - Updated list:", values)


# Q5
names = ["Akash", "Neha", "Riya", "Karan", "Vishal"]

names.pop(0)
names.pop()
names.remove("Riya")

print("\nQ5 - Remaining students:", names)


# Q6
values = [35, 15, 50, 8, 25]

largest = values[0]
smallest = values[0]

for value in values:
    if value > largest:
        largest = value

    if value < smallest:
        smallest = value

print("\nQ6 - Largest:", largest)
print("Smallest:", smallest)


# Q7
values = []

for i in range(10):
    value = int(input("\nQ7 - Enter number: "))
    values.append(value)

total = sum(values)
average = total / len(values)

print("Sum:", total)
print("Average:", average)


# Q8
values = [12, 25, 34, 47, 56, 63, 72, 81, 90, 17, 28, 39, 44, 51, 68]

even_count = 0
odd_count = 0

for value in values:
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nQ8 - Even numbers:", even_count)
print("Odd numbers:", odd_count)


# Q9
places = ["Delhi", "Mumbai", "Pune", "Jaipur", "Surat"]

place = input("\nQ9 - Enter city name: ")

if place in places:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")


# Q10
values = [5, 10, 15, 20, 25]

reversed_values = values[::-1]

print("\nQ10 - Original:", values)
print("Reversed:", reversed_values)


# Q11
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]

print("\nQ11 - First 5 elements:", values[:5])
print("Last 5 elements:", values[5:])
print("Middle 4 elements:", values[3:7])
print("Alternate elements:", values[::2])
print("Reverse list:", values[::-1])


# Q12
values = [12, 24, 36, 48, 60, 72, 84, 96]

print("\nQ12 - Elements at even index positions:")

for index in range(len(values)):
    if index % 2 == 0:
        print(values[index])


# Q15
values = [15, 35, 55, 25, 65, 45]

distinct_values = []

for value in values:
    if value not in distinct_values:
        distinct_values.append(value)

distinct_values.sort()

print("\nQ15 - Second largest:", distinct_values[-2])


# Q16
student_data = [
    ["Rohit", 201, 78],
    ["Anjali", 202, 91],
    ["Varun", 203, 84],
    ["Meera", 204, 95]
]

print("\nQ16 - Student Details:")

for student in student_data:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# Q23
values = [15, 25, 15, 35, 25, 15, 45]

count = {}

for value in values:
    if value in count:
        count[value] += 1
    else:
        count[value] = 1

print("\nQ23 - Frequency:", count)


# Q25
values = [15, 25, 15, 35, 25, 45, 35, 55]

distinct_values = []

for value in values:
    if value not in distinct_values:
        distinct_values.append(value)

print("\nQ25 - List after removing duplicates:", distinct_values)