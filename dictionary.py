# Q1
person = {"name": "Aarav", "age": 21, "marks": 92}
print("Q1 - Person details:", person)

# Q2
details = {"name": "Sneha", "age": 20, "city": "Pune"}
print("Q2 - Name:", details["name"])
print("City:", details["city"])

# Q3
learner = {"name": "Kunal", "age": 19}
learner["course"] = "Java"
print("Q3 - Updated dictionary:", learner)

# Q4
record = {"name": "Meera", "marks": 78}
record["marks"] = 95
print("Q4 - Updated dictionary:", record)

# Q5
worker = {"name": "Arjun", "age": 26, "salary": 35000}
worker.pop("age")
print("Q5 - Updated dictionary:", worker)

# Q6
profile = {"name": "Riya", "age": 22, "marks": 89}
print("Q6 - Keys:", list(profile.keys()))
print("Values:", list(profile.values()))

# Q7
student_info = {"name": "Dev", "age": 20, "grade": "A"}
if "grade" in student_info:
    print("Q7 - Key exists")
else:
    print("Q7 - Key does not exist")

# Q8
subject_marks = {"Physics": 88, "Chemistry": 91, "Biology": 84}
total_marks = sum(subject_marks.values())
print("Q8 - Total marks:", total_marks)

# Q9
word = "apple"
char_count = {}
for letter in word:
    char_count[letter] = char_count.get(letter, 0) + 1
print("Q9 - Character frequency:", char_count)