n = 50

#Q1
i = 1
while i <= n:
    print(i)
    i += 1    
    
#Q2
while n < 50:
    if n % 2 == 0:
        print(n)
    n += 1
    
#Q3
while n < 50:
    if n % 2 != 0:
        print(n)
    n += 1
    
#Q4
s = 0
while n < 50:
    s += n
    n += 1
print(s)

#Q5
a = 0
while n < 50:
    if n % 2 != 0:
        a += n
    n += 1
print(a)

#Q6
b = 0
while n < 50:
    if n % 2 == 0:
        b += n
    n += 1
print(b)

#Q7
while n >= 1:
    print(n)
    n -= 1

#Q8
c, d = 0, 1
while c <= 50:
    print(c)
    c, d = d, c + d
    
#Q9
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)

#Q10
num1 = int(input("Enter a number: "))
is_prime = True
if num1 <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= num1:
        if num1 % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(num1, "is a prime number")
else:
    print(num1, "is not a prime number")
    
#Q11
num2 = int(input("Enter a number: "))
sum_of_digits = 0
while num2 > 0:
    sum_of_digits += num2 % 10
    num2 //= 10
print("Sum of digits:", sum_of_digits)

#Q12
num3 = int(input("Enter a number: "))
original_num = num3
reversed_num = 0
while num3 > 0:
    digit = num3 % 10
    reversed_num = reversed_num * 10 + digit
    num3 //= 10

if original_num == reversed_num:
    print(original_num, "is a palindrome")
else:
    print(original_num, "is not a palindrome")
    
#Q13
num4 = int(input("Enter a number: "))
reversed_num4 = 0
while num4 > 0:
    digit = num4 % 10
    reversed_num4 = reversed_num4 * 10 + digit
    num4 //= 10
print("Reversed number:", reversed_num4)