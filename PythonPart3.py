# Concepts : String, List, Tuple, Dictionary & Set
"""
In this chapter we are going to dive deep 
into some of the not-so-simple data types of
Python.
"""
# Strings
"""
What is a String?
A string in Python is a sequence of characters enclosed in quotes:
Strings are immutable, meaning once created, their contents can't be 
changed directly.
"""
# Example
str1 = "hello world"
str2 = 'Prime'
# len() function // to print the lenght of string
word = "Rsjkusr"
print(len(word)) #7 lenght

str1  = 'raj'
str2 = 'kumar'
concate = str1+str2
print(concate)
#  loop in string
s = 'python'
for c in s:
    print(c)

# Indexing in Strings
"""
Indexing lets us access individual characters in
a string.
"""

# example
w = 'rajkumar sharma'
print(w[5])
print(w[0])
print(w[-1])

# Slicing in Strings
"""
Slicing is a powerful feature of Python that lets us access
multiple elements at once. We can do slicing in strings & 
even on other sequences like lists & tuples.
The general syntax for slicing a string is:
string[start : end : step]
start -> include
end -> exclude
step -> default 1
"""
# Example
s = "Python"
print(s[0:2]) # 'Py'
print(s[2:]) # 'thon'
print(s[:3]) # 'Py t' 
print(s[::2]) # 'Pto' (every second char) 
print(s[::-1]) # 'nohtyP' (reversed string)

# String Formatting
# 1. Using .formate()
""""
In this way we use  {} as placeholders & pass placeholder replacement values in the
format function.
"""
# example
name = "Rahul" 
age = 25 
text = "My name is {} and I am {} years old".format(name, age) 
print(text)

# We can also use positional & named placeholders:
"Coordinates: {1}, {0}".format("x", "y") # 'Coordinates: y, x'
"Name: {n}, Age: {a}".format(n="Bob", a=30)

# 2. Using f-strings (Python 3.6+)
"""
F-strings are concise, readable & will be our preferred way going forward.
In f-strings we prefix the string with and put our variable or expressions inside .
"""
# Example
name = "Rahul" 
age = 25 
text = f"My name is {name} and I am {age} years old" 
print(text)

# Lists
"""
Lists are collection of items in python.
item  in list are mutable(changable), ordered, and can obtain duplicate value.
Lists can hold any data type like number, string, lists also.
lists are written using square brackets []
"""
# Example
my_list = [1, 2, 3, 4, 5] 
print(my_list) 
print(type(my_list)) # <class 'list'>
my_list2 = [10, "Hello", 3.14, True, 10] # heterogenous list
print(my_list2)

# Lists Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Simple Slice
print(numbers[2:5]) # Output: [2, 3, 4]
print(numbers[:4]) # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[5:]) # Output: [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[:]) # Output: [0,1,2,3,4,5,6,7,8,9] (copy of the whole list)
# using STEP
print(numbers[::2]) # Output: [0, 2, 4, 6, 8] (every2nd element)
print(numbers[1::3]) # Output: [1, 4, 7] (start at 1, every 3rd element) 
# NEGATIVE slice 
print(numbers[-5:-2]) # Output: [5, 6, 7] (negative indexing from end)


# Tuples
"""
What is a Tuple?
A tuple in Python is an ordered, immutable collection of items.
"""
# Example
tup = (10, 20, 30) 
print(tup) 
print(type(tup)) # < class 'tuple'> 
empty_tuple = ()  #empty tuple
single_element_tuple = (42,)
# Tuple Methods

# Let’s have a look at some of tuple methods
# index() - return index of first occurence for any
# count() return  total count of occurrence for any val
t = ( 1 , 2 , 2 , 3 , 5 )
print(  t .index(  2 )) # 1
print(  t .count(  2 )) # 3

# Dictionaries
# What is a Dictionary?
# A dictionary is an unordered, mutable collection of  key -v alue pairs .
#  Example:
my_dict = {
 "name": "Shradha",
 "age": 30,
 "city": "Delhi"
}

# Dictionary Characteristics
"""
1. Dictionary Keys must be unique
2. Dictionary Keys must be immutable (e.g., strings, numbers, tuples)
3. Dictionary is mutable.
4. Dictionary values can be anything (lists, other dictionaries, etc.)
5. Unordered (although in modern Python, dictionaries preserve insertion order)
"""
"""
keys() - returns all key
values() returns all values
items() returns key_value pairs as tuples
get(key) a safer way to access value of a particular key
update(new_item) - adds a new item to the dictionary
"""

d = { 
 "name": "Shradha",
 "subjects": ["math", "science", "physics"], 
 "cgpa": 9.5 
} 

print(d.keys()) # dict_keys 
print(d.values()) # dict_values 
print(d.items()) # dict_items
print(d.get("cgpa2")) # return None as no such key as "cgpa2" 
new_item = {"city": "Delhi"} 
print(d.update(new_item)) 
print(d)

# Loops on Dictionary
d = { 
 "name": "Shradha",
 "subjects": ["math", "science", "physics"], 
 "cgp a": 9.5 
} 
for key, value in d.items(): 
 print(key, value)

#  Sets
"""
What is a Set?
A set is an unordered collection of unique elements
"""
my_set = {1, 2, 2, 2, 3} 
print(my_set) # {1, 2, 3} 
print(type(my_set)) 
print(len(my_set)) # 3
"""
Set Characteristics
1. Sets can only have unique elements.
2. They are unordered - no indexing or slicing.
3. They are mutable - we can add or remove elements.
4. Set elements must be immutable (like strings, numbers, tuples)
"""

# Note->Sets are often used when we need uniqueness or mathematical set 
# operations.

# Set Methods
# Let’s have a look at some of the important set methods:

"""
add(val) - adds an element to set
remove(val)- removes an element (raises error if not found)
clear() -removes all elements
pop() -removes and returns a random element (since sets are unordered)
s1.union(s2)-returns new union (union is collection of all unique values in both 
sets)
s1.ntersection(s2)-returns new union (intersection is collection of all common&
uniquevalues inbothsets)

"""
# Example
s = {10, 20, 30} 
s.add(40) # {10, 20, 30, 40} 
print(s) 
s.remove(10) # {20, 30, 40} 
print(s) 
print(s.pop()) # can be any value 
s.clear() 
print(s) # set() - empty set 
# Union & Intersection 
A = {1, 2, 3} 
B = {3, 4, 5} 
print(A.union(B)) # {1, 2, 3, 4, 5}
print(A.intersection(B)) # {3}