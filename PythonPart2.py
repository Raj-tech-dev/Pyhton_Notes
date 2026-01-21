# Concepts : Conditional Statements, Loops & Functions

# There are 3 main conditional statements in Python:
# 1. if - used to test a condition. If it’s True, the indented block runs.
# 2. else - else block runs if all above conditions are false.
# 3. elif - (“else if”) used when we have multiple conditions to check

#Practice
name = int(input("Enter your age: "))
if(name>18):
    print("You can vote")
else:
    print("You can not vote")

#traffic light practise
color = input("choose a color: ")
if(color == "green"):
    print("you can go")
elif(color == "yellow"):
    print("ready to go")
elif(color == "red"):
    print("Stop")
else:
    print("you choose wrong color")

'''Note - We can have standalone & multiple if statements but elif & else
can’t be used without an statement preceding them.

Apart from simple conditions we can also check for multiple conditions using Logical 
operators like , and in expressions'''

#Exampe
age = int(input("Enter Your age: "))
if(age < 13):
    print("child")
elif(age>13 and age<18):
    print("Teenager")
else:
    print("adult")

# Nesting in Conditionals
# Nesting means placing one block of code inside another.

#Example
user_name = input("Enter your user_name: ")
password = int(input("Enter your password:"))
if(user_name == "admin" and password == 123):
    print("login Succesfull")
else:
    if(user_name != "admin"):
        print("Wrong user_name, try again.")
    else:
        print("wrong password, try again.")


# Ternary Statements
# just another compact way to writing our statements in one-line.
# Ternary statement Syntax:
# value_if_true if condition else value_if_false

#Example
age = 18
status = "Adult" if age >= 18 else "Not Adult"
print(status)
# Note---
# Ternary statements are generally only used for 
# simple conditions, not recommended for nested or complex conditions


# Match Case Statements
'''In Python, the / statements are an alternative to long chain of
 if, else, elif statements. They were introduced in Python 3.10 & we generally don’t
see them much in production code'''

# # Match Case Syntax
'''match variable: 
 case pattern1: 
      # code to run if pattern1 matches 
 case pattern2: 
     # code to run if pattern2 matches 
 case _: 
    #  default case (like 'else')'''
#Example:
color = input("Choose a color: ")
match color:
    case "red":
        print("stop")
    case "Yellow":
        print("look")
    case "Green":
        print("go")
    case _:
        print("wrong color")

# # practice problem
# 1. For a given number , print if it’s a multiple of 5 or not.
# 2. For a given number , print if it’s Odd or Even.

#Que 1
num = int(input("enter a number: "))
if(num%5 == 0):
    print(f"{num} is multiple of 5.")
else:
    print(f"{num} is not multiple of 5")

#Que 2
number = int(input("enter a number: "))
if(number%2 == 0):
    print(f"{number} is even number.")
else:
    print(f"{number} is odd number")

#Loops
"""
A loop lets us execute a block of code multiple times: either a set number of 
times or until a condition is met.
Python has 2 main types of loops:
1. while loop - repeat while a condition is
2. for loop - iterate over a sequence (like a list, string, or range)
"""

# The while loop 
"""
Syntax of a loop:
while condition:
# code block
"""
# Example
# print 1 to 10 number
n = 1
while n<10:
    print(n)
    n += 1
# print 10 to 1
n = 10
while n >1:
    print(n)
    n -= 1

# Loop control statements
"""Python gives us some tools to control how loops behave & a classical example of 
them are 2 statement - & ."""

# The (break) keyword
"""It stops the loop immediately."""
i = 1
while i<10:
    if(i%6 == 0):
        break
    print(i)
    i += 1

# The continue keyword
"""It skips the rest of the current iteration and moves to the next one"""
# Skip multiples of 3
i = 0
while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue
    print(i)
 # output: 1, 2, 4, 5, 7, 8, 10

#  The for Loops
"""In Python, a for loop is used to iterate (loop) over a sequence, such as a list, tuple, 
string, or range, and execute a block of code for each item in that sequence."""
# Syntax of a for loop:
"""
for variable in sequence:
  code to run for each item
"""
#Example
for i in range(5):
    print(i)

"""
The (in) keyword that we used is a membership operator in Python, used to loop 
over a sequence or to check the presence of an item in a sequence, like a string."""

#Example
word = "prime"
# Example 1 - Looping over a string
for ch in word:
 print(ch)

# Example 2 - Check if char 'i' exists in word 
if 'i' in word: 
 print("letter exists")
# Example 3 - Count number of i's in the word
word = "artificial intelligence"
count = 0
for ch in word:
 if ch == 'i':
    count += 1
print(f"i occurs {count} times.")



