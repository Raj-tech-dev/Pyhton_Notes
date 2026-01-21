print("hello world!")
print("Hi raj, Now you have written your first programme in python")
print(5+4)
print(30.14)
print("Hi", "raj") # print multiple satement in single line

#Variable
name = "Raj Kumar "
age  = 30
PI = 3.14
word = "AI"
print("Value of PI", PI)

#type function & diff type of data type
x = 10   # int data tyep
print(type(x))

y = "Raj" # string data type
print(type(y))

z = 3.14  # float data type
print(type(z))

isTeacher = True #boolean data type
print(type(isTeacher))

empty_var = None # None data type
print(type(empty_var))

#Type Conversion & type casting
# Two types of Type conversion, 
#1st Implicit conversion, which python done autometically
#Example
a = 5
b = 3.14
print(a+b) #python converts its result in float by default

#2nd Explicitly, which done by programmer
# exampe
x = 10  #int
y = float(x)  #float
z = str(x)  #string
print(x,y,z)

#Operators

# 1st Arithmetic Operator-> +, -, *, /, %, **
a = 5 
b = 10
print(a + b) # Addition 
print(a - b) # Subtraction 
print(a * b) # Multiplication 
print(a / b) # Division 
print(a % b) # Modulo - remainder
print(a ** b) # Power

# 2nd Relational Operators-> ==, !=, >, <, <=, >=
a = 10
b = 20
# Equal to
print("a == b:", a == b) # False
# Not equal to
print("a != b:", a != b) # True
# Greater than
print("a > b:", a > b) # False
# Less than
print("a < b:", a < b) # True
# Greater than or equal to 
print("a >= b:", a >= b) # False 
# Less than or equal to 
print ("a <= b:", a <= b) # True

# 3rd Assignment Operator(use to assign value to a variable)->= += -= *= /= %= **=
# Simple assignment
x = 10
print("x =", x) # 10
x += 5 # equivalent to x = x + 5
print("x += 5 ->", x) # 15
x -= 3 # equivalent to x = x - 3
print("x -= 3 ->", x) # 12
x *= 2 # equivalent to x = x * 2
print("x *= 2 ->", x) # 24 
x /= 4 # equivalent to x = x / 4 
print("x /= 4 ->", x) # 6.0 
x %= 4 # equivalent to x = x % 4 
print("x %= 4 ->", x) # 2.0 
x **= 3 # equivalent to x = x ** 3 
print("x **= 3 ->", x) # 8.0

# 4th Logical Operator-> and, or, not 
x = 10 
y = 20 
z = 5 
# AND 
print(x > z and y > x) # True (when both value true)
# OR 
print(x > y or y > z) # True  (any single value true)
# NOT 
print(not (x > y)) # True 

# Operator Precendence

# Operators have a priority;
# order is as follows:

#  Parentheses (highest priority)           -> ()
# Exponent                                  -> **
# Unary operators                           -> +x, -x, ~x
# Multiplication, division, floor, modulus  -> / // %
# Addition, subtraction                     -> + -
# Bitwise shifts                            -> << >>
# Bitwise AND                               -> &
# Bitwise XOR                               -> ^
# Bitwise OR                                -> |
# Comparison operators -                    -> <, <=, >, >=, !=, ==
# not
# and
# or
# Assignment operators                     -> =, +=, -= ......


# Input function
# input()
# We use the function to take input from user

# Syntax:
name = input("enter name: ") 
print(name) 
print(type(name)) # type is string

a = int(input("enter 1st num: ")) # 5
b = int(input("enter 2nd num: ")) # 10
avg = (a + b) / 2
print("average = ", avg) # 7.5
