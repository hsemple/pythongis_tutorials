
Introduction the Python Language
==================================

In this module, we will look at the following aspects of the Python language:

* Hello World
* Variables
* Data Types
* Comments
* Basic Python Statements
* Simple programs 

Please vist the websites below to learn about the Python concepts listed above.

* `Python Basics <https://www.learnpython.org/en/Basic_Operators>`_

* `Creating Variables and Assigning Data <https://vimeo.com/104028282>`_

* `Python Statements <https://pynative.com/python-statements/>`_

* `Basic Python Statements <https://vimeo.com/105271585>`_


|



Practice Programs 
------------------

If you do not have a Python' interpreter already installed, you can can use the interpreter at this `website <https://www.programiz.com/python-programming/online-compiler/>`_.




**1. Write a program to calculate the average of three scores**

# Key functions in the program below are: input(), float(), and round().  

.. code-block:: python
   :linenos: 

   # Get the three scores
   num1 = float(input("Enter the first number: "))
   num2 = float(input("Enter the second number: "))
   num3 = float(input("Enter  the third number: "))
   
   # Calculate the average
   average = (num1 + num2 + num3) / 3

   # Print out the test score
   print ("the average score is: ", round(average,2))


 |


**2. Write a program that converts the temperature in Fahrenheit to Celsius**

# Note the formatting of the results in the print statement.  str(round(Celsius,2)) converts formats the results to two decimal places then converts the value to a string.   The plus sign concatenates or joins the first string with the second second string.

.. code-block:: python
   :linenos:

   Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
   Celsius = (Fahrenheit - 32) * 5.0/9.0
   print (str(round(Celsius,2)) + " degrees Celsius")

 

Note:

We can format the output even more as shown in the example below.

.. code-block:: python
   :linenos:

   Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
   Celsius = (Fahrenheit - 32) * 5.0/9.0
   print (str(round(Fahrenheit,2)) + " degrees Fahrenheit = " + str(round(Celsius,2)) + " degrees Celsius")



|

**3. Write a program to calculate the square root of a number**

In the code below, %0.2f and %0.4f' are formatted place holders for two variables. The variables appear at the end of the string in the form of a tuple preceded by a % sign. 


.. code-block:: python
   :linenos:

   num = float(input('Enter a number: '))
   num_sqrt = num ** 0.5
   print ('The square root of', num, 'is', num_sqrt)



|


**4. Write a Python Program to find the area of triangle**


.. code-block:: python
   :linenos:

   #This program also illustrates the use of format strings (%0.2f)  to format the output. 

   # Get inputs from the user
   base = float(input('Enter length of the base of the triangle: '))
   height = float(input('Enter the height of the triangle '))

   # calculate the area of the triangle
   triangle_area = (base * height) / 2

   # Display the results
   print ('The area of the triangle is',  triangle_area)

|



**5. Write a program that calculates the spatial interaction between two places using a simple form of the gravity model.**

.. image:: img/interaction.png
   :alt: Spatial Interpolation Concept

   

.. code-block:: python
   :linenos: 


   print ("Welcome to the gravity model calculation program")
   print ("------------------------------------------------")
   print ("")

   #Get the user's input
   P1 = input("Please input the size of the first city: ")
   P2 = input("Please input the size of the second city: ")
   Distance = input("Please input the distance between the two cities: ")
  
   # Calculate the interaction ,with output of decimal format
   PI = (int(P1)*int(P2))/(float(Distance)*float(Distance))

   #Print the result
   print (”The potential interaction between the two cities is", round(PI,2) )   
 
   #End of the program
   print ("Thanks for using this program...")


|


**6. String formatting with the format method**

Curly braces can serve as place-holders for the variables you would like to store inside a string. In order to pass variables to a string you must call upon the .format() method.

.. code-block:: python
   :linenos:

   fname = "John"
   lname = "Doe"
   age = "24"

   print ("{} {} is {} years old." .format(fname, lname, age))

John Doe is 24 years old.



Note: For the print statement, you can also use the line below where the number indicate the position of the placeholders

print ("{0} {1} is {2} years old." .format(fname, lname, age))



|



**7. Write a program to calculate the area of a circle**

The script below illustrates how to import a library (math) and use a function from the math library. Note that the dot notation is used to show that the pi function is related to the math library. 

.. code-block:: python
   :linenos:

   # Get inputs from the user
   import math
   radius = float(input("Enter the radius of the circle: "))
 
   circle_area = math.pi * radius ** 2

   # Display the results
   print('The area of the circle is', circle_area)


|



**8.  Write a Python program to display calendar of given month of the year**

The script below illustrates how to import the calendar library and use a function from the calendar library.


.. code-block:: python
   :linenos:

   import calendar

   # Get the month and year from the user
   yy = int(input("Enter year: "))
   mm = int(input("Enter month: "))

   # display the calendar
   print(calendar.month(yy, mm))


|

**9. Write a program to create a time stamp**

.. code-block:: python
   :linenos:

   #Note the use of concatenation, i.e., the use of the plus sign to join strings to create a single string.

   from datetime import datetime  
   now = datetime.now()
   mm = str(now.month)
   dd = str(now.day)
   yyyy = str(now.year)
   hour = str(now.hour)
   mi = str(now.minute)
   ss = str(now.second)

   print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


|


Lab 1
----------

Write a program that interpolates a single point value using the IDW method. (Links to an external site.)Links to an external site. As shown in the illustration below, we are trying to estimate a value for the unknown point (?) based on the nearest four surrounding values. Instead of calculating a simple average, we are weighting each z-value by the inverse of the distance between the location of the  z-value and the location of the point whose z-value is being calculated.

.. image:: img/interpolation.png
   :alt: Spatial Interpolation Concept


In terms of program flow, your program should prompt the user for each of the known points, zi.  (Tip: repeat the input statement z-values four times).  Next, it should also prompt the user for the distance of each of the z-value to the point that is being calculated (Tip: repeat the input statement for distance values four times).   Once all the z-values and distances are collected, the program should use these values along with the formula below to compute the z-value at the unknown location.   Demonstrate that your program works using the data in the above diagram.


Formula for Spatial Interpolation

.. image:: img/idw_formula.png
   :alt: IDW Formula


|


**Deliverables**


1. Submit the source code of your program as well as screenshot showing that the program successfully ran in Python.

