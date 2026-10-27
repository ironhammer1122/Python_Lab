import re
# Q1
data1 = "My phone number is 9876543210"
digits = re.findall(r'\d', data1)
print("Q1 - Digits:", digits)

# Q2
data2 = "An apple and an ant are around"
words = re.findall(r'\b[Aa]\w*', data2)
print("Q2 - Words starting with A:", words)

# Q3
data3 = input("Q3 - Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', data3)
print("Number of vowels:", len(vowels))

# Q4
data4 = "Welcome To PYTHON Programming"
capital_letters = re.findall(r'[A-Z]', data4)
print("Q4 - Uppercase letters:", capital_letters)

# Q5
data5 = "Good Morning\tStudents\nWelcome"
whitespace = re.findall(r'[ \t\n]', data5)
print("Q5 - Whitespace characters:", whitespace)
print("Total whitespace:", len(whitespace))

# Q6
data6 = "Python     is    very     useful"
clean_text = re.sub(r' +', ' ', data6)
print("Q6 - Updated text:", clean_text)

# Q8
data8 = "Lions tigers birds and rabbits"
ending_words = re.findall(r'\b\w+s\b', data8, re.IGNORECASE)
print("Q8 - Words ending with s:", ending_words)

# Q9
data9 = "Python@123 is# easy!"
simple_text = re.sub(r'[^A-Za-z0-9 ]', '', data9)
print("Q9 - Clean text:", simple_text)

# Q10
data10 = "Regular expressions are useful in Python"
word_list = re.findall(r'\b\w+\b', data10)
print("Q10 - Number of words:", len(word_list))

# Q12
email_id = input("Q12 - Enter email address: ")
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if re.fullmatch(email_pattern, email_id):
    print("Valid email")
else:
    print("Invalid email")

# Q16
user_password = input("Q16 - Enter password: ")
password_pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}'
if re.fullmatch(password_pattern, user_password):
    print("Strong password")
else:
    print("Weak password")
