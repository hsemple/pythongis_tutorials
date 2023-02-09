
Strings and Lists
====================

|

Strings
---------

A string is a sequence of characters, e.g.,

   >>> "Hello. I am a GIS Analyst"



Strings in Python are surrounded by either single quotation marks, or double quotation marks. However, you cannot combine the two quotation styles.

  'Hello' is the same as "Hello".



Strings can be stored as variables, e.g.,: 

   >>> y = 'Hello' is the same as "Hello".



|


String Operations
------------------

Various operations can be performed on string variables. Some of these are presented below:


**a.  Concatenation**

Concatenating strings means joining strings by linking them end-to-end.


.. code-block:: python
   :linenos:
   
   print ('James' + 'Brown')
   #The output of this statement is JamesBrown.


   #Put a space after James or Brown to create the space.
   print ('James ' + 'Brown')

   #or
   print ('James' + ' ' + 'Brown')

   #or
   print ('James', 'Brown')


|


**b. Converting Non-String Objects to String**

Virtually any object in Python can be rendered as a string. The str(obj) returns the string representation of object obj:

 >>> str(50.2)
 '50.2'
 >>> str(3+4j)
 '(3+4j)'
 >>> str(3 + 29)
 '32'
 >>> str('foo')
 'foo'

|


**c. Concatenating Strings and Integers**

>>> temp = 100
>>> print ("The temperature is " + temp + " degrees")
TypeError: cannot concatenate 'str' and 'int' objects

>>> print ("The temperature is " + str(temp) + " degrees")
The temperature is 100 degrees


|



**d. Repetition** 

The * operator is used to perform perform repetition

>>> 'Semple ' * 3
 'Semple Semple Semple'

|


**e. Changing Cases**

*string.lower()*    

>>> text = "I LOVE WRITING PYTHON CODE"

>>> # convert message to lowercase
>>> print(text.lower())
i love writing python code



*string.upper()* 

text = "I love learning Javascript"

# convert message to lowercase
print(text.upper())
I LOVE LEARNING JAVASCRIPT



|


**f. Returning the Length of a String**

The len() method returns the number of characters in the variable.  With len(), you can check the length of Python strings.   

>>> s = 'I am a string.'
>>> len(s)
14


|

**g. String Indexing**

In programming, individual items in an ordered set of data can be accessed directly using a numeric index or key value. This process is referred to as indexing.

In Python, strings are ordered sequences of character data, and thus can be indexed in this way. Individual characters in a string can be accessed by specifying the string name followed by a number in square brackets [ ].

String indexing in Python is zero-based: the first character in the string has index 0, the next has index 1, and so on. The index of the last character will be the length of the string minus one.

The individual characters can be accessed by index as follows:

>>> s = 'foobar'
>>> s[0]
'f'
>>> s[1]
'o'
>>> s[3]
'b'
>>> len(s)
6
>>> s[len(s)-1]
'r'


Attempting to index beyond the end of the string results in an error:

>>> s[6]

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
  s[6]
  IndexError: string index out of range


|

String indices can also be specified with negative numbers, in which case indexing occurs from the end of the string backward: -1 refers to the last character, -2 the second-to-last character, and so on.  Here are some examples of negative indexing:

>>> s = 'foobar'
>>> s[-1]
'r'
>>> s[-2]
'a'
>>> len(s)
6
>>> s[-len(s)]
'f'

|

**h. String Slicing**

Python also allows a form of indexing syntax that extracts substrings from a string, known as string slicing. If 's' is a string, an expression of the form  s[m:n]  returns the portion of  s starting with position m, and up to but not including position n:

>>> s = 'foobar'
>>> s[2:5]
'oba'

 
Again, the second index specifies the first character that is not included in the result—the character 'r' in the example above. This may seem slightly unintuitive, but after a while you will get used to it.  The expression s[m:n] will return a substring that is n minus m characters in length, in this case, 5 minus 2 = 3. 
 

If you omit the first index, the slice starts at the beginning of the string. Thus, s[:m] and s[0:m] are equivalent:

>>> s = 'foobar'
>>> s[:4]
'foob'
>>> s[0:4]
'foob'

 

Similarly, if you omit the second index as in s[n:], the slice extends from the first index through the end of the string.

>>> s = 'foobar'
>>> s[2:]
'obar'

 

Omitting both indices returns the original string, in its entirety.

>>> s = 'foobar'
>>> t = s[:]



**i. Slicing with Negative indices**

Negative indices can be used with slicing as well. -1 refers to the last character, -2, the second-to-last, and so on, just as with simple indexing. The diagram below shows how to slice the substring 'oob' from the string 'foobar' using both positive and negative indices:
String index 3

 

Here is the corresponding Python code:

>>> s = 'foobar'

>>> s[-5:-2]
'oob'
>>> s[1:4]
'oob'
>>> s[-5:-2] == s[1:4]
True

Specifying a Stride in a String Slice
Links to an external site.

Adding an additional  : and a third index designates a stride (also called a step), which indicates how many characters to jump after retrieving each character in the slice.

For example, for the string 'foobar', the slice 0:6:2  starts with the first character and ends with the last character (the whole string), and every second character is skipped. This is shown in the following diagram:
String stride 1

 

Similarly, 1:6:2 specifies a slice starting with the second character (index 1) and ending with the last character, and again the stride value 2 causes every other character to be skipped:
String stride 2
 

>>> s = 'foobar'
>>> s[0:6:2]
'foa'

>>> s[1:6:2]
'obr'

 

As with any slicing, the first and second indices can be omitted, and default to the first and last characters respectively:

>>> s = '12345' * 5
>>> s
'1234512345123451234512345'
>>> s[::5]
'11111'
>>> s[4::5]
'55555'

 

You can specify a negative stride value as well, in which case Python steps backward through the string. In that case, the starting/first index should be greater than the ending/second index:

>>> s = 'foobar'
>>> s[5:0:-2]
'rbo'
 

|

**j. Formatting String Variables Using the % Operator**
The program below illustrates the use of string formatting using the % operator.    With this method,  the percentage sign followed by a letter and some numbers indicate how a variable should be formatted. The variable itself is stored as a tuple to the right of the string.   Here are some basic argument specifiers you should know:

%s - means format the variable as a string
%d - means format the variable as an integer
%f - means format the variable as as floating point number
%.3f means format the variable as a floating point numbers with three digits to the right of the decimal value.

See this link  (Links to an external site.)for more info on formatting strings.

 

In the code below, %0.2f and %0.4f' are formatted place holders for two variables. The variables appear at the end of the string in the form of a tuple preceded by a % sign. 

num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print ('The square root of %0.2f is %0.4f' %(num, num_sqrt))



#This program also illustrates the use of format strings (%0.2f)  to format the output. 

# Get inputs from the user
base = float(input('Enter length of the base of the triangle: '))
height = float(input('Enter the height of the triangle '))
 
# calculate the area of the triangle
triangle_area = (base * height) / 2

# Display the results
print ('The area of the triangle is %0.2f' % triangle_area)

 Note that when only one variable is being formatted, a tuple is not used.

|



**k. String formatting with the format method**

This is another method for formatting strings. When you use the curly braces or {} operators, they serve as place-holders for the variables you would like to store inside a string. In order to pass variables to a string you must call upon the .format() method.

fname = "John"
lname = "Doe"
age = "24"

print ("{} {} is {} years old." .format(fname, lname, age))

John Doe is 24 years old.


Note: You can also use:


print ("{0} {1} is {2} years old." .format(fname, lname, age))

Where the number indicate the position of the placeholders



|

**l. Mathematical Opeerations and Strings**

In general, mathematical operations on strings are illegal:

'2'-'1'    'eggs'/'easy'    'third' * 'a charm'




|


Lists
---------


Lists are collections of items (strings, integers, or even other lists), e.g.,

 >>> y = [1,2,3, “Jim”]



Lists are widely used in GIS, e.g., list of feature classes, list of records, list of fields, list of numbers, etc.


|


**List Creation**

>>> list1 = ['one', 'two', 'three', 'four', 'five']

>>> numlist = [1, 3, 5, 7, 9]

>>> list1= [ ]   # creates an empty list

|




List Operations
-----------------


**a. Get the length of a List**

>>> list1 =  ["1", "hello", 2, "world"]

>>> len(list1) # Use the len function

 4

