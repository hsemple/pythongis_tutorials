Functions
===========

|

What are Functions?
--------------------


In programming, a function is a named sequence of statements that performs a computation.  Functions are used to avoid rewriting code everytime a particular task is required to be completed. For example, suppose you have to write a program in which you have to calculate the area of five different fields at different times in the program. Instead of rewriting the code to calculate area each of the five times, we can write a single function to compute area so whenever an area calculation is needed in the program, we simply call the function to do the job. 

Each time we call the area function, we would have to pass it the length and width parameters of the field and the computation would be performed. After performing the computation, the function would return the answer to the statement that called it.  

The example below shows a function that calculates area based on length and width values that have been passed to it.


.. code-block:: python

   def calculate_area(length, width):
      area = length * width
      return area

|


**Points to Note about Functions in Python**

1. Functions are started with 'def' keyword which stands for 'definition'.

2. Each function has a name.  The tern "calculate_area()" is the name of the function. The name is usually followed by opening and closing parenthesis.

3. The parenthesis is used to store arguments or values from the user that the function needs to perform calculations.

4. Indentation matters in Python! It determine what is in the function, and when the function ends.

5. The "return" keyword is used to send results back to the main routine.

6. To call the above function, use the function name followed by parentheses containing the length and width values. , e.g., 
         
             calculate_area(300, 245)


7. To call the function and store the output in a variabe named 'get_area', write:

        get_area = calculate_area(300, 245)

|



Function Examples
--------------------

1.  The code below is an example of a function that takes the temperature in Celsius and then prints the results in Fahrenheit results.

.. code-block:: python

   def convertTemp(temp):
       freezing = 32

       fahrenheit = (9 * celsius/5) + freezing
       print ("The temperature in Fahrenheit is", fahrenheit, "degrees")
       return fahrenheit


To call the function, type convertTemp and pass in a temperature value, e.g., convertTemp(20)




2. Function to multiply all the numbers in a list.


.. code-block:: python

   mylist = [8, 2, 3, -1, 7]

   def multiply(numbers):  
      total = 1
      for x in numbers:
          total *= x
      return total  


#call the function and submit the list
print(multiply(mylist))





3. The function below takes a number and evaluates it in relation to the number 10. 

.. code-block:: python

    def number(x):
       if x < 10:
          print (x, "is less than 10")
       elif x > 10:
          print (x, "is greater than 10")
       else:
           print ("your number is 10")
        print ("Goodbye")


Call the function:  number (100)



4. The function below plots a graph. X1 and x2 define the range of the graph over the x axis. 


.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np

    def createline(x1,x2):
        x = np.linspace(x1,x2)
        y = 2*x+1
        plt.plot(x, y, 'blue', label='y=2x+1')
        plt.title('Graph of y=2x+1')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()


Call the function:  createline(5,25)


|


5. Python function to find the factorial of a number.

.. code-block:: python

   def factorial(n):
      fact = 1
      while(n!=0):
         fact *= n 
         n = n-1
      print("The factorial is",fact)
    
   

   Call the function:  factorial(5)



|


Python’s In-built Functions
--------------------------------

Python has many built in functions. For example, input() is a function which reads and returns the text you type. However, on many occasions, we have to write our own functions.


**Type Conversion Functions**

| int(' 32')     = 32
| int(3.99999)   = 3


|


**Math Functions**

Here are some examples:


- math.floor(x) - Returns the floor of x, the largest integer less than or equal to x.  

- math.exp(x) - returns e raised to the power x, where e = 2.718281… is the base of natural logarithms.

- math.atan(x) - returns the arc tangent of x, in radians. 

-  math.cos(x) - returns the cosine of x radians

-  math.pow(x, y) - returns x raised to the power y. 




To use the math functions, you have to first import the math library

>>> import math

Next,  you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called dot notation, e.g

>>> math.sqrt(2) / 2.0

0.707106781187

>>> pow(2, 20) #raises 2 to the 20th power.

|


Variable-length arguments in Python Functions
------------------------------------------------

Functions do not always have a fixed number of arguments. Sometimes, it is not always possible to know beforehand how many arguments will be passed to the function.  For example, in a spatial interpolation exercise, it is possible to estimate the unknown value from three or four or any number of nearby values.  In such a case, the function must be designed to handle any number of arguments that will be passed to it.


In Python, we define a variable argument using an asterisk ('*') followed by a variable name.  By convention, the variable name is called "aargs" but  name can be used.  A tuple is used to store the values passed to *args and you can send zero or more arguments to the function.  Also, a formal argument cab be placed before the *args variable but not after it. 



The following example demonstrates the usage of a function that takes variable length arguments.



