
Error Handling
================


In computing, exceptions are error conditions that occur in your code. Exception statements in Python enable you to trap and handle errors in your code, allowing you to gracefully recover from error conditions.


Exception handling makes your code more robust as it helps anticipate potential failures that would cause the program to stop in an uncontrolled manner.  Errors can be defined as the following types:

    * Syntax Error
    * Exceptions    
    * Out of Memory Error
    * Recursion Error
       

An exception object is created when a Python script raises an exception. 



|



Error Handling
-----------------

1. If error handling is not explicitly dealt with, Python will handle it for you, though in terse way that users may not always find easy to understand. In the code below, the correct path to myfile.txt is not given, so the Python interpreter throws an exception.


>>> f = open('myfile.txt')

.. role:: red

`Traceback (most recent call last):
File "<pyshell#31>", line 1, in <module>
f = open('myfile.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'`



Tracebacks are very important in figuring out what is wrong in your code and the line number in which the error lies.  When reading a traceback, start with the last line in the traceback. There, you will see the type of error and a brief explanation of the error. Above that you will see the text that is causing the error, then above that you will be given the file and line number of the error.



Although tracebacks are useful, they are not the most graceful way to handle errors in your code. It is possible to write code so that errors are handled gracefully.  



**Try ... Except Block**

To capture errors and deal with them gracefully, at a minimum, you can create a *try ... except* blocks, as shown below and enclose your code in the try block. Next, write an error message and place it in the except block.  When the code runs, if an exception occurs, it will be handled by the except block.


.. code-block:: python

    try:
         f = open('myfile.txt')

    except Exception:
        print ("Sorry. This file does not not exist.")


Sorry. This file does not not exist.




**The "Exception" keyword**

The "Exception" keyword  catches all types of error.  However, you can catch specific errors by using specific keywords. Note that you can have more than 1 exception blocks in your code.

.. code-block:: python

    try:
          f = open('myfile.txt')

    except FileNotFoundError:
          print ("Sorry. File not found.")

    except Exception:
           print ("Sorry. Something went wrong.")

 
 
Here are some Python specific Exceptions - https://docs.python.org/3/library/exceptions.html


Instead of writing your own error message, use Python's message.   Use (e) to capture the error message


.. code-block:: python

    try:
        f = open('myfile.txt')

    except FileNotFoundError as e:
         print (e)

    except Exception as e:
        print (e)


[Errno 2] No such file or directory: 'myfile.txt'


|



**Try...Except...Else**

In addition to the try... except block, you can also include an "else" block in your code. If there are no errors in the try block, the else block is executed.


.. code-block:: python

    try:
          f = open('/Users/semple/Desktop/test_file.txt')

    except FileNotFoundError as e:
         print (e)

    except Exception as e:
         print (e)

    else:
         print (f.read ())
        f.close()




7. You can also include a finally block in your code.   Finally runs regardless of exceptions.


.. code-block:: python

    try:
         f = open('/Users/semple1/Desktop/test_file.txt')

    except FileNotFoundError as e:
        print (e)

    except Exception as e:
        print (e)

    else:
        print (f.read ())
        f.close()

    finally:
         print ("Close down the database")




8. If you want to throw an error when a certain condition occurs use "raise". You could go about it like this:


.. code-block:: python

    x = int(input("Enter a value less than 5 "))
    if x > 5:
         raise Exception ('x should not exceed 5. The value of x was: {}'.format(x))



When you run this code, the output will be the following:


Traceback (most recent call last):
  File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10



The program comes to a halt and displays your exception to the screen, offering clues about what went wrong.



|



Handling ArcPy's Error Messages
--------------------------------



**Use Python's sys_info() function**

At a very basic level, you can use the sys_info() to capture the error message.   Note:  The sys.exc _info() function returns a tuple of three values that give information about the exception that is currently being handled.  The values returned are type of error,, the value of the error, and traceback, i.e., where the error is located.



In the code  below, Buffer, fails because the required buffer_distance_or_field argument has not been provided. Instead of failing without explanation, the except statement is used to trap the error, then fetch and print the error message generated by Buffer. Note that the except block is only executed if Buffer returns an error.

.. code-block:: python

    import arcpy
    import sys

    try:
        # Execute the Buffer tool
        arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
    except Exception:
        e = sys.exc_info()[1]
        print(e)
    

Failed to execute. Parameters are not valid.
ERROR 000725: Output Feature Class: Dataset C:\Users\Hugh\Desktop\California\California\Cali_buffer.shp already exists.
ERROR 000735: Distance [value or field]: Value is required
Failed to execute (Buffer).



Note:  sys.exc_info returns a tuple with three values: type, value, and traceback.   Type or (0) indicates the type of exception that is raised , i.e., arcgisscripting error.  Value or (1) relates to exception parameter errors, while traceback object (3) provides information on the exact memory location of the error.



Note: Instead of writing out sys.exc_info(1), you can omit it and write as except Exception as e:

.. code-block:: python

    import arcpy
    import sys

    try:
        # Execute the Buffer tool
        arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
    except Exception as e:
        print(e)
    


|


Use ArcPy GetMessages() function
----------------------------------


It is possible for arcpy to directly capture the messages returned by the geoprocessing tool using the GetMessages() function.  GetMessages() returns a list containing all messages from the last tool run.


.. code-block:: python

    import arcpy
    try:
       # Execute the Buffer tool
       arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
     except Exception:
        e = arcpy.GetMessages()
        print(e)



3. You can also get individual severity messages from the string returned by GetMessages().  Severity levels of messages are:

    0 —no errors
    1 —warning raised.
    2 —error raised.


.. code-block:: python

    import arcpy
    # Set current workspace
    arcpy.env.workspace = "c:/data/mydata.gdb"
    try:
     arcpy.Clip_analysis("Roads", "County", "Roads_Clip")
    except arcpy.ExecuteError:
     severity = arcpy.GetMaxSeverity()
     if severity == 2:
     print("Error occurred \n{0}".format(arcpy.GetMessages(2)))
     elif severity == 1:
     print("Warning raised \n{0}".format(arcpy.GetMessages(1)))
     else:
     # If the tool did not return an error or a warning
     print(arcpy.GetMessages())




4. More commonly, people simply use Getmessages()  with the severity level placed in the GetMessages function, i.e., GetMessages(2)

.. code-block:: python

    import arcpy
    import sys

    try:
        inputfile = "C:/Users/Hugh/Desktop/California/California/California.shp"
        outputfile = "C:/Users/Hugh/Desktop/California/California/Cali_buffer.shp"
        bufferdistance = 1000
        
        # Execute the Buffer tool
        arcpy.Buffer_analysis(inputfile, outputfile)
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
    


Failed to execute. Parameters are not valid.
ERROR 000725: Output Feature Class: Dataset C:\Users\Hugh\Desktop\California\California\Cali_buffer.shp already exists.
ERROR 000735: Distance [value or field]: Value is required
Failed to execute (Buffer).



|



Readings

Python Try ... Except 
Custom Exceptions
Links to an external site.
Error Handling with ArcPy


