
Conditional Statements and Looping
=====================================

|

Conditionals 
------------

Unless otherwise directed, lines of codes in a procedure run sequentially, from first to last. Conditional statements can change the sequential flow of program based on whether a given condition is true or false.

Python uses the If statement for testing conditions. If the condition is true, then the code block following the if statement is executed. If it is isn’t true, the program jumps to the end of the code block.A colon is placed at the end of the condition statement, and the lines below the condition statement are indented. 



There are three types of conditional structures in Python:

    | – if ..
    | – if.. else
    | – if ..elif .. else


|


**The If.. Conditional Structure**

If the condition is true, tht is, if the variable is defined, then the block following will be executed.

 
.. code-block:: python
   :linenos:

   if condition:  # if the variable is defined
       execute statement


Here is a another example:

.. code-block:: python
   :linenos:

   var1 = "blue"

   if  var1:
      print ("The sky is blue.")


 |


**The If.. Else Conditional Structure**

.. code-block:: python
   :linenos:

   if condition:  # if condition is true.
       execute this statement

   else:

     execute these statement



.. code-block:: python
   :linenos:

    answer = int (input("Please enter a number: "))
    if answer == 5:
    print ("My lucky number.")
       print ("That is not my lucky number")

 



** The If.. elif.. Else Conditional Structure**


.. code-block:: python
   :linenos:

   if condition:
      execute statements
   
   elif condition:    
      statements ...

   else:
    statements

 


.. code-block:: python
   :linenos:
 
   # Guess a number
   import random
 
   answer = int(input ("Please enter a number between 0 and 100: "))

   x = random.randint(0,100)

   print ("You entered", answer)

   if answer == x:
       print ("That's my lucky number.")

   elif answer > x:
       print ("That number is too large to be my lucky number")

else:
    print ("That's too small to be my lucky number")


|



Comparison Operators
----------------------

Python has many different operators for testing conditions including:
   |  == (Double equal sign) : tests equality, is equal to
   |  != (Excl. mark and equal sign): tests inequality, is not equal to
   |  >, < (greater than, less than)



**Equal Sign vs Double Equal Sign**

 =  The single equal sign is used to assign values to variables.  The double equal sign is used to test for equality of two variables.

 


Testing Equality

.. code-block:: python
   :linenos:
   
   list1 = [11, 21, 34, 12, 31, 26]
   list2 = [23, 25, 54, 24, 20, 35, 40, 46]

   if len(list1) != len(list2):
        print("Error:  Lists have unequal lengths")



|



Looping
----------

In programming, looping is used to execute a block of code repeatedly until a certain condition is met.  It is a simple concept that has widespread usage in programming.

Python uses the for loop and the while loop for iteration or repetitions.  For loops are used when you know beforehand the amount of times you want to loop.m While Loops enable you to test for a particular condition and are used when you don’t know beforehand how many times the loop will occur.


|


For Loops
----------

General Pattern


.. code-block:: python
   :linenos:

   for var in sequence:  # for each item of a variable that is in a particular sequence
        statements       # do something.

 
|

**Examples**

.. code-block:: python
   :linenos:

   x = [1, 2, 3, 4, 5]
   for num in x:
       print (num)



.. code-block:: python
   :linenos:

   for num in range(1,6):
       print (num)

 
Notes:
num is a made-up variable name. You can use any name
range (1,6) is a python function that takes a lower and upper value. It gives numbers between the given range


|

**For Loops and Lists**

For loops are great for manipulating lists


.. code-block:: python
   :linenos:

   a = [‘cat’, ‘dog’, ‘window’, ‘Main Street’]
   for x in a:
      vprint (x)
 
| Results
| cat
| dog
| window
| Main Street

|



**Nested For Loops**

.. code-block:: python
   :linenos:

   suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
   values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
   for suit in suits:
      for value in values:
          print (str(value) + " of " + str(suit))

      print ( " " )


In the above example you enter the first loop visiting “Spades”, then immediately jump to the nested loop printing out the value for each card.  When the program reachs the end of the list of “values’, it jumps out of the nested loop and return to the first loop to get to “Clubs. Then you loop through all values in the second suit and print the card names. This process continues until all the suits and values have been looped through.


|

**Multiplication Tables**


.. code-block:: python
   :linenos:

   for i in range(1,13):
      for j in range (1,13):
           print (i * j, end="\t")
      print ("")


|



For Loops  with Break and Continue
-----------------------------------------
 

**Break**

Break is typically part of a conditional \ looping situation in the program.  If the "if condition"  evaluates to false, break will not be  activated and the program will keep looping normally.   If the condition evaluates to true, 'break' is activated and the code jumps out of the loop entirely and moves to the next block in the program.



Run the code below to study "break"


.. code-block:: python
   :linenos:

   #1st code block

   for letter in 'Python':
      print (letter)
      if letter == 'h':
         break
   print ('Hello World')

| P
| y
| t
| h
| Hello World


|


#2nd code block


.. code-block:: python
   :linenos:

   for i in range (100000000):
       print (i)

       if i > 5:
           break
       else:
           print ('hello')

| 0
| hello
| 1
| hello
| 2
| hello
| 3
| hello
| 4
| hello
| 5
| hello
| 6


|

**Run the code below to study "continue"**

When the condition evaluates to false, the program will keep looping. normally. When it evaluates to true, it will stop executing that particular iteration of the loop and continue on to the next iteration in the loop.   



Try the code below to see how 'continue' works.

.. code-block:: python
   :linenos:

   for letter in 'Python':
      if letter == 'h':
          continue
      print ('Current Letter :', letter)


| Current Letter : P
| Current Letter : y
| Current Letter : t
| Current Letter : o
| Current Letter : n
 
 
 |

 .. code-block:: python
   :linenos:

   for i in range (100):
        print (i)
        if i > 5:
           continue
        else:
           print ('hello')

|




While Loops
-------------

While loops are used when you cannot predict at runtime the number of times an operation will occur.



**While Loop Structure**

 .. code-block:: python
   :linenos:

   while condition:
       statements


As long as the condition is true, the while statement will execute. When the expression is evaluated as False, the loop halts.


Example 1

 .. code-block:: python
   :linenos:

   x = 1
   while x < 5:  # condition
         print (x)
         x = x + 1   # counter

| 1
| 2
| 3
| 4

|

**Use of Plus Equal**

When writing counters, you can write  x = x + 1

 .. code-block:: python
   :linenos:

   x = 1
   while x < 5: # condition
        print (x)
        x = x + 1 # counter

|


You can also use the plus equal term "+=" to add another value to the variable's value and assign a  new value to the variable.


 .. code-block:: python
   :linenos:

   x = 1
   while x < 5: # condition
       print (x)
   x += 1 # counter

|

Operators such as -=, *=, /= do similar for subtraction, multiplication and division.


|


Example 2

 .. code-block:: python
   :linenos:

   max = 5
   n = 1
   a = [ ] # Create empty list

   while n < max:
        a.append(round((1.0/n),2)) # Append element to list
        n = n + 1
     print (a)


[1.0, 0.5, 0.33, 0.25]

|


Example 3


 .. code-block:: python
   :linenos:

    number = 23
    running = True

    while running:
        guess = int(input('Enter an integer : '))
        if guess == number:
        print ('Congratulations, you guessed it.')
        running = False # this causes the while loop to stop

    elif guess < number:
        print ('No, your guess is too low.')

    else:
        print ('Incorrect Guess. Too high. Try again')

 

 

**While Loop with "Continue"**
# Continue causes the program to break out of the particular iteration it is executing. See example below:


 .. code-block:: python
   :linenos:


   number = 23

   while 1:
       guess = int('Enter an integer : '))
       if guess == number:
          print ("You guessed the correct number")
          print ("Start a new round of guessing!")
          continue
       elif guess < number:
             print ('No, it is a little higher than that.')
       else:
             print ('No, it is lower than that.')

 

|

While Loop Example With "Break"
"Break” causes the program to jump out of the loop and move to the next block in the program" if one exists.


 .. code-block:: python
   :linenos:
   
   number = 23

   while 1:
        guess = int(input('Enter an integer : '))
        if guess == number:
            print ('You guessed the correct number.')
            break
        elif guess < number:
            print ('No, it is a little higher than that.')
        
        else:
            print ('No, it is lower than that.')


|




Repeating a program until the user wants to quit.

 .. code-block:: python
   :linenos:

   while 1:
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
       num3 = float(input("Enter the third number: "))


       print ("The average of the numbers is", (num1 + num2 + num3) / 3)


       y = int(input("Do you want to repeat? Enter 1 for yes, 2 for No"))

       if y == 1:
          continue
       else:
           print ("End of Program")
           break
           print("")

 

 

Looping, Performing Calculations and Populating an Empty List

Example

 .. code-block:: python
   :linenos:

   nums = [0, 1, 2, 3, 4]
   squares = [ ]
   for x in nums:
      squares.append(x ** 2)
      print(squares)


|


**List Comprehension**

The code below represents a typical way to loop and perform an operation on a set of numbers:


 .. code-block:: python
   :linenos:

   nums = [ 1, 2, 3, 4]
   results = [ ]
   for x in nums:
       results.append(x / 2)

   print(results)

[0.5, 1.0, 1.5, 2.0]




List comprehensions provide a concise way of looping, populating lists, and performing operations. Instead of populating a list using the method shown above, you can reduce your looping code by using a list comprehension.  The general syntax is:

 

new_list = [expression for member in iterable object]



#Example.  Square the values in the list 


 .. code-block:: python
   :linenos:

   nums = [1, 2, 3, 4, 5]
   results = [x /2 for x in nums]
   print(results)]

[0.5, 1.0, 1.5, 2.0]

|

To use the syntax, do the following:

* Define your list that you wish to iterate
* Come up with a descriptive name for the result list, e.g., 'results'.
* Open a pair of square brackets and define the expression that will generate the values you want to store in the new list. In this example the expression is x/2, which divides each value in the list by 2.
* Write a for loop to generate the numbers you want to feed into the expression.  Notice that no colon is used at the end of the 'for' statement. The result is the same list of square numbers you saw earlier

|


The syntax can be expanded to include more than 1 for clause.  It can also include if statements.


 .. code-block:: python
   :linenos:

   nums = [0, 1, 2, 3, 4]
   squares = [x **2 for x in nums if x < 8]
   print(squares)]

   The list comprehension always returns a result list.


| 



Looping and GIS
-----------------

Looping is used repeatedly in GIS scripting. For example, you might need to iterate through rows in a table, or fields in a table, or feature classes in a folder. You might even need to loop through the vertices of a geographic feature and do something with the vertices.  The scripts below show examples of looping in GIS using the ArcPy library.



**Getting a List of fields in a Shapefile's Attribute Table**


The syntax is: ListFields (dataset, {wild_card}, {field_type})



.. code-block:: python
   :linenos:
   
   import arcpy
   arcpy.env.workspace = "c:/data"

   fieldlist = arcpy.ListFields("roads.shp")
          for field in fieldlist:
                print (field.name, field.type, field.length)


|


Get a List of all the Feature Classes in a Directory or a Geodatabase

.. code-block:: python
   :linenos:
   
   import arcpy
   arcpy.env.workspace = "C:/data"

   fcList = arcpy.ListFeatureClasses ()
    for fc in fcList:
        print (fc)  




