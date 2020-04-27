# introduction of python
#Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
#The syntex of python is very easy as compared to other programming language.

#indentation.
#the indentation in Python is very important.it reffers at the biggining of line.
if 5 > 2:
  print("Five is greater than two!")
# if we skip the indentation. python will give us error
if 5 > 2:
 print("five is greater than two!")

# VARIABLES
# variables are used for temporary storage of data that may change
# a single equals sign is the assignment operator
age = 18
first_name = 'Aqeela'
gpa = 3.98

#  we have three different types of data stored in variables: an integer, a string, and a float.
# we do not have to declare the data type stored in each variable.
# we can see what type of data is in a variable using the type() function
print(type(age))
print(type(first_name))
print(type(gpa))
#variable Name
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
#A variable name cannot start with a number
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#correct variabnle names:
myvar = "John"
my_var = "John"
_my_var = "browao"
myVar = "Delta"
MYVAR = "Charli"
myvar2 = "Alpha"

#Python allows us to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#And we can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)
# in python we cannot add numbers in string
#----------------
#String
#String can be written in python with single or dubble code.
#'hello' is the same as "hello".
#we can display a string item by using print() function:
print("Hello")
print('hello')
#multiple string
#we can assign a multiline string to a variable by using three quotes:
a ="""A computer is an electronic device
computer cannot understand human language
we use compiler for translate the language"""
print(a)
# string in an arrey
#-------------
#we use square brakits to get a specific cheracter in python
a = "Aqeela Shaheen"
print(a[4])
#we can specify the range of index
a = "Aqeela Shaheen"
print(a[4:8])
# nagitive index start from the end
#we can find the length of string by using len() function:

#Boolean values.
#Booleans represent one of two values: True or False.
# These all evaluate to False: 0, 0.0, [], "", None
# These are all True: any non-zero number, any non-empty string, list or set
#True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#-----------
# Operators
#Operators are used to perform operations on variables and values.

#Python divides the operators in the following groups:
#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators
#Arthmatic operator :
# + for addition, - for subtrection, * for multiplication, / for division,% for modulus, ** for Exponentiation, // for Floor division
#logical operator.
#And operator: it give true when both condition are true.
#or operator:  it give true when any one condition is true.
#not operator: it reverse the result. when result is false it give true and when result is true it return false.

#List
#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

a = ["APPLE","Banana","Mango"]       #seperated list item with comma
print(a)
# we access item in the list by using index number.
a = ["Apple","Banana","mango"]
print(a[2])           #print 'mango'
#Nagitive indexing start from end of the list.if we access -1 it print the last aitem of the list.
x = ["goat","cat","dog"]
print(x[-1])       #print 'dog'
#we can also specify the range of index
Names = ["Aqeela","Tanzeela","Ayesha","Haleema","Aqsa","sara"]
print(Names[2:4])         #print 'Ayesha','Haleema'
   #change item in a List.
#To change the value of a specific item, refer to the index number:
x = ["Aqeela","Aqsa","Haleema"]
x[0] = "Tanzeela"
print(x)          #print 'Tanzeela','Aqsa','Haleema'
# Slicing -- slice out substrings, sublists, subtuples using indexes
# [start : end+1 : step]
x = 'beautiful'
print(x[1:4])			# items 1 to 3, 'eau' index 4 not access
print(x[1:6:2])			# items 1, 3, 5, 'eui'
print(x[3:])			# items 3 to end, 'utiful'
print(x[:8])			# items 0 to 7, 'beautifu'
print(x[-1])			# last item, 'l'
print(x[-3:])			# last 3 items, 'ful'
print(x[:-2])			# all except last 2 items, 'beautif'
# Adding   -- combine 2 item of the same type using +
x = 'cat' + 'dog'
print (x)				# prints 'catdog'

x = ['pec', 'cow'] + ['lion']
print (x)				# prints ['pec', 'cow', 'lion']
# Multiplying -- multiply a list using *
x = 'dog' * 3
print (x)				# prints 'dogdogdog'

x = [2, 5] * 2
print (x)				# prints [2, 5, 2, 5]
#checking item in the list.
x = 'cat'
print('t' in x)         #print true
# Iterating	-- iterate through the items in a list
x = [7, 8, 3]
for item in x:       #using for loop
 print (item * 3)	# prints 21, 24, 9
# Length -- count the number of items in a list we use len() function
x = 'dog'
print(len(x))     # prints

#add item by using append method
x =["dog","cat","goat"]
x.append("hourse")
print(x)      #print 'dog','cat','goat','hourse'
#remove item from list
x = ['cow','dog','cat','hourse','elephant']
x.remove("hourse")
print(x)     #print 'cow','dog','cat','elephant'
#another method is to remove item from list and that iss pop() method
#it remove item by reffering index
x = ['cow','dog','cat','hourse','elephant']
x.pop(2)
print(x)        #print 'cow','dog','hourse','elephant'
#join two list__ with = operator and extend() method
a = ['name','place','person']
b = ['a','b','c']
c = a + b
print(c)     #print'name','place','person','a','b','c'

a = ['name','place','person']
b = ['a','b','c']
a.extend(b)
print(a)     #print'name','place','person','a','b','c'

#tuple
#---------------------
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
tuple = {'cow','dog','cat'}
print(tuple)         #print 'cow','dog','cat'
#tuples are imuitable.

#set
#-----------------
#sets are unorder and unindexed
#sets are written with curly brakits {}
set = {"cat","dog","goat"}
print(set)    #sets are unorderd so we cannot specify the order
#checking item ---- using in keyword
x = {"cow","cat","dog"}
print("cat" in x)     # print true
#add multiple item=---- using update() function
a = {'car','bike','cycle'}
a.update(['cat','cow','dog'])
print(a)     #print 'car', 'bike', 'dog', 'cat', 'cow', 'cycle'

#Dictionary
#----------------
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
dict = {
    'car': 'hunda',
    'owner': 'Abubaker',
    'year': 2020
 }
print(dict)    #print 'car': 'hunda', 'year': 2020, 'owner': 'Abubaker'
#access item-----
#we access item by using keyword inside with square brakits[]
dict = {
    'car': 'hunda',
    'owner': 'Abubaker',
    'year': 2020
}
x = dict['owner']
print(x)
#add item--
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
dict = {
    'car': 'hunda',
    'owner': 'Abubaker',
    'year': 2020
}
dict['colour'] = 'red'
print(dict)   #print'car': 'hunda', 'owner': 'Abubaker', 'year': 2020, 'colour': 'red'

#Python Conditions and If statements
#--------------------
#Python supports the usual logical conditions from mathematics:

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Greater than: a > b
#Greater than or equal to: a >= b
#These conditions can be used in several ways, most commonly in "if statements" and loops.

#An "if statement" is written by using the if keyword.
a = 20
b = 13
if a>b:
    print("true")
#Elif
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 10
b = 5
if a > b:
    print("true")
elif a==b:
    print("a is equal to b")   #print true
#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 15
b = 10
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
   print("false")    #print false
#Short Hand If
#If we have only one statement to execute, we can put it on the same line as the if statement.
a = 10
b = 5
if a > b:print("a is greater than b")    #print  a is greater than b
#short hand else ----- multiple else
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#And
#The and keyword is a logical operator, and is used to combine conditional statements
a = 20
b = 5
if a > b and b < a:
    print("both condition are true")     #print both condition are true
#Nested If
 #we have if statements
#inside if statements,
#this is called nested if statements.

x = 41

if x > 10:
    print("Above ten,")     #print above ten
    if x > 20:
        print("and also above 20!")     #print and also above 20
    else:
        print("but not above 20.")

# if ternary
x = 10
y = 20
#  action/ if condition true/ else condfition false
z = x + y if x > y else y - x
print(z)
# result 10
# STRINGS
# ------------------------------------------------
# a string is a sequence of characters (ie. text)
s = 'shirt'
print(s)
print(len(s))
print(s[3])
print(s[1:3])
t = ' single! '
s += t
print(s + '|')
print(s.strip() + '|')
s = s.rstrip('! ')
print(s)

s = 'shirt single!'
print(s.lower())
print(s.upper()[:5])
print(s.title())
print(s.replace('Howdy', 'Greetings'))
print(s)
print(s.count('d'))
print(s.find('w'))
print('dud' in s)
print('X' not in s)
print(s.startswith('How'))
print(s.endswith('cat'))
print(s > 'Honk')
print(s.isalpha())
print(s[0:4].isalpha())
print(s.isnumeric())
print(s.split())
print('5,7,9'.split(','))
print('73.294'.split('.'))
print(s[0], '\t', s[1], '\t', s[2])
print(s[:s.find(' ')] + '\n' + s[s.find(' ')+1:])
# LOOPS -- FOR, WHILE
# ------------------------------------------------
# used to iterate through the items of a string or list
# indention is important.
# every statement indented from for will be executed each iteration
x ='student'
for student in x:
    print(student)
for student in x:
    print(student ,end = '' )
    print()
#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:
fruit = ("Apple","banana","cherry")
for x in fruit:
 if x == "banana":
     break
print(x)      #print'banana'
#range function
for x in range(1,5):
    print(x)
#while loop-----
#With the while loop we can execute a set of statements as long as a condition is true.
x = 2
while x < 5:
    print('yes')
    x += 1

# FUNCTIONS
# ------------------------------------------------
# use the def keyword to create a function
# give the function a name, followed by parentheses and a colon
# we can pass in 0 or more variables. here we pass in num.
# we can return 0 or more variables. here we return the cube of num
# indention is important.
def square(num):
 num_squared = num * num
 return num_squared

# to call the function, and pass in 5:
square(5)

# but if we want to assign the return value (125) to a variable,
x = 5
x_squared = square(x)
print(x, x_squared)
# we can set default values for parameters
def square(num=2):
    num_squared = num * num
    return num_squared
print(square())  # uses the default 2
print(square(3))  # 3 overrides the default

# we can pass in multiple values, and return multiple values
# but order is important
def solve_triangle(base, height, side1, side2, side3):
    area = base * height / 2
    perimeter = side1 + side2 + side3
    return area, perimeter

area, perim = solve_triangle(2, 7, 6, 4, 2)  # b=3, h=4, s1=5, s2=3, s3=4
print('Area:', area, ' Perimeter:', perim)

# above are all called "positional arguments", and order matters
# you can also pass in "keyword arguments" when calling a function
a, p = solve_triangle(side1=6, side2=4, side3=2, height=7, base=2)
print(a, p)

# or use a combination of both, but positional arguments must come first
a, p = solve_triangle(2, 7, side3=2, side2=4, side1=6)
print(a, p)


# CLASSES & OBJECTS
# ------------------------------------------------
# Use classes to model real-world things.
# Keep related data (variables) and actions (functions) in one block of code.
class Circle:
    # Circle constructor -- __init__ method creates a new Circle object
    def __init__(self, r=1):
        self.radius = r

    def getPerimeter(self):
        return 2 * self.radius * 3.14

    def getArea(self):
        return self.radius ** 2 * 3.14


# all methods have the self parameter, which is Python's reference to the object that invoked the method

# this calls the __init__ method, which creates the new Circle
circle1 = Circle(3)
# you can access the circle's attributes and methods using the dot operator
print("Radius =", circle1.radius)
print("Perimeter =", circle1.getPerimeter())

# IMPORTS
# ------------------------------------------------
# Python has many many classes already written that you can use
# To access methods and data from another class you must import it
import math

print(math.pi)

import random

print(random.randint(1, 5))

# shorter version, using as to abbreviate module name
import math as m

print(m.pi)

import random as rd

print(rd.randint(1, 5))

# import just one or two functions or constants rather than a whole module
# easier for coding, but need to beware names don't conflict
from math import pi

print(pi)

from random import randint, shuffle

print(randint(1, 5))
x = ['a', 'b', 'c']
shuffle(x)
print(x)

# can rename an imported function if you want
x = ['a', 'b', 'c']
from random import shuffle as sf

sf(x)
print(x)

# can also import whole module using *
from random import *

print(randint(1, 5))




