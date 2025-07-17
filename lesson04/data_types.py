#string data type
#literal assign of values

first ="Kens"
last = "Hizer"

# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))


#constructor

# pizza= (str("Pepperoni"))
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str)) 

fullname = first + " " + last
print (fullname)

fullname+="!"
print(fullname)

# casting a variable
decade=str(1980)
print(type(decade))
print(decade)

statement="I like rock music from the " + decade + "'s"
print (statement)

#multi lines

multiline = '''
how are you?                            

checking in.                
                        all good?

'''

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","OK"))

print(len(multiline))
multiline+="                                 "
multiline="                "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print ("")

#build a menu
title="menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheese Cake".ljust(16,".") + "$4".rjust(4))
print("Milk".ljust(16,".") + "$1".rjust(4))

print('')

#string index values

print(first[0])
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some methods return boolean
print(first.startswith("K"))
print(first.endswith("z"))

#boolean data type
myvalue=True
x=bool(False)

print(type(x))
print(isinstance(myvalue, bool))

#numeric data types

price=100
bestprice=int(80)
print(type(price))
print(isinstance(bestprice, int))


#float type
gpa=3.85
y=float(3.88)
print(type(gpa))

#complext type
complex_value=5+3j
print(type(complex_value))
print(complex_value.real)
print(complex_value.imag)

#built in functions for numbers
print('')

print(abs(gpa))
print(abs(gpa*-1))

print(round(gpa))
print(round(gpa,1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#cast a string to a number

zipcode="32092"
zip_value = int(zipcode)
print(type(zip_value))

print()
# why would i use contructor versus asssignment functions in pytyon
# Great question — and one that gets to the heart of how Python classes work! Let’s break it down:

# 🏗️ Constructor (__init__) vs Assignment After Instantiation
# Feature	Constructor (__init__)	Assignment After Creation
# Purpose	Initializes object when it's created	Modifies or adds attributes after creation
# Timing	Runs automatically during object instantiation	Happens manually after the object exists
# Consistency	Ensures all instances start with expected attributes	Can lead to inconsistent or missing attributes
# Vaidation	Can include checks, defaults, or setup logic	Typically lacks validation unless manually added
# Readability	Clear and predictable initialization	May confuse readers if attributes appear later
# 🧠 Why Use a Constructor?
# Encapsulation: Keeps initialization logic inside the class.

# Predictability: Every object starts with the same structure.

# Validation: You can check inputs and raise errors if needed.

# Cleaner Code: Avoids scattered assignments throughout your program.

# python
# class Item:
#     def __init__(self, name):
#         self.name = name

# item = Item("Phone")  # Clean and predictable
# ⚠️ Why Assignment Alone Can Be Risky
# python
# class Item:
#     pass

# item = Item()
# item.name = "Phone"  # Works, but lacks structure
# This works because Python allows dynamic attribute assignment.

# But it’s less safe — someone might forget to assign name, or assign it incorrectly.

# It also makes your class harder to understand and maintain.

# 🧪 When Might You Use Assignment?
# For optional or dynamic attributes that aren’t part of the core object.

# In prototyping or quick scripts where structure isn’t critical.

# When using dataclasses or frameworks that handle initialization differently.

# Want to see how constructors can be customized with default values, type hints, or even multiple behaviors? I can show you some cool examples!