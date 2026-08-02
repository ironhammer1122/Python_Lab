n = 10

#Q1
for i in range(1,n + 1):
    print(i)
    
#Q2
for i in range(1,n + 1):
    if i % 2 == 0:
        print(i)

#Q3
for i in range(1,n + 1):
    if i % 2 != 0:
        print(i)
        
#Q4
for i in range(1,n + 1):
    value = 2 ** i
    if value > n:
        break
    print(value)
    
#Q8
for i in range(3):
    print("A B C")
    
#Q9
num = int(input("Enter a number: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1, num + 1):
    for j in range(i):
        print(letters[j], end="")
    print()
    
#Q10
num1 = int(input("Enter a number: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(num1, 0, -1):
    for j in range(i):
        print(letters[j], end="")
    print()
    
#Q11
num2 = int(input("Enter a number: "))
for i in range(1, num2 + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
#Q12
num3 = int(input("Enter a number: "))
for i in range(1, num3 + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()