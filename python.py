#!bin/python3
print("Hello, World!")

#Indentation (any number of spaces)
if 5 > 2:
   print(Five is greater than two!") #any number of spaces
 
 #!Assignment of variables
x = 5
y = 2
z = "Five is greater than two..."
a = "...but you already knew that!"
if x > y:
 print(z)
 print(a)

#Multi-lined comments
"""
This is a comment 
written in more than just 
one line
"""
print("Hello, world!")

#Python variables>>>...
https://www.w3schools.com/python/python_variables.asp

#For Help learning touchtyping:
https://www.typingclub.com/sportal/program-3/188.play

#Specify variable types
x = int(3) #same as 3
y = str(3) #same as '3'
z = float(3) #same as 3.0
print(x)
print(y)
print(z)

#Get variable type
x = 5
y = "John"
print(type(x))
print(type(y))

#Single and double quotes are the same.
x = "Klondike"
print(x)
x = 'Klondike'
print(x)

#Variables are case sensitive
a = 4
A = "Sally"
print(A)
#Therefore 'a' will not overwrite 'A'

#Assigning multiple variables in one line
x,y,z, q = "Orange", "Banana", "Cherry",5
print(x)
print(y)
print(z)
print(q)

#Assigning one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
#is equivalent to 
#x,y,z = fruits = ["apple", "banana", "cherry"]
#is equivalent to
#x,y,z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)

#Python numbers
"""
To select a random number
within range 3 to 15
"""
import random
print(random.randrange(3,15))

#looping through a string
for x in "pneumonoultuamicroscopicsilicovolcanoconiosis":
 print(x)
 
#creating a multiline string variable
a = """Lorem ipsum dolor
sit amet blah blah 
blah blah yada yada 
etc"""

#IN and NOT IN statements
x="there was a bee in the window"
if "bee" in x:
 print("There is bee in the statement")
if "bee" not in x
print("Didn't see it")
#OR one could...
else:
 print("Didn't see it")
 
#Slicing
a="Hello, Planet Earth!"
print(a[3:11])
#gives 'lo, Plan'
print(a[-6:])
#gives 'Earth!'

#Modifying Strings
x="Make this fully upper case"
print(x.upper())

#Modifying Strings
x="Make this fully lower case"
print(x.lower())

x=" Remove the white spaces, please! "
print(x.strip())

#Modifying Strings: Replace a string
x="Hello, World!"
print(x.replace("Hello","Heaven"))

#Modifying Strings: Convert to list with "," as separator
x="Hello, world!"
print(x.split(","))


#Python string concatenation:
https://www.w3schools.com/python/python_strings_concatenate.asp

a = "Hello"
b = "World!"
c = a + " " + b
print(c)
#='Hello World!'

#Python Format Strings
item_price = 325
item_number = 11
item_units = 3
order = "You have ordered {2} units of item {1} (${0} each)."
print(order.format(item_price, item_number, item_units))

#Escape Character: '\'
print("We are your \"Managers\" for today")

"""Python String methods"""
https://www.w3schools.com/python/python_strings_methods.asp


#Count the no. of times a character appeared in a string
string="I love to eat apples. Apples are my favourite fruit and apples are healthy"
print(string.count("apples"))#Returns 2


#Format String {this gives 'This item is $50.00 only for today!'}
discount="This item is ${cost:.2f} only for today!"
print(discount.format(cost=50))

#Join all the items in a list, tuple, etc. into one string
list_variable=("John", "Finance Executive", "2 years")
separator="SPACE"
separator.join(list_variable)
print(z)

#Trim (or strip) Left and Right
txt="...........Trim this statement left,.,.,.,,,,,"
x=txt.lstrip(".")
print(x)
#returns: 'Trim this statement left,.,.,.,,,,,'
y=x.rstrip(".,")
print(y)
#returns: 'Trim this statement left'
'''Another Example'''
txt="......Clean up the stuff at the ends..//,,.,////.,,..,"

a=txt.rstrip(".,")
b=a.rstrip("/")
c=b.rstrip(".,/")
d=c.lstrip(".")
#OR
x=txt.strip

print(a)#gives '......Clean up the stuff at the ends..//,,.,////'
print(b)#gives '......Clean up the stuff at the ends..//,,.,'
print(c)#gives '......Clean up the stuff at the ends'
print(d)#gives 'Clean up the stuff at the ends'

#String Make Translation: maketrans() Method
statement="Good night Sam!"
replacement=statement.maketrans("aSm","oJe","odnght")#This removes 'odnght' from the statement and then replaces the characters 'aSm' with 'oJe' (Whatever characters are left after removal)
trasl=statement.translate(replacement)
print(trasl)#this gives 'G i Joe!'

#Partition: Splits/separates a string into a list of 3 items
partition_x="I enjoy playing badmington. badmington is fun and good for you!"
print(partition_x.partition("badmington"))
#gives '('I enjoy playing ', 'badmington', '. badmington is fun and good for you!')'

#String replace() Method
text="one one was a good dog. three three was one, too"
print(text.replace("one", "two", 2))
#gives 'two two was a good dog. three three was one, too'

#rfind() and rindex() Methods return the last occurence of specified value within 
txt="A search within this statement will show the function of the search method"
print(txt.rfind("search", 0, 10))#gives '2'
print(txt.rindex("search"))#gives '61'
print(txt.rfind("shear"))#gives '-1'
print(txt.rindex("shear"))#gives an error

"""Python Booleans"""
a = 356
b = 27

if a<b:
logic="{1} is greater than {0}"
print(logic.format(b,a))
else:
logic="{1} is NOT greater than {0}"
print(logic.format(a,b))

a="Hello"
b=15

print(bool(a))#OR print(bool("Hello"))
print(bool(b))#OR print(bool(15))
#give 'True' for both statements

#Empty values (and few other values) give 'False'
print(bool(" "))#True
print(bool(0.0001))#True
print(bool(["🐜", "🐝", "centipede"]))#True
print(bool(0))#False
print(bool(""))#False
print(bool(False))#False
print(bool(None))#False
print(bool(()))#False
print(bool([]))#False
print(bool({}))#False

#Also False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Python Booleans
https://www.w3schools.com/python/python_booleans.asp

#Booleans: execute code based on the output of a function
def afunction():
return False

x=afunction()

if x:
print("Sure,\nwhatever")
else:
print("Nope,\nnoth\'n\' doin\'")

#isinstance() returns a Boolean for whether an object is a specified data type.
a="This is a string."
r=isinstance(a, str)

print(r)


'''Python Operators'''
#Arithmetic operators
x = 28
y = 10
print(x*y)#returns 280
print(x % y)#returns 8

#Identity Operators
a=["red", "blue", "green"]
b=["red", "blue", "green"]
c = a
x, y, z = a

#all conditions return True because:
print(c is a)#'c' is same object as 'a' (and is therefore also equal to 'a'--ie, has the same content)
print([x, y, z] is not a)#they are equal to, but not the same object as 'a'
print(b is not a)#b & a have the same content (are equal) but are NOT the same object
print(c == a)
print([x, y, z] == a)
print(b == a)
print(type(a), type(x))#'a' is list, 'x' is str

#Membership Operators
a=["red", "blue", "green"]
b=["red", "blue", "green"]
c = a
x, y, z = a

print(x in a)#returns True
print("blue" in c)#returns True
print("yellow" in c)#returns False
print(c in a)#returns #False

'''Python Lists'''

alist = ["water", "oil", "wine"]
blist = ["black", 2, False,"red", 7, True, 2]#A list can contain multiple data types.
cnstrct_list = list(("red", "blue", "green", 3))#Use the 'list() constructor to create a list
print(alist)
print(blist)
print(cnstrct_list)
print(type(alist))#'list'
print(len(alist))#'3'

for m in blist:
 print(m)
#returns:
'''black
2
False
red
7
True
2'''

#Access Lists Items
trdlist=["orange", "banana", "green", "cherry", "purple"]
one=trdlist[0]
new=trdlist[:4]
fruit=trdlist[2:4]
color=trdlist[-4:-1]
print(one, new, fruit, color)

if "banana" in trdlist:
print("I saw it!")

#Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#returns list with 'blackcurrant' in place of 'banana'

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#replaces "banana" with 2 items;  "blackcurrant", "watermelon"

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#replaces 2 items with

'''The insert() method adds items to a list at a specified index/position:'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items
#Insert
nodaList = ["a", "b", "c", "d", "e"]
nodaList.insert(0, "ants")
print(nodaList)
#returns ['ants', 'a', 'b', 'c', 'd', 'e']

#Append
nodaList.append("fish")
print(nodaList)
#returns ['ants', 'a', 'b', 'c', 'd', 'e', 'fish']

#Extend
addThis = {"g": "gun", "h": "hat"}
print(addThis)
nodaList.extend(addThis)
print(nodaList)
#returns ['ants', 'a', 'b', 'c', 'd', 'e', 'fish', 'g', 'h']


#Remove List Items
nodaList.remove("ants")
print(nodaList)

nodaList.pop(2)
print(nodaList)
nodaList.pop()
print(nodaList)
#the 'del' keyword also achieves the same as 'pop()'
del nodaList[0]
print(nodaList)

nodaList.clear()
print(nodaList)

del nodaList
#print(nodaList)
#returns an error bcos list no longer exists.

'''Looping through lists'''
listname = ["ant", "wasp", "bee", "termite"]

#Using for loops
for x in listname:
 print(x)
 
#for loop, len() and range()
for var in range(len(listname)):
 print(listname[var])
 
#Using while loop
var2 = 0
while var2 < len(listname):
 print(listname[var2])
 var2 = var2 + 1 #OR var2 += 1

#Using list comprehension (its the shortest syntax)
[print(z) for z in listname]

'''List Comprehension'''
color = ["red", "yellow", "blue", "white", "black"]

#Instead of using
asection = []
for g in color:
 if g.startswith("b"):
  asection.append(g)
print(asection)

#List Comprehension is used, which shortens the syntax
section = [g for g in color if g.startswith("b")]
print(section)

#The condition (from 'if') is optional and filters the values
bsection = [g for g in color]
print(bsection)

#The Expression can be altered b4 being added to the new list
csection = [x.upper() for x in color if x.startswith("b")]
print(csection)

#Expression can contain condition, NOT as filter, but to alter output
dsection = [h if h is not "black" else "limit" for h in color]
print(dsection)


uptoten = [g for g in range(10)]
print(uptoten)

uptofive = [g for g in range(10) if g < 6]
print(uptofive)

'''Sort Lists'''
alist=["red", "black", "Yellow", "Purple", "Blue"]

#reverse() the current order of the list
alist.reverse()
print(alist)

#sort(); by default alphabetical or numerical, in ascending order; and uppercase b4 lowercase. Use 'key' and 'reverse' to alter.
alist.sort(key = str.upper, reverse=True)
print(alist)

#Numerical example
blist=[6, 12.5, 17, 51, 69]

#Use the 'key' keyword and a customized function to sort by nearness to 50.
def blistfunc(item):
 return abs(item - 50)

blist.sort(key = blistfunc)
print(blist)

'''Copy Lists'''

list1 = ["alpha", "beta", "gamma", "omega"]

#copy()method
list2 = list1.copy()

#list() method
list2 = list(list1)

print(list1)
print(list2)

'''Join (or concatenate) Lists'''

list1 = ["alpha", "beta", "gamma", "omega"]
list2 = ["a", "b", "c", "y", "z"]

#Use operator +
list3 = list1+list2
print(list3)

#append() each item from one list to the other
for x in list1:
list2.append(x)
print(list2)

#OR use the extend() method
list1.extend(list2)
print(list1)

'''Python Tuples'''

mytuple = (True, False, "a", "b", "c", True, False)

print(mytuple)
print(len(mytuple))

tuple1 = tuple((1, True, 2, "Volvo", 7, False, 19))
print(type(tuple1))

#A tuple with only 1 item must have a comma (or use the 'tuple()' constructor), otherwise it's a string
tuple2 = ("item 1",)
print(type(tuple2))


'''Access Tuples'''

tuple1 = tuple((1, True, 2, "Volvo", 7, False, 19))

tuple2 = tuple1[1:-1]
print(tuple2)#from 'True' to 'False'

print(tuple1[-1])#returns 19. But when using a range [int x:int y], the item at index y is not included in result.

print(tuple1[:4])#returns items to, but not including '7' (which is at index 4)

print(tuple1[-5:])#from 2 to the end

if True in tuple1:
print("True, it's in tuple1.")

'''Update Tuples'''

#This is generally done by changing the type to a list, updating it and then converting it back to tuple.

#Change values
tuple1=("ant","bee", "caterpillar",)
list1=list(tuple1)
list1[1:3]=["bear", "cat","dog"]
tuple1=tuple(list1)

print(tuple1)

#Add values
list1=list(tuple1)
list1.insert(4, "elephant (added)")
tuple1=tuple(list1)

print(tuple1)

#Remove items
list1=list(tuple1)
list1.remove("bear")
tuple1=tuple(list1)

print(tuple1)

#Delete a tuple
del tuple1
print(tuple1) #this gives an error as the  tuple no longer exists

'''Unpack Tuples'''

tuple1 = ("ant", "butterfly", "centipede")

(six, two, hundred) = tuple1

print(six)
print(two)
print(hundred)

#If tuple variables are not equal to values, using asterisk on ONE value will assign excess variables to it as a list (or an empty list when variables are fewer by 1).
tuple2 = (1, 2, 3, 4, 5)

(w, x, *y, z) = tuple2

print(w)
print(x)
print(y)
print(z)

#Looping through Tuples

fruits = ("apple", "banana", "cherry")

#for loop
for item in fruits:
print(item)

#for loop with range() and len() functions
for index_num in range(len(fruits)):
print(fruits[index_num])

#while loop
current = 0

while current<len(fruits):
print(fruits[current])
current = current + 1

#Join Tuples

#Use the + operator
fruits = ("apple", "banana", "cherry")
colors = ("yellow", "green", "red")
salad = fruits + colors

print(salad)

#Multiply Tuples

#Use * the number of times you want to multiply it
triple = fruits * 3
print(triple)

#Built-in methods
#count()
print(triple.count("apple"))#returns 3
#index()
print(triple.index("cherry"))#returns 2

'''Python Sets'''

#unordered and unindexed
firstset = {"volvo", "volkswagen", "mazda", "toyota"}
print(firstset)

set1 = {"apple", 1, "banana",True, "cherry", 13, "apple"}
print(len(set1))
print(type(set1))

#can contain any characters
set2 = set((21, False, "Fifteen", 12, True))
print(type(set2))

#cannot use index numbers (ahem! unindexed...) to access items
#use for to loop
for x in set2:
print(x)

#use in to determine the presence of a character
a = True in set1
print(a)

if "Fifteen" in set2:
print("Fifteen is in set 1")

#Add Set Items
aset = {"ant", "bee", "centipede", "dragonfly"}

#add single items: add()
aset.add("earwig")
print(aset)

#add other  iterables: update()
bset = {"flea", "grasshopper"}

aset.update(bset)
print(aset)

ctuple = ("housefly", "inchworm")

aset.update(ctuple)
print(aset)


'''Join Sets using any of the following methods'''

fruits = {"apple", "blackberry", "banana", "mango", "cherry"}

companies = {"apple", "blackberry", "microsoft", "google", "verizon"}

#update() methods return a combination of two sets [x.update(y)] as the first set (x)
fruits.update(companies)
print(fruits)

#The union() method returns a new set:
fruits = {"apple", "blackberry", "banana", "mango", "cherry"}

x = fruits.union(companies)
print(x)

#intersection_update() returns ONLY values in both sets
fruits.intersection_update(companies)
print(fruits)

#intersection() method returns a new set of ONLY values in both sets
fruits = {"apple", "blackberry", "banana", "mango", "cherry"}

x = fruits.intersection(companies)
print(x)

#symmetric_difference_update() method returns all EXCEPT/EXCLUDING values in both sets
fruits.symmetric_difference_update(companies)

print(fruits)

#symmetric_difference() method returns a new set EXCLUDING values found in both sets.
fruits = {"apple", "blackberry", "banana", "mango", "cherry"}

x = fruits.symmetric_difference(companies)
print(x)


'''(Other) Set Methods'''

fruits = {"apple", "blackberry", "banana", "mango", "cherry"}

companies = {"apple", "blackberry", "microsoft", "google", "verizon"}

num = {1, 6, 4, 9, 13}

num2 = {1, 4, 9}

#isdisjoint(): returns True if 2 sets have no intersection.

print(companies.isdisjoint(fruits))#False

print(companies.isdisjoint(num))#True

#issubset(): False if 1 or more elements in x are NOT in y
print(fruits.issubset(companies))#False

#issuperset(): returns True if All elements in y ARE IN x

x = num.issuperset(num2)
print(x)#True



'''Python Dictionaries'''
firstdict = {
"name": "John",
"age": 32,
"job": "Scientist",
"job": "Librarian",
"age": 54
}
#Dictionaries do not allow duplicates, are ordered and changeable.

print(firstdict)#returns '{'name': 'John', 'age': 54, 'job''
print(type(firstdict))#returns '<class 'dict'>'
print(len(firstdict))#returns '3'

'''Access Dictionaries'''
print(firstdict["job"])#returns the value of the key: 'Librarian'
candidateAge = firstdict.get("age")#this also returns the value tied to this key:
print(candidateAge)#'54'

print(firstdict.keys())#returns a list of all the keys in the dictionary
print(firstdict.values())#returns a list of all the values in the dictionary
print(firstdict.items())#returns each item (key:value) as a list of tuples

#The output of keys(), values() and items() methods are *views* of the existing mapping:
firstdict["education"] = "College"

print(firstdict.keys())
print(firstdict.values())
print(firstdict.items())
#Therefore changes in the original dictionary are reflected


#Check if key is in dictionary.

timedict = {
"year": 2021, "month": "May", "day": "Friday",
}
time = "{}:{}pm"

if "year" in timedict:
print("Key exists in \"time\" dictionary")
else:
print("Requested Key is absent")

#Change an items by referring to its index key
timedict["month"] = "June"
print(timedict)

#Add a new item using a new index key and assigning a value to it.
x = "{}th"
timedict["date"] = x.format(30)

#use the update() method+another dictionary (argument) to change multiple items or add new item(s)
timedict.update({"year": 2043, "time": time.format(11, 27)})
print(timedict.items())

#Remove Dictionary Items

dict1 = {"name": "Ben", "job": "Surgeon", "gender": "Male", "age": 69, "status": "Retired"}

#pop() method to remove an item by referring to key its index.
dict1.pop("gender")
print(dict1)

#popitem() to remove the last item
dict1.popitem()
print(dict1)

#del keyword to remove item by referring to its key index
del dict1["job"]
print(dict1)

#clear() method empties a dictionary.
dict1.clear()
print(dict1)

#del dict1
print(dict1)#raises an error

#Loop Through Dictionary

dict1 = {"name": "Ben", "job": "Surgeon", "gender": "Male", "age": 69, "status": "Retired"}

#Use a 'for' loop to print return dictionary KEYS 1 by 1
for keyname in dict1:
print(keyname)

#here the key (is used as) index to return values.
for keyname in dict1:
print(dict1[keyname])

#also use keys() method to loop through keys
for key in dict1.keys():
print(key)

#and values()method  to loop through values
for value in dict1.values():
print(value)

#items() method returns Dictionary items
for item in dict1.items():
print(item)

#Copy Dictionaries
dict1 = {"a": 1, "b": 2, "c": 7, "d": "37"}
#copy() method
dict2 = dict1.copy()
print(dict2)

#dict() method
dict3 = dict(dict1)
print(dict3)

'''Nested Dictionaries'''
#method 1: A dictionary containing multiple dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#method 2: create multiple dictionaries and add them to a dictionary as values
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

#Dictionaries: other methods

#get() method prints the value of a specified key,
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("brand"))

#or prints specified value if key does not exist.
x = car.get("speed", "359Kmph")#returns '359Kmph'
print(x)

#fromkeys() method creates a dictionary from a list of keys
keys = ["a","b","c"]
values = "nice"
dict1 = dict.fromkeys(keys, values)

print(dict1)

#setdefault() returns a key's value if the key exists, or inserts (None or) a specified value if it doesn't

print(car.setdefault("brand", "Toyota"))#returns Ford

print(car.setdefault("transmission", "Manual"))#returns AND inserts 'manual' into dictionary.
print(car)


'''Python Conditions (IF statements)'''

a = 33
b = 200
c = 314
d = 33

#IF
if b > a:
  print("b is greater than a")

#ELSE
if a > b:
print("33 is greater than 200")
else:
print("33 is NOT greater than 200")

#ELIF (Else If)
if a > b:
print("33 is greater than 200")
elif a < b:
print("33 is less than 200")

#ELSE catches anything that isn't caught by preceeding conditions
if a > d:
print("33 is greater than 33")
elif a < d:
print("33 is less than 33")
else:
print("33 is equal to 33")

'''Ternary Operators or Conditional Expressions'''
#shorthand IF
if a == d: print("Thirty-three is equal to Thirty-three")

#shorthand IF... ELSE
print("Thirty-three is greater than 200") if a > b else print("Thirty-three is NOT greater than 200")

#shorthand ELSE... IF (multiple ELSE statements on one line)
print("200 is less than 33") if b < a else print("200 is equal to 33") if b == a else print("200 must be greater than 33...🤔")


a = 33
b = 200
c = 314
d = 33

#and
if a < b and a == d: print ("33 is less than 200", "AND 33 is equal to 33")

#or
if b > c or a == d:
print("200 is greater than 314🤨"" OR 33 is equal to 33")

#Nested IF
print("Thirty-three is... ")
if a > 10:
print("greater than 10,")
if a > 20:
  print("greater than 20,")
  if a > 30:
   print("and also greater than 30...")
   if a < 35:
     print("but less than 35")

#pass statement
if a < b:
pass #this IF statement gets ignored


'''Python While Loops'''
i = 15
j = 17
breaktime = 0

#while
while i > 0:
print(i)
i -= 3

print("\n")

#'break' statement
while j > breaktime:
print(j)
j -= 1
if j < 7:
  break

#'continue'
j = 12

while j > 0:
j -= 2
if j == 6:
  continue
print(j)#'6' is skipped while other even numbers are printed

#'else' statement
var = 0

while var < 9:
var += 1
print(var)
else:
  print("9 says: \"Operation is completed 😎\"")
  
'''Python For Loops'''

#for loops are used for iterating over a sequence (lists, strings, etc)
list1 = ["wix", "wordpress", "joomla", "squarespace"]

for item in list1:
print(item)

for alphbt in "generalization":
print(alphbt)

#break statement: exit loop when specified condition is met
for char in "psychological":
print(char)
if char == "g":
  break

#Exit at "g", but the 'break' comes b4 print this time
for element in "etymologically":
if element == "g":
  break
print(element)#therefore 'g' doesn't get printed

#the continue statement: stop current iteration and continue with next
for z in list1:
if z == "joomla":
  continue
print(z)


#range() function:
for number in range(7):
print(number)

#specify range() starting point:
for x in range(3, 9):
  print(x)

#specify range() starting point AND increments:
for i in range(6, 28, 3):
print(i)

#else statement: executes when loop is finished
for x in "#throwbackThursday!":
print(x)
else:
print("It's Friday today🤗")
#else will not execute if loop is stopped with 'break'


#Nested for loops
animal = ["sheep", "goat(s)", "cow(s)"]

for x in range(1, 6):
    for y in animal:
     print(x, y)

#pass statement:
for item in animal:
for x in range(22):
     pass
   #this 'for' loop is ignored

'''Python Functions'''
#functions are defined using the'def' keyword:
def new_function():
    print("This is a newly created function!")
#and are called using the 'function_name' followed by '()'
new_function()

#'firstname' is a parameter of the function while the actual "Firstname" is an argument.
def nameFunction(firstname):
    print(firstname + " Akande")

print("These are the names of my parents' children by order of birth:")

nameFunction("Similoluwa")
nameFunction("Toluwanimi")
nameFunction("Gboluwaga")
nameFunction("Oluwapelumi")

#Arbitrary Arguments (*args)

#*args are used when one does not know how many arguments will be passed to a function parameter. Then the argument(s) are treated as a tuple, and an [index no.] is used to access the desired argument

def arbitraryArgument(fname, lname, x, y, *age):
   
     print(fname +" "+ lname + ", " + x.format(age[y]))

print("The children were...")

arbitraryArgument("Mathias", "Garret", "in Grade {}", 1, 12, 7, 9)
arbitraryArgument("David", "Refsnes", "{} years old", 0, 12, 15, 19)
print("and")
arbitraryArgument("Miles", "Moore", "who joined the elites program {} months ago", 2, 23, 9, 6)

#Keyword Arguments
#using 'key = value' syntax to specify the argument value of each parameter, so the order of parameter doesn't matter anymore:
def keywordArgument(name, course, grade, date):
    print(name + ", " + course + ": " + grade + ", " + date)

keywordArgument(course = "Typing", name = "David Refsnes", grade = "Excellent", date = "27th June")

#Arbitrary Keyword Arguments
#Use '**' and the function is give a Dictionary of items (which require key=value syntax) and use keys as index positions to select an argument

def arbitraryKeyArg(name, **isfrom):
    print("Student is "+name+", from "+ isfrom["country2"])

arbitraryKeyArg(name="Logan", country1="Nigeria", country2="S.Korea", country3="Pakistan")

#Default parameter value:
#create a default value for parameters, and if no argument is given when the function is called, default will be used.
def defaultValue(country, state="Ondo", lga="Akure South"):
    print("I am a resident of "+lga+", "+state+", located in "+country+"!")

defaultValue("Nigeria")
defaultValue("Australia", "Sydney", "New South Wales")

#Pass A List, Tuple, etc as an argument
def loopFunction(color):
    for x in color:
        print(x)

loopFunction(color=("orange", "red", "black"))
loopFunction("Overenthusiastic")
   

#Return Values in a function
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))

#'pass' Statement:
def function():
    pass

'''Recursion'''
#Recursion involves a function calling itself, looping through data to arrive at a result:
def recursionFunction(x):
    if x > 0:
        a = x + recursionFunction(x - 1)
        print(a)
    else:
        a = 0
    return a

print(recursionFunction(5))


'''Lambda Function'''
#A Lambda functions is a small anonymous functions. It can have any number of arguments but only 1 expression.


x = lambda arg: arg * 10
print(x(5))

z = lambda y: print(y * 3)
z(3.333)

'''Used in a function:'''
def aFunction(multiplier):
    return lambda val: val * multiplier

call = aFunction(7)
answer = call(3)
print(answer)

#note that return is (probably) used to assign a value to a function
def test(y):
    return 5 / y
print(test(2))
#this will return 'None' bcos there is no 'return' (or 'print') in the function:
def test(y):
    5 / y
print(test(2))


'''Python Classes & Objects'''
#To create a class:
class FirstClass:
    property = 5

#To create an object from the class:
object = FirstClass()
print(object.property)


class CarClass:
    def __init__(brand, model, color, tint):
        brand.model = model
        brand.color = color
        brand.tint = tint

x = CarClass("Mustang", "Grey", "Black")
print(x.tint)
print(x.model)

#Method Objects: these are functions that belong to the method:
class CarClass:
    def __init__(model, brand, color, name):
        model.brand=brand
        model.color=color
        model.name=name
   
    def method(model):
        return "My car is a "+model.color+" "+model.brand+" "+model.name

obj = CarClass("Ford", "Grey", "Mustang")

#*note that the first parameter of functions inside the class ('model' in example) is always used as a reference to access variables that belong to the class. It doesn't have to be the same for different functions inside a class.

print(obj.method())

#Classes 'self' parameter:
#used in any functions in a Class to refer to variables in a Class. Can be called anything

class Class:
    def __init__(self, name, color):
        self.name = name
        self.color = color
   
    def describe(self_prefix):
        return "You have purchased a "+self_prefix.color+" "+self_prefix.name+"!"

obj = Class("Mango", "Yellow")
print(obj.describe())

#Change object properties
print(obj.name)

obj.name = "Apple"
print(obj.name)

#Delete object properties
del obj.name
print(obj.name)#gives an error

#Delete an object
del obj
print(obj.color)#gives

#the Pass statement
#a Class cannot be empty. the pass statement can be used if a class is being left empty
class unusedClass:
    pass

'''Inheritance'''
#a 'child' or 'derived' class inherits properties from a 'parent' or 'base' class
#any class can be a parent class:

class Person:
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
   
    def returnName(access):
        return "The person is called "+access.fname+" "+access.lname

stuff = Person("David", "Finley")
print(stuff.fname)
print(stuff.lname)
print(stuff.returnName())
#To create a Child class out another class, use the 'class' keyword
class Student0(Person):
    pass #include 'pass' if u don't want to add more properties or methods to avoid errors

#Use properties of the Child class:
childStuff = Student0("Maximus", "Gerald")
print(childStuff.fname+", "+childStuff.lname)
print(childStuff.returnName())

#When the '__init__()' function is added to a Child class, it overides that of the parent class. The class will no longer inherit its parent's '__init__' function
class Student(Person):
    def __init__(self, firstname, lastname):
        '''self.fname = firstname
        self.lname = lastname'''
#To add the 'init' function to a Child class and still inherit the parent's 'init' function:
        '''Person.__init__(self, firstname, lastname)'''
#or use the 'super()' function:
        super().__init__(firstname, lastname)

objectStuff = Student("Ant", "Falcon")
print(objectStuff.returnName())


#To add new properties to a child class:
#1. create it (fixed value) or
#2. add it to list of 'init' function parameters (variable):
class Student(Person):
    def __init__(self, firstname, lastname, year):
        self.entranceYear = 2021 #1
        super().__init__(firstname, lastname)
        self.graduationYear = year #2
   
    def welcomeStudent(ref):
        return "This University welcomes "+ref.fname+" "+ref.lname+" to the Masters set of {}!".format(ref.graduationYear)
       
       
objectStuff = Student("Ant", "Falcon", 2019)
print(objectStuff.entranceYear)
print(objectStuff.welcomeStudent())



'''Python Iterators'''
#iterable objects include list, tuples, sets, dictionaries and strings

newlist = ["watermelon", "banana", "pineapple", "mango"]

myiterat = iter(newlist)

print(next(myiterat))
print(next(myiterat))
print(next(myiterat))
print(next(myiterat))
#print(next(iterat))#gives 'Stop iteration' error
print(next(iter(newlist)))

#iterator from string:
newiter = iter("iterate")
j = 0
while j < len("iterate"):
    print(next(newiter),"\n")
    j += 1

#Looping through an operator is done using the for loop:

for laugh in "laughter":
    print(laugh)

atuple = (1, 6, 4, 6, 9)
for x in atuple:
    print("",x)


'''Create an Iterator'''

class of20:
    def __iter__(self):
        self.less = 2
        return self
   
    def __next__(self):
        x = self.less
        self.less += 2
        return x

object1 = of20()
iter1 = iter(object1)

#print(next(iter1))

x = 0
while x < 20:
    print(next(iter1))
    x += 1

#StopIteration: used to limit the number of times that the iteration is performed:
print("\n")

class of20:
    def __iter__(bat):
        bat.man = 1
        return bat
   
    def __next__(funny):
        if funny.man <= 20:
            nxt = funny.man
            funny.man += 1
            return nxt
        else:
            raise StopIteration

myterator = of20()
nexterator = iter(myterator)

for x in nexterator:
    print(x)


'''Python Scope'''

#A variable created inside a function belongs to its 'local' scope, and can therefore only be used inside that function
def newFunction(a):
    y = 200
    print(y,"\n")
    x = 7 * a
    return x
   
print(newFunction(2))
#print(y) #Gives an error

#function inside a function:

def newFunc():
    var = 250
    #an inside function that prints 'var':
    def innerFunc():
        print(var)
    #call inside function:
    innerFunc()

newFunc()
#A variable created in the main body of Python code belongs to the 'global' scope and can be used both locally and globally:
x = 300

#A function which prints 'x'
def aFunc():
    print(x)

aFunc()
print(x)

#Using the same name for a global and local variable will result in 2 variables, one will be global, and the other (inside) variable will be local
j = 12

def newFunc():
    j = 35
    print(j)

newFunc()#gives 35
print(j)#gives 12

#the 'global' keyword:
#Used to create global variables inside a function:
def global_y():
     global y
     y = 22.77
     print(y)

global_y()
print(y)
#both give '22.77'

#Use 'global' to change a global variable (locally) inside a function:
u = 32
def change_u():
    global u
    u = 55.00

print(u)#gives 32
change_u()
print(u)#gives 55.00




'''PYTHON MODULES'''
#A module it's a code library which can be imported and used. To create one, simply enter the code into a document and save it with the .py (e.g. newmodule.py)
#To import it, use the 'import' command:
#import mymodule

import platform

x = platform.system()
print(x)

import numpy as np

#print(np.version)

print(dir(np))


'''PYTHON MODULES'''
#A module it's a code library (containing functions, arrays/lists and any other variable) which can be imported and used. To create one, simply enter the code into a document and save it with the .py (e.g. newmodule.py)
#To import it, use the 'import' command:
'''import mymodule'''

#To use a function in a module, use the syntax:
'''module_name.function_name()'''
#You can access other data types (like dictionaries) in this way:
'''module_name.dict_name["key"]'''

'''Built-in Modules'''
#These are python modules which can be imported whenever one wishes, e.g:
import platform as plaf
#Use 'as' to Rename a module

x = plaf.system()
print(x)

#Use the dir() method to print a list of all the variables in any module (Built-in or otherwise):
x = dir(plaf)
print(x)

#Use the 'from' keyword to import only parts of a module:

from numpy import AxisError, Bytes0

print(AxisError(7), Bytes0(3))
#Note that when parts are imported, they don't need to be referred to using the 'module_name' before function/variable name


'''Python Datetime'''
#There is no data type as 'date' but by importing the 'datetime' module, one can work with dates as date objects:
import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%A"))#gave 'Sunday'

#Use the 'datetime()' class constructor to create date objects
y = datetime.datetime(2021, 6, 28)
print("Tomorrow,", y)

print("Today,", datetime.datetime.now().strftime("%d-%m-%y"))


'''Python Math'''
#Python had a set of built-in math functions
a = min(5, 53, 27, 18, 3, 12)
print(a)#5
a = max(5, 53, 27, 18, 3, 12)
print(a)#53

b = abs(-3.6*5)
print(b)#18.0

c = pow(4, 3)
print(c)#64

'''Python also has a built in module called 'math' which extends the list of mathematical functions'''
print("\n")
#to use the math.methods and contents, start by importing:
import math

#Square root
x = math.sqrt(8)
print(x)

#round-up
x = math.ceil(3.274)
print(x)#4
x = math.ceil(-3.274)
print(x)#-3

#round-down
y = math.floor(10.9987)
print(y)#10
y = math.floor(-10.9987)
print(y)#-11

#pi constant
print(math.pi)
print(math.ceil(7*math.pi))#22

#Some other math functions
a = (5, 10)
b = (15, 25)

print(math.dist(a, b), math.sqrt(90))
print(math.gcd(27,44))#greatest common divisor


'''Python JSON'''
import json

#use json.loads() to parse JSON (convert to Python).

#json string:
x = '{"title":"Mr", "name":"John", "age":32}' #Result is Python dictionary

y = json.loads(x)
print(y["age"])

print(json.loads(x)["name"])

#use json.dumps() to convert Python to JSON

pydict = {
    "title":"Master",
    "name":"Magnus",
    "age":22
}

jsondict = json.dumps(pydict)
print(jsondict)

#Python strings, iterables and number object types can be converted to JSON text:

print(json.dumps("Three Blind Mice"))
print(json.dumps(["Thirty-three", 47, True, "False", None]))
print(json.dumps(("Stairs", "Balcony", "Column", "Roof")))
print(json.dumps({"Red": 12, "Green": 25, "Blue": 0}))
print(json.dumps(23))
print(json.dumps(-1.206573))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Formatting the JSON results for readability:
alldict = {
    "name": "Stephen",
    "title": "Apostle",
    "family": {
        "children":{None: "Unrecorded"},
        "wife":{None: "Unrecorded"}},
        "acts":["Preaching", "Matyrdom"], "associated": (
        {"Saul":"custodian at execution", "info":"later called by Christ to apostleship"},
        {"apostles": "Selected him to help in managing affairs of the church", "info": "Also selected: Philip, Procorus, Nicanor, Timon, Parmenas, and Nicolas"}
        ), "scared": False, "disciple": True, "charsInName": 7
}

#Use indent to specify number of indents, separators to change default separators (, and :) and use sort_keys to select whether or not keys should be sorted

print(json.dumps(alldict, indent=5, separators=(", "," = "), sort_keys=True))


'''Python RegEx 're' (Regular Expressions)'''
#The re module is used to check if text contains regular expressions

import re

#The RegEx functions include:
#search
text = "Remain calm like it's play time"

a = re.search("^Remain..*time$", "Remain calm like it's play time")
print(a)

#findall
c = "Maintain like trains crossing mountains in Spain"
b = "ain"
a = re.findall(b+"+", c)

print(a)
if a:
    print ("The \"" + b + "\" characters exist.")
else:
    print ("Characters \"" + b + "\" were not found.")

#split
print(re.split(b, c,  4))#maxsplit = 4

#sub
print(re.sub(b, "***", c, 3))#i.e. replace 'b' with "***" in 'c' for '3' occurences.

#Match Object: 
#Object containing information about the search and its result. If no match is found, 'None' is returned instead.
print(re.search("impostor", "...but there were impostors among them."))#This returns a Match object

#Match object methods can be used to return information about the match
x = "Book titled Great Expectations."

#span
print(re.search(r"\bG\w+\s", x).span())
#the above returns '(12, 18)' which is a tuple of start and end positions of the search.
#NOTE: \b-beginning of word, \w-word characters (a-z, 0-9, _), (\w+=one or more word characters) \s-whitespace.

#string
y = re.search(r"\bG\w+\s", x)
print(y.string)
#returns the string (x) passed to the function

#group
y = re.search(r"\s\bt\w+", x)
print(y.group())
#returns the part of the string (' titled') that matched the search




'''Python Try Except'''
#the 'try' block helps determine if an error exists a block of code
#the 'except' block handles an error
#the 'finally' block executes code regardless of the result of the try... except

try:
    print(x)
except:
    print("An error exists in the code...\n")

print("..the program continues, however...")

#If the try... except is not used, the program stops when an error occurs
#print(x)
print("...but this line is not printed because of the error in the line above\n")

#There can be any number of 'except' lines for different errors
try:
    print(x)
except NameError:
    print("The variable named 'x' is not defined\n")
except:
    print("Some unidentified error occurred")

#'else' is used to execute code when no exception is raised
try:
    print("An attempt at program execution...")
except:
    print("An error occurred")
else:
    print("...No errors were identified.\n")

#The 'finally' block, if specified, executes whether or not an error/exception is raised

try:
    print(x)
except:
    print("Well, that didn't work")
finally:
    print("The try... except has concluded.")
#'finally' is useful for cleaning up and for closing objects
#for example:

try:
    file = open("Person_Salaries.csv")
    file.write("Uhhhhhg, Fine!")
except:
    print("Unable to write to file")
'''finally:
    file.close()'''
    #should close the file object, allowing the program to continue without leaving it open


'''Raising an Exception'''
#Use the 'raise' keyword to raise an exception if a condition is met
number = -0.0002

'''if number <= 0:
    raise Exception("Only numbers greater than 0")'''
    #this prints the exception and stops the program

#Specify the type of error/exception (such as NameError or TypeError)
age = "twenty-six"
print(age)
'''if type(age) is not int:
    raise TypeError("Only numbers allowed")'''



''' Python User Input'''
#Python allows for user input using the 'input()' method ('raw_input()' for Python 2.7)
#The program stops executing when it gets to input, and continues after it has received an input

nickname = input("Type in your nickname: ")
print("You will now be known as "+nickname)




'''Python String Formatting (2)'''
#The 'format()' method is used to make a string display as expected (in combining variables, user input, integers with a string)

intg = 52.5250
string = "The item costs {} after a 33% discount!"

output = string.format(intg)
print(output)

#Add parameters inside the curly bracket to determine how value will be converted
string = "Apply our discount to get ${:.2g} off your order"
print(string.format(intg))

#Formatting Multiple Values
#achieved by listing the values in the format method
year = 33
month = 3
day = 1
text = "On the {}st day of the {}rd month, in the year 20{}, the following entry was made..."

print(text.format(day, month, year),"\n")

#Indexes can be included in curly brackets to determine the order in which values appear
#and can also be used to refer to a value more than once

date = 7
pos = "22nd"
discount = 77
text = "On day {1} of July, David was the {0} customer to receive a ${2:.2f} discount for the company's {1} year anniversary"
print(text.format(pos, date, discount))

#Named Indexes: Use named indexes by entering a name in the curly brackets. Then names must be used to pass the parameter values.

history = "{king} and his son {prince} were among the greatest Kings the land ever knew."
print(history.format(king = "Caspian", prince = "Rilian"))


'''Python File Handling'''

'''File Open'''
#The main function used in working with files is 'open()'
#There are 4 modes/methods for opening files:
'''
r: open an existing file for reading
a: append to a file and create it if it doesn't exist
w: open a file for writing and create it if it doesn't exist
x: create a file. Error if it already exists

Can also specify if the file should be handled as text ('t', default) or binary ('b', such as images)
'''

#open("afile.txt")
#is the same as

#open("afile.txt", "rt")
#because 'r' (read) & t'(text) are the default and don't need to be specified




'''Read Files'''

#assuming the file 'testfile.txt' exists *On the same folder as Python* and has the following content:
'''
Good morning merry sunshine,
How did you wake so soon?

You scared the little stars away,
and shined away the moon!
'''
a = open("testfile.txt", "r")
#opens the file

#The 'read()' method
print(a.read())
#prints the content of the file

#assuming the file is in a different location,
a = open("D:\\User\folder\testfile.txt", "r")

#Read parts of the file
a = open("testfile.txt", "r")
print(a.read(5))
#print only first 5 characters

'''Read Lines'''
a = open("testfile.txt", "r")
print(a.readline())#this prints the first line of the file
print(a.readline())#prints the second line.

'''Loop through the entire file, line by line, using a for loop'''
a = open("testfile.txt", "r")
for x in a:
    print(x)

'''Close File'''
a = open("testfile.txt", "r")
print(a.read())

a.close()
#Sometimes changes may not show until a file had been closed.


'''File Write'''

#files are written to using:-

#the 'a' (append) will add to the end of the file
file = open("testfile.txt", "a")
file.write("This is what we've added to the file")
file.close()

#and 'w' (write) will overwrite any existing content.
file = open("testfile.txt", "w")
file.write("This new content has now overwritten all formerly existing content on the file.")
file.close()

#to read the new content of the file:-
file = open("testfile.txt", "r")
print(file.read())
file.close()

'''Create New File'''
#Use 'a' or 'w' to make a file if it does not exist (or write to an already existing file)
#'x' (create) is used to make a new empty file if it doesn't exist. Gives an error if the file exists.
file = open("testfile.txt", "x")



'''Python Delete Files'''

#This is achieved using the 'os.remove()' function of the 'os' module
import os

os.remove("testfile.txt")

#Use 'os.path.exists()' to check if a file exists before deleting to avoid getting an error:-
if os.path.exists("testfile.txt"):
    os.remove("testfile.txt")
else:
    print("How do we say this... the file just isn't there!")

#to delete an entire folder:-
os.rmdir("foldername")

#can only delete empty folders.





#Typing
https://www.typingclub.com/login.html -- lesson 200

