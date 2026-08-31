#Q1
file1 = open("student.txt", "w")
name = input("Enter name: ")
r_no = input("Enter roll no: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")
file1.write(name) 
file1.write(r_no) 
file1.write(branch) 
file1.write(sem) 
file1.close()

#Q2
file2 = open("student.txt","r")
content = file2.readlines()
print(content)
file2.close()

#Q3
with open("student.txt","a") as file3:
    name = input("Enter name: ")
    r_no = input("Enter roll no: ")
    branch = input("Enter branch: ")
    sem = input("Enter semester: ")
    file3.write(name) 
    file3.write(r_no)   
    file3.write(branch) 
    file3.write(sem)
    
#Q4
with open("demo.txt") as file4:
    content = file4.readlines()
    print(content)
    
#Q5
with open("demo.txt") as file5:
    content = file5.readlines()
    cnt = 0
    while content:
        cnt += 1
    print(cnt)

#Q6
with open("demo.txt") as file7:
    cntw = 0
    for word in file7.readlines():
        cntw += 1
    print("Count of words = ",cntw)
    
#Q7
with open("demo.txt") as file8:
    cntch = 0
    for i in file8.read():
        cntch += 1
    print("Count of characters = ",cntch)

#Q9
with open("demo.txt") as file6:
    cntv = 0
    cntc = 0
    for i in file6.read():
        if i.lower() in "aeiou":
            cntv += 1
        else:
            cntc += 1
    print("Vowel count = ",cntv)
    print("Consonant count = ",cntc)

#Q16
file9 = open("demo.txt")
content = file9.read()
file10 = open("demo1.txt","w")
file10.write(content.upper())
file9.close()
file10.close()

#Q17
file11 = open("demo2.txt","w+")
file11.write("Rollno, Name, Marks\n")    
file11.write("101, Amit, 85\n")    
file11.write("102, Priya, 92\n")    
file11.write("103, Rahul, 78\n")
content = file11.readlines()
print(content)
file11.close()

