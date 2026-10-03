name = "Diwakar"
age = 24
weight = 55.5
is_he_student = False

print(type(is_he_student))

age_float = float(age)
print(age_float)

s= 100
print(int(s)+age)

a=10
b=11

a=a+b
b=a-b
a=a-b
print(a,b)

x=5
y=6

temp=x
x=y
y=temp
print(x,y)

p=1
q=2
p,q = q,p
print(p,q)

# Homework

# Arithmetic Practice: Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. Define the two numbers as variables within the code and print the results for each operation.

a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)

# Swap Two Variables: Write a Python program that swaps the values of two variables with and without using a third variable.

a = 5
b = 10

temp = a
a = b
b = temp
print(a, b)  # Output: 10 5

 