Functions
===========

|

What are Functions?
--------------------


In programming, a function is a named sequence of statements that performs a computation.  The example below shows a function that calculates area based on length and width values that have been passed to it.


.. code-block:: python
   :linenos:

   def calculate_area(length, width):
      area = length * width
      return area


**Points to Note about Functions in Python**

1. Functions are started with 'def' keyword which stands for 'definition'.

2. Each function has a name.  The tern "calculate_area()" is the name of the function. The name is usually followed by opening and closing parenthesis.

3. The parenthesis is used to store arguments or values from the user that the function needs to perform calculations.

4. Indentation matters in Python! It determine what is in the function, and when the function ends.

5. The "return" keyword is used to send results back to the main routine.

6. To call the above function and store the output in a variabe named 'get_area', write:

        get_area = calculate_area(300, 245)

|


Function Examples
--------------------

1.  The code below is an example of a function that takes the temperature in Celsius and then prints the results in Fahrenheit results.

.. code-block:: python
   :linenos:

   def convertTemp(temp):
       freezing = 32

       fahrenheit = (9 * celsius/5) + freezing
       print ("The temperature in Fahrenheit is", fahrenheit, "degrees")
       return fahrenheit


To call the function, type convertTemp and pass in a temperature value, e.g., convertTemp(20)



2. The function below takes a number and evaluates it in relation to the number 10. 

.. code-block:: python
   :linenos:

    def number(x):
       if x < 10:
          print (x, "is less than 10")
       elif x > 10:
          print (x, "is greater than 10")
       else:
           print ("your number is 10")
        print ("Goodbye")


Call the function:  number (100)



3. The function below plot a graph. X1 and x2 define the range of the graph over the x axis. 


.. code-block:: python
   :linenos:

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


Python’s  In-built Functions
--------------------------------

Python has many built in functions. For example, input() is a function which reads and returns the text you type. However, on many occasions, we have to write our own functions.


**Type Conversion Functions**

int(' 32')     = 32
int(3.99999)   = 3


|


**Math Functions**

>>> import math

To use the math functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called dot notation, e.g

>>> math.sqrt(2) / 2.0

0.707106781187

>>> pow(2, 20) #raises 2 to the 20th power.

|



ArcPy Functions
-----------------

ArcPy has many functions which are used to support ArcGIS workflows from a Python perspective.  To call a function call,  we write arcpy followed by the name of the function and any arguments that the function requires, for example, arcpy.<function_name> (<arguments>)


In the code sample, we are using ArcPy's ListField() function to print out the name of the fields in a shapefile's attribute table. 


.. code-block:: python
   :linenos:

   #Listfields function

   import arcpy
   arcpy.env.workspace = "c:/data"
   fieldlist = arcpy.ListFields("roads.shp", "", "String")

   for field in fieldlist:
      print field.name)

|


# The following script uses ArcPy's ListRaster function to creaate a list of raster files and iterates through each file in the list and prints out their names. Try to identify the functions in the script.


.. code-block:: python
   :linenos:

   import arcpy

   # Set the workspace that contains the rasters 
   arcpy.env.workspace = "C:/Users/Hugh/Desktop/GuyNode_Images"

   # Use the ListRaster function to return a list of rasters .
   rasters = arcpy.ListRasters()

   # print name of feature class
   for rst in rasters:
      print (str(rst))

|


#Get a list of field names in the roads shapefile


.. code-block:: python
   :linenos:

    import arcpy
    arcpy.env.workspace = "c:/data"

    fieldlist = arcpy.ListFields("roads.shp")
        for field in fieldlist:
             print (field.name, field.type, field.length)

 

.. code-block:: python
   :linenos:

    #Get a List of all the Feature Classes in a Directory

    import arcpy
    arcpy.env.workspace = "C:/data"

    fcList = arcpy.ListFeatureClasses ()
    for fc in fcList:
       print (fc)  


|

Resources
-----------

Creating and Using Functions - https://vimeo.com/107270986 



Exercises
-----------

1. Write a Pyhton function that squares each value in a list that is passed to it. The results should be passed to the calling statement and printed out.

  
     my_list = [11,14,15,100, 34, 67, 89, 90, 98]

 
