
Reading and Displaying Files
================================


To read a file, we must first open the file. This is done using Python's built-in open() function. The open() function returns a file object, which has a read() method for reading  files and storing their contents as variables .  Once a file is read and stored as a variable, the original file can be closed.  We can then loop through the file variable and do stuff with its contents.


`Download Earthquake Data <https://corgis-edu.github.io/corgis/csv/earthquakes/">`_



.. code-block:: python

	file = open("/Users/student/Desktop/Equakes2.csv", "r")
	text = file.readlines()
	file.close()

	for line in text:
	    print (line)



*Points to Note*

1. The open method has the following modes:

  | ‘r’ – Python read file. Read mode is used when the file is only being read
  | ‘w’ – Python write file. Write mode is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
  | ‘a’ – Python append file. Append mode is used to add new data to the end of the file; that is new information is automatically amended to the end
  | ‘r+’ – Special read and write mode is used to handle both actions when working with a file



2.  Always close the file after reading or writing to it. In most cases, upon termination of an application or script, a file will be closed eventually. However, there is no guarantee when exactly that will happen. This can lead to unwanted behavior including resource leaks and unwanted behavior.



|


Writing File Paths
--------------------

In Python, it is better not to write your file paths with backslashes as shown below:

.. code-block:: python

	file = open("C:\Projects\PacktDB.gdb\Chapter3Results\Intersect71Census", "r")



Writing paths with backslashes is not advisable because a Python string can contain special characters that also incorporate backslashes for other reasons, e.g.,  "\t" (tabs),  "\n" (newlines), "\r" ( carriage returns), etc.

These special characters make it very hard to create a file path that uses single backslashes because file paths in Windows also use single backslashes. There are several workarounds:



**1. Use Forward Slashes**

.. code-block:: python

   file = open("C:/Users/Student/Desktop/earthquakes.csv", "r")


|

**2. Use Raw Strings**

These are regular strings, but includes an r before the script begins.  The r tells the Python Interpreter that the string does not contain any special characters or escape characters.

.. code-block:: python

   file = (r"C:\Users\Student\Desktop\earthquakes.csv")



|


**3. Use Double Backslahes**

In this case, the backslashes are escaped using a second backslash.

.. code-block:: python

   "C:\\Users\\Student\\Desktop\\earthquakes.csv"


|


**4.  Use os.path.join**

The os module provides access to operating system functions regardless of the platform you are using, i.e, Windows, Mac OS, Linux, etc. 

os.path.join() takes any number of path strings and returns a single path using the platform-specific path separator. 



.. code-block:: python

	import os
	os.path.join("c:/", "Windows")

	>>> 'c:/Windows'

or

.. code-block:: python

	import os
	os.path.join('c:', os.sep, 'mydata')
	
	>>> 'c:\\mydata'

Note: os.sep will supply the separator


|


Opening a file using the "With" Statement
------------------------------------------

A second way  second way to open a file is to use the "with" statement.  The with statement automatically takes care of closing the file once it leaves the with block, even in cases of error. I highly recommend that you use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.

.. code-block:: python

	with open("/Users/student/Desktop/Equakes2.csv", 'r') as file:
	   text = file.readlines()
	for line in text:
	   print (line)


|


Now, let's open a data file then read its content into Python. After that, we will split the file contents into inidividual columns, and store the columns in variables

.. code-block:: python

	infile = open("/Users/student/Desktop/earthquakes.csv", 'r') 
	lines = infile.readlines() 
	infile.close() 

	del lines[0] # Remove the first line
	#Create empty lists 
	xvar = [] 
	yvar = []
	count = 0

	for line in lines:
	    elements = line.split(",") # splits the line
	    mag = float(elements[2]) # Get the data in the third column
	    dep = float(elements[3]) # Get the data in the fourth column

	    # Add magnitude and depth data to the empty lists 
	    xvar.append(dep) 
	    yvar.append(mag)



	#Print the two lists as columnss

	magnitude = "Magnitude"
	depth = "Depth"

	print ("%-15s %s" %(magnitude, depth))
	print ("")

	for c1, c2 in zip(xvar, yvar):
	    print ("%-15s %s" % (c1, c2))



|

**Reading a Data file into Python, Performing Calculations and Making a Graph**