.. code-block:: python

   def add_num(*args):
       sum = 0
       for num in args:
          sum += num
       return sum
    
       result = add_num(1, 2, 3)
       print('Sum is', result)

       result = add_num(10, 20, 30, 40)
       print('Sum is', result)
 
       result = add_num(5, 6, 7, 8, 9)
       print('Sum is', result)


|

Python Docstrings
-----------------

Python docstrings are strings used to document code.  They are placed right after the definition of a function, as in the example below.


.. code-block:: python

    def square(n):
        '''Takes in a number n, returns the square of n'''
        return n**2

    print(square.__doc__)



|

Here is the docstrings for the built-in function int() function in Python. Run it and note the results.  Click on this `hyperlink <https://www.programiz.com/python-programming/docstrings>`_ to learn more about Python docstrings.


.. code-block:: python

    print(int.__doc__)


|



Arcpy Functions
-----------------

Arcpy has many functions which are used to support ArcGIS workflows from a Python perspective.  Take a look at this `list of ArcPy functions <https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/alphabetical-list-of-arcpy-functions.htm>`_


When working with arcpy's functions, we must first import the arcpy library into our development environment then call the function. To call the function, we write arcpy followed by the name of the function and any arguments that the function requires, for example, arcpy.function_name(arguments).


In the code sample below, we are using ArcPy's ListField() function to print out a list of the fieldnames in a shapefile's attribute table. 


.. code-block:: python

   #Listfields function

   import arcpy
   arcpy.env.workspace = "c:/data"
   fieldlist = arcpy.ListFields("roads.shp", "", "String")

   for field in fieldlist:
      print (field.name)

|


In the script below,  Arcpy's ListRaster function is being used to print out a list of raster files in a folder. Run the using your own data.  Study each line of the code to understand the script in its entirety.


.. code-block:: python

   import arcpy

   # Set the workspace that contains the rasters 
   arcpy.env.workspace = "C:/data/rasters"

   # Use the ListRaster function to return a list of rasters .
   rasters = arcpy.ListRasters()

   # print name of feature class
   for rst in rasters:
      print (str(rst))

|


#Get a list of field names in the roads shapefile


.. code-block:: python

    import arcpy
    arcpy.env.workspace = "c:/data"

    fieldlist = arcpy.ListFields("roads.shp")
        for field in fieldlist:
             print (field.name, field.type, field.length)

 

  #Get a List of all the Feature Classes in a Directory


.. code-block:: python

    import arcpy
    arcpy.env.workspace = "C:/data"

    fcList = arcpy.ListFeatureClasses ()
    for fc in fcList:
       print (fc)  




 #Get a List of Tables in a geodatabase

.. code-block:: python

    import arcpy

    # Set the current workspace
    arcpy.env.workspace = "c:/data/mydata.gdb"

    # Get and print a list of tables
    tables = arcpy.ListTables()
    for table in tables:
        print(table)


|




Resources
-----------

* `Creating and Using Functions <https://vimeo.com/107270986>`_
* `An overview of ArcPy functions <https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/alphabetical-list-of-arcpy-functions.htm>`_

|



Exercises
-----------

1. Write a Python function that squares each value in a list that is passed to it. The results should be passed to the calling statement and printed out.

  
     my_list = [11,14,15,100, 34, 67, 89, 90, 98]


2. Define a function that accepts radius and returns the area of a circle.


3. Define a function that accepts two numbers as arguments and returns the first number raised to the power of the second number.

4. Rewrite the spatial interpolation program you wrote in the second lab as a function.

5. Rewrite the gravity model that appears in geography textbooks as function.

6. The script sbelow uses arcpy's buffer function to buffer a shapefile.  Run the script using your own data. Comment it to show your understanding of the function.



.. code-block:: python
   :linenos:

   import arcpy

   try:
     infc = r"C:\mydata\California\California.shp"
     outfc = r"C:\mydata\California\CA_Buffered.shp"

     bufferDistance = 2000

     arcpy.Buffer_analysis(infc, outfc  bufferDistance", "", "", "ALL")





7. The script below is another arcpy buffer script to buffer multiple feature classes. . Run the script using your own data. Comment it to show your understanding of the script.



.. code-block:: python
   :linenos:

   import arcpy

   #Set geoprocessing environments
   arcpy.env.workspace = r"C:\mydata\California"
   arcpy.env.overwriteOutput = True

   #Create list of feature classes
   fclist = arcpy.ListFeatureClasses()


   #Provide a list of distances to be used for buffering
   distances = [1000, 5000, 8000]


   # Create a loop to buffer the list of feature classes

   for distance in distances:
       for fc in fclist:
            arcpy.Buffer_analysis(fc, "_Buffer" + str(distance),  "distance", "", "", "ALL")