|


**b. Accessing members of a list**

Use the index of the value in the list surrounded by square brackets to get to the members of the list.


>>> print (list1[0], list1[1])
 

|


**c. Deleting List Elements**

>>> del list1[2];



|


**d. Append values to a List**

List append will add the item at the end. If you want to add at the beginning, you can use the insert function.

.. code-block:: python
   :linenos:

   list = ["Movies", "Music", "Pictures"] 
   list.append("Documents" ) # will add "Document" to the list
   list 

["Movies", "Music", "Pictures", "Documents"]   

|



**e. Sorting a List**

You can sort a list with the following code:

.. code-block:: python
   :linenos:

   list = ["Movies", "Pictures", "Actors", "Cinemas"] 
   list.sort() 
   list

['Actors', 'Cinemas', 'Movies', 'Pictures']


|


**f. Summing a List**

You can sum a list with the following code:

.. code-block:: python
   :linenos:

   list = [890, 786, 1234, 65, 345, 500]
   Sumlist = sum(list)
   print (Sumlist)

3820

| 


**g. Adding Two List Elements**

Lists cannot be added with the simple use of an addition sign, i.e., list1 + list2. We have to iterate the list, then get the corresponding values and do the addition.

.. code-block:: python
   :linenos:

   # Set up the lists 
   list1 = [11, 21, 34, 12, 31, 26]
   list2 = [23, 25, 54, 24, 20, 35]

   #Create an empty list to store the sum of values at the same index position
   result_list = []

   #Get the length of one of the lists. If the list lengths are unequal, use the shorter list.
   list_to_iterate = len(list1)

   #Iterate the list adding the corresponding values at the running index from the two lists, and insert the sum into a new list.

   for i in range(0, list_to_iterate):
       result_list.append(list1[i] + list2[i])

   # Print resultant list 
   print ("Test Result is: " + str(result_list))

Test Result is: [34, 46, 88, 36, 51, 61]

We can use the same logic for subtracting, multiplying and dividing two lists.


|


**h.  Graphing a List**

You can graph a list with the code below:


.. code-block:: python
   :linenos:

   import matplotlib.pyplot as plt

   cases = [890, 786, 1234, 65, 345, 500]
   year = (1950, 1960,1970,1980,1990,2000)

   plt.plot (year, cases)

   plt.xlabel ("Year")
   plt.ylabel ("Cases")
   plt.show()


|


**i. List Slicing**

>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

To retrieve a number from the list, just type the list name with the index number in square brackets, e.g.,

>>> print my_list[4]    # This prints out 5, which is the 4th number in the list counting from zero.
  


The syntax for slicing is

listname (start, stop, step)

 

>>> my_list[1:4] # Prints out the numbers between 1 and 4, but not including 4.
 [1,2,3]


>>> my_list[1:8:2] #Prints out the numbers between 1 and 8, skipping every other number. 
 [1,3,5,7]


|


**i. Negative Slicing**

>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> my_list[-1] # Prints out the last number in the list. 
 9


>>> my_list[::-1] # 
 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]



If there is no value before the first colon, it means to start at the beginning index of the list. If there isn't a value after the
first colon, it means to go all the way to the end of the list.


|


Tuples
-------

A List is a collection which is ordered and changeable. Allows duplicate members. On the other hand, a tuple is a collection which is ordered and unchangeable. Allows duplicate members.


A tuple is similar to a list, but the ordering of the values do not change once created.
Coordinate values whose sequence must be maintained to draw a polygon can be stored as tuples.

>>> tup1 = ('physics', 'chemistry', 1997, 2000)
>>> tup2 = (1, 2, 3, 4, 5, 6, 7 )

|

Basic Tuples Operations
-------------------------

Tuple operations are similar to list operations

>>> len((1, 2, 3)) 
 3    - Length

>>> (1, 2, 3) + (4, 5, 6)  
 (1, 2, 3, 4, 5, 6)   - Concatenation

>>> ('Hi!',) * 4  
('Hi!', 'Hi!', 'Hi!', 'Hi!')   - Repetition

>>> for x in (1, 2, 3): print x,  
 1 2 3  -  Iteration


|

**References**

https://www.techbeamers.com/python-add-two-list-elements/