.. code-block:: python

	import math
	import matplotlib.pyplot as plt
	infile = open("C:/Users/student/Desktop/Equakes2.csv, 'r')
	lines = infile.readlines()
	infile.close()
	del lines[0] # Remove the header line

	#Create empty lists
	xvar = []
	yvar = []
	std_dev = []
	count = 0
	sum = 0
	for line in lines:
	    elements = line.split(",") #splits the lines
	    mag = float(elements[4]) # Get the data in the fifth column
	    count = count + 1

	    # Add count and magnitude data to the empty x,y lists
	    xvar.append(count)
	    yvar.append(mag)
	    sum = sum + mag

	    #Calculate mean
	    average = sum / count

	print ("Average is",average)
	print ("")

	width = 1

	plt.figure(figsize=(4, 8)) 
	plt.bar(xvar, yvar, width, facecolor='orangered')
	plt.xlabel("No. of Earthquakes", fontweight='bold', fontsize='17', color = 'orange')
	plt.ylabel("Magnitude", fontweight='bold', color = 'orange', fontsize='12')
	plt.title("Magnitude of Earthquakes")
	plt.show()




|



Reading Data Files and Plotting Graphs Using Pandas
-----------------------------------------------------

The script above used many lines of code to open the file, compute average, and plot a graph.  We can achieve the same results with far fewer lines of code by using a specialized library named Pandas.  Pandas is a very powerful, popular and easy to use Python library for data analysis.  It has many Excel-like functions. Its primary object is the DataFrame, which can be thought of as an abstract database table or spreadsheet.  Once you create a dataframe object, you can use it to display tables, plot columns, create and run queries, with just a few lines of code. 

 
Let's plot the earthquake dataset using Pandas. 



.. code-block:: python

	import pandas as pd
	df = pd.read_csv("C:/Users/student/Desktop/Equakes2.csv")
	df


|



**Displaying Specific Columns of your Dataframe**

To select multiple columns, use a list of column names within the selection brackets [].  In the example below, we are selecting the earthquake depth and magnitude fields. 


.. code-block:: python
 
	import pandas as pd
	df = pd.read_csv("C:/Users/student/Desktop/Equakes2.csv")
	df[['depth', 'magnitude']]

|


Get the size of the table.

.. code-block:: python

	import pandas as pd
	df = pd.read_csv("/Users/hsemple/Desktop/earthquakes4.csv")
	df[["depth", "mag"]].shape

|

Filtering the Data Frame for Certain Rows

import pandas as pd
df = pd.read_csv("/Users/hsemple/Desktop/earthquakes4.csv")
above_3.5 = df[["mag"] > 3.5]
above_35.head()



|

Plotting Graphs
-----------------

Many types of graphs can be plotted by pandas. Below are seven types of graphs that are useful to know how to create.


The kind parameter accepts eleven different string values and determines which kind of plot you’ll create:

   | "area" is for area plots.
   | "bar" is for vertical bar charts.
   | "barh" is for horizontal bar charts.
   | "box" is for box plots.
   | "hexbin" is for hexbin plots.
   | "hist" is for histograms.
   | "kde" is for kernel density estimate charts.
   | "density" is an alias for "kde".
   | "line" is for line graphs.
   | "pie" is for pie charts.
   | "scatter" is for scatter plots.


|


**Line Graphs**

.. code-block:: python

	import matplotlib.pyplot as plt
	import pandas as pd

	df = pd.read_csv("/Users/student/Desktop/Equakes2.csv")
	df.plot(kind='line',y='Depth_mls',color='red', figsize=(6, 8))
	plt.show()




|


**Histograms**

.. code-block:: python

	import matplotlib.pyplot as plt
	import pandas as pd
	df = pd.read_csv("/Users/student/Desktop/Equakes2.csv")

	#df.plot.line(column = df.columns[3],  figsize=(6, 8))

	df.plot(kind='hist',y='Depth_mls',color='red',bins = 10, figsize=(6, 8))
	plt.show()




|



**Bar Plot**

.. code-block:: python

   import matplotlib.pyplot as plt
   import pandas as pd

   speed = [0.1, 17.5, 40, 48, 52, 69, 88]
   lifespan = [2, 8, 70, 1.5, 25, 12, 28]
   index = ['snail', 'pig', 'elephant','rabbit', 'giraffe', 'coyote', 'horse']

   df = pd.DataFrame({'speed': speed,'lifespan': lifespan}, index=index)

   ax = df.plot.bar(rot=10)
   plt.title("Speed vs Lifespan, Selected Animals")
   plt.show()




|



**Scatter**

To plot the Depth and Magnitude Data, write:

.. code-block:: python

	import matplotlib.pyplot as plt
	import pandas as pd
	df = pd.read_csv("/Users/student/Desktop/Equakes2.csv")

	df.plot(kind='scatter', x='Depth_mls',y='Magnitude', color='red',figsize=(6, 8))
	plt.show()


or

.. code-block:: python

	df.plot(kind='scatter',x='Depth_mls',y='Magnitude',color='red')

	plt.show()


 

|




Writing to a File
--------------------

Once we are done with data analysis, we can also write to a file, as shown below.


.. code-block:: python

	with open("C:/Users/student/Desktop/john.txt", "w") as f:
	    f.write('Hello \n')
	    f.write('Hello \n')
	    f.write('Hello \n')
	    f.write('Hello \n')
	    f.write('Hello \n')
	    f.write('Hello \n')
	    f.write('Hello \n')
	f.close


|


Reading a Data file into Python, splitting its contents by columns, and storing the columns in variables

.. code-block:: python
 
	infile = open("C:/Users/student/Desktop/Equakes2.csv, 'r') 
	lines = infile.readlines() 
	newfile=open("C:/Users/student/Desktop/newfile.txt",mode="a+",encoding="utf-8")

	del lines[0] # Remove the first line
	#Create empty lists 
	xvar  = [] 
	yvar  = []
	count = 0
	sum   = 0

	for line in lines:
	     elements = line.split(",") # splits the line
	     mag = float(elements[4]) # Get the data in the fifth column 
	     count = count + 1

	     # Add count and magnitude data to the empty x,y lists 
	     xvar.append(count) 
	     yvar.append(mag)
	     sum = sum + mag
	     newfile.write("\n")
	     newfile.write(str(mag))

	#Calculate mean
	average = sum / count
	newfile2.write(str(average))
	infile.close()
	print ("The average earthquake magnitude is",round(average, 2))
	print ("")


|



Readings
-----------

Plotting Graphs with Matplotlib 

* Download Plotting Graphs with Matplotlib
* Reading and Writing Text Files
* File I/O. Reading and writing files 
* Customizing the legend
* https://automating-gis-processes.github.io/CSC18/index.html

