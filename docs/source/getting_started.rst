


<<<<<<< HEAD
Getting Started
=================
=======


Development Environments
==========================

For these tutorials, we will run Python in the following development environments: The Standard Python Distribution, Anaconda Distribution, ArcGIS Pro, ArcGIS API for Python, and QGIS. 
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420


|


<<<<<<< HEAD
Accessing Python
--------------------

1. Anaconda is a large Python distribution that has become very popular over the last several years.  One reason for its popularity is that it comes with many libraries already pre-installed. Also, we can run our code using Jupyter Notebook.  I strongly recommend that you download the `Anaconda Distribution <https://www.anaconda.com/products/distribution>`_. 
 
2. Some people  use the core Python software to run their code. However, by default this software lacks many libraries that you will need for GIS so you will have to install additional libraries. To download, visit Python's `homepage <https://www.python.org/downloads/>`_. Download the latest version.

3. Python is preinstalled in ArcGIS Pro and QGIS, so you can use Python from within these environment to run your code.


|



Setting up your Python Working Environment
--------------------------------------------

Setting up your Python working environment depends on the Python distribution you are using. Below I provide information on a few approaches to this task.


 
**Anaconda/ Jupyter Notebook**

* Click on this `link <https://www.edlitera.com/en/blog/posts/guide-how-to-start-jupyter-notebook#mcetoc_1gcqvj0h63>`_ for information on how to open a Jupyter Notebook on Mac OS or Windows.

*  To create a new conda environment we can run:

           conda create --name arcgis4


*  If you need to install a new package, open the Anaconda folder in Windows, look for Anaconda prompt.  When the Anaconda prompt starts, enter the command below to search for an install a new package.

           conda install package_name
 

Conda installs many libraries with ease, however, installation of the arcpy library needs some special attention. The links below are workflows for installing arcpy in Anaconda.
  * `Set up Anaconda with ArcGIS  <https://developers.arcgis.com/python/guide/understanding-conda/>`_
  * `Anaconda Conda Jupyter Notebooks and ArcGIS Pro <https://www.esri.com/arcgis-blog/products/api-python/administration/python-api-core-concepts-part-2/>`_

   



|


**Configuring the Python Core Distribution**


After installing the core Python software, you will need to do the following:

a. Add the Python 2.7 Directory to your System Path Environment Variable. ...
b. Install pip to Manage Your Python Packages. 
c. Install virtualenv to Create Local Python Environments for Your Projects.

Click `here <https://aaronstannard.com/how-to-setup-a-proper-python-environment-on-windows/>`_ for more details.

    
 .. image:: img/install_python.png
   :alt: Install Python

 

*Writing, Saving and Running Python Programs with IDLE*

Python has a shell window called IDLE  which gives you access to the Python interactive mode. It also has a file editor that lets you create and edit existing Python source files. 
=======
The Python Standard Distribution 
-----------------------------------------

Many people use the standard Python distribution along with needed GIS packages and their dependencies to run their GIS code. This is an excellent environment for doing GIS, however, users will have to manually install almost all the required packages and their dependencies.  This task can sometimes be difficult for beginners. 


1. To download the Python Core Distribution, visit Python's `homepage <https://www.python.org/downloads/>`_. Download the latest version.


2. After downloading, install the program on your computer.

 .. image:: img/install_python.png
   :alt: Install Python


3. Follow the `instructions <https://aaronstannard.com/how-to-setup-a-proper-python-environment-on-windows/>`_ on this page to do the following:

  a. Add the Python 3.x directory to your system path environment variable.   
  b. Install `pip  <https://phoenixnap.com/kb/install-pip-windows>`_ to manage your Python packages. 
  c. Install virtualenv to create local Python environments for your projects.

   
4. To begin entering code into Python, start the Python Interpreter or IDLE.  IDLE is an integrated development environment that lets you create and edit Python scripts. 


 .. image:: img/interpreter_idle.png
   :alt: Install Python

>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420


|
 


<<<<<<< HEAD
**Using Jupyter Notebook that is already installed with ArcGIS Pro.**

If you have ArcGIS Pro installed on your computer, you can run Python using Jupyter Notebook that is installed with ArcGIS Pro. 


This tutorial shows how to run Python using Jupyter Notebook that is installed with ArcGIS Pro. This is a good option as the connection between Python and Jupyter Notebook has been already configured.   
=======
 
Jupyter Notebook in Anaconda 
-------------------------------

Anaconda is a large Python distribution that has become very popular over the last several years.  One reason for its popularity is that it comes with many packages already pre-installed. Also, users can run their code using Jupyter Notebook, which is a nice, browser-based environment for running code. I strongly recommend that you use Jupyter Notebook for your Python GIS programming.


1. Download the Anaconda Distribution at `this site <https://www.anaconda.com/products/distribution>`_. 


2. Start Anaconda, then launch the Jupyter Notebook. 


 .. image:: img/jupyter_notebook.png
   :alt: Install Python


3. Click on this `link <https://www.edlitera.com/en/blog/posts/guide-how-to-start-jupyter-notebook#mcetoc_1gcqvj0h63>`_ for information on how to open a Jupyter Notebook on Mac OS or Windows.  The Jupyter development environment should appear as shown below.


 .. image:: img/jupyter_dev_environment.png
   :alt: Install Python



4. If you need to install a new package, open the Anaconda folder in Windows then click on Anaconda prompt.  When the Anaconda prompt starts, enter the command below to search for an install a new package. Conda installs many packages with ease, so you should use it often.

           conda install package_name


5. Alternatively, you can install new packages from within Anaconda Navigator, as shown in the illustration below.

 .. image:: img/install_packages.png
   :alt: Install Python


 
|


Jupyter Notebook within ArcGIS Pro
-------------------------------------

1. If you have ArcGIS Pro installed on your computer, you use Jupyter Notebook that is installed with ArcGIS Pro as your development environment. This is a good development environment to use as the connection between Python and Jupyter Notebook is already configured.   


2. To run Python using Jupyter Notebook that is installed with ArcGIS Pro, open ArcGIS Pro, then click on Project | Python | Python Notebook, This shown in the illustration below.
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

 .. image:: img/python_notebook.png
   :alt: Python's Notebook in ArcGIS Pro 


<<<<<<< HEAD
 
If you wish to add new libraries to ArcGIS, you will first have to clone Python's default environment in ArcGIS Pro, then install the new libraries to the cloned environment.  This tutorial shows you how to clone Python's default environment within ArcGIS Pro and install new libraries to the cloned environment.
 
=======
3. If you wish to add new libraries to ArcGIS, you will first have to clone Python's default environment in ArcGIS Pro then install the new libraries to the cloned environment.  This `ESRI tutorial <https://support.esri.com/en/technical-article/000020560>`_shows  how to clone Python's default environment within ArcGIS Pro.
 

>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
 

|

<<<<<<< HEAD
**Running Scripts from within ArcGIS Pro Using the Python Window**

In ArcGIS Pro, select the Analysis tab. Depending on your version of ArcGIS Pro, you will be able to select the Python Window. As shown below, in Python 2.7, you can click the drop-down menu to the right of the Python button and click Python Window. In other versions, or you may just have to click on the Python Window.
  

=======

Python Window in ArcGIS Pro 
-----------------------------
The Python window is a convenient environment for running the numerous geoprocessing tools that comes with ArcGIS. The environment is fully integrated with ArcGIS and saves the users the time needed to perform this configuration.



1. In ArcGIS Pro, select the Analysis tab. Depending on your version of ArcGIS Pro, you will be able to select the Python Window. As shown below, in ArcGIS Pro you can click the drop-down menu to the right of the Python button and click Python Window. In other versions, or you may just have to click on the Python Window.. This opens the Python window, as shown below.
   
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
 .. image:: img/new_jupyter_notebook.png
   :alt: New Python Notebook

  
<<<<<<< HEAD
 
 
This opens the Python window.
   

 .. image:: img/arcgis_python_window.png
   :alt: ArcGIS Python Notebook


The top section of the Python Window is called the transcript, and the bottom section is called the prompt. The transcript is initially blank. The transcript provides a record of previously entered code and its results.

The prompt is where you type your code. When the Python window first opens, the message in the prompt reads Initializing Python interpreter, which means the window is getting ready to receive your code. After a few seconds the message is replaced with Enter Python code here, which means you can start typing your code. After you have opened the Python window for the first time, these messages don’t appear again in the current session.
=======
2. The top section of the Python Window is called the transcript while the bottom section is called the prompt. The transcript is initially blank. The transcript provides a record of previously entered code and its results.

3. The prompt is where you type your code. When the Python window first opens, the message in the prompt reads Initializing Python interpreter, which means the window is getting ready to receive your code. After a few seconds the message is replaced with Enter Python code here, which means you can start typing your code. After you have opened the Python window for the first time, these messages don’t appear again in the current session.
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
See this link for a tutorial.
 


<<<<<<< HEAD

|

**Running Python Using Spyder**
 
 * Setting up Spyder to work with ArcGIS Pro 



 |


**Running Python from within QGIS**


*Running Python from the Console Shell*


1. Open QGIS and add this WFS layer. To do so, click on Add Layer | Add WFS Layer..., then select New and provide this URL: https://maps.gns.cri.nz/geology/wfs

2. Highlight the layer called NZL_GNS_250K_faults and select Add Layer to Project. 

.. image:: img/python_wfsLayer.png
   :alt: The NZL_GNS_250K_faults layer


3. From the main menu in QGIS, select Plugins | Python Console.  This will cause the Python Console to appear. It may open up towards the bottom of the application, however, if you wish, you can detach it from the main window and place it whereever you wish.


4. The lower part of the Console display with the >>> prompt. This is is where you type commands.  


5. The Python commands can be pure Python commands that have nothing to do with GIS or QGIS, or they can be Python commands ained at manipulating QGIS commands or user data.


6.  The iface class is used to access most graphical QGIS components. For example, to get a reference to the active layer, we can write:   
=======
|


ArcGIS API for Python
-----------------------

ArcGIS API for Python is a Python library for performing GIS visualization, analysis, and data management from within a Jupyter Notebook environment.  The ArcGIS API can be run from within ArcGIS Online or ArcGIS Enterprise.  

The ArcGIS API for Python is distributed as a conda package named *arcgis*. It can be run from within Anaconda and other Python Distributions.  See this `hyperlink <https://developers.arcgis.com/python/guide/install-and-set-up/>`_ for more information. 




|


The Python Console within QGIS
---------------------------------

Similar to ArcGIS Pro, Python can be run from within the QGIS software. Short codes can be run from a Console Shell while longer codes can be run from an editor.



**Running Python from the Console Shell**


1. From the main menu in QGIS, select Plugins | Python Console.  This will cause the Python Console to appear. It may open up towards the bottom of the application, however, if you wish, you can detach it from the main window and place it whereever you wish.

.. image:: img/python_console.png
   :alt: Python Console QGIS



2. The lower part of the Console display with the >>> prompt. This is is where you type commands.  


3. The Python commands can be pure Python commands that have nothing to do with GIS or QGIS, or they can be Python commands ained at manipulating QGIS commands or user data.


4.  The iface class is used to access most graphical QGIS components. For example, to get a reference to the active layer, we can write:   
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

   >>> layer = iface.activeLayer()


<<<<<<< HEAD
7. Once you get a reference to the active layer object, you can access methods and properties associated with this object. For example, to get the name of the active layer, we write:
=======
5. Once you get a reference to the active layer object, you can access methods and properties associated with this object. For example, to get the name of the active layer, we write:
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
   
   >>> layer.sourceName()


<<<<<<< HEAD
8.  You should get the response in the upper half of the console

     'NZL_GNS_250K_faults'



9. Now, let us get a count of the number of features in the layer:

>>> layer.featureCount()

=======
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

|


<<<<<<< HEAD
*Accessing the QGIS Python Editor**

1.  The editor is used to write scripts that would be too lengthy to run from the Console Shell.   It can be accessed by right-clicking Show Editor in the upper part of the console.

2.  We will write a simple script to print the names of the fields in the attribute table of the WFC layer ::
=======
**Accessing the QGIS Python Editor**

1.  The editor is used to write scripts that would be too lengthy to run from the Console Shell.   It can be accessed by right-clicking Show Editor in the upper part of the console.

2.  To write a simple script to print the names of the fields in the attribute table of a shapefile, we can enter ::
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

      layer = iface.activeLayer()

      for fld in layer.fields():
          print(fld.name())


.. image:: img/python_script1.png
   :alt: Python Script Print Name of Attribute Fields


3. The script below get the length of each fault segment and maintains keeps a running total of the lengths ::

    layer = iface.activeLayer()
    lengths = []
    for fault in layer.getFeatures():
        lengths.append(fault.attribute("shape_len"))
        print(sum(lengths))



|

<<<<<<< HEAD
**Using Jupyter Notebook with QGIS**
 

1. If you are familiar with Jupyter notebook, then you can use it with QGIS.  First, you must install the pyqgis modules into an environment. After than, you can with QGIS outside of the application itself. 
=======

Jupyter Notebook with QGIS
-----------------------------

1. It is possible to run Jupyter notebook from within QGIS.  First, you must install the pyqgis modules into an environment. After than, you can with QGIS outside of the application itself. 
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

2. Create a Python GIS environment  - https://autogis-site.readthedocs.io/en/latest/course-info/create-python-gis-environment.html



<<<<<<< HEAD
|




**Create an Anaconda environment that is compatible with ArcGIS Pro**


1. You can install the latest Anaconda for Windows via this link https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe 

2. To avoid breaking ArcGIS (or other software), uncheck the checkboxes (a) make Anaconda the default Python and (b) add Anaconda's Python to the PATH. I will install Anaconda3 at C:/Anaconda3

3. You can follow step-by-step above in macOS Spatial Stack section on creating environment, activate and deactivate, install package via channel.
Workflow to set up Anaconda with ArcGIS Pro 2.7

    
4. Copy the folder arcgispro-py3 from C:\Program Files\ArcGIS\Pro\bin\Python\envs and paste to C:\Anaconda3\envs

5. Rename the copied folder arcgispro-py3 in C:\Anaconda3\envs to arcgispro

6. Test the virtual environment

     * At the Anaconda Command Prompt, type: conda activate arcgispro
     * Type: conda list. You can see the list of packages installed

7. Add more packages

     * Let's add the Python Spatial Analysis Library (pysal) module.
     * Type the following command at the Anaconda Prompt: conda install pysal

8. Configure ArcGIS to see Anaconda and vice versa

        Anaconda Python to ArcPy

            Edit the ArcGISPro.pth (path) file within "C:\Anaconda3\envs\arcgispro\lib\site-packages".

            Change the relative ArcPy path to C:\Program Files\ArcGIS\Pro\Resources\ArcPy

            Change the relative ArcToolBox path to C:\Program Files\ArcGIS\Pro\Resources\ArcToolBox\Script

        Arcpy to Anaconda Python

            Create a zconda.pth (path) file with the content "C:\Anaconda3\envs\arcgispro\lib\site-packages" in it.

            Then Copy zconda.pth to C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages

        
        Testing in ArcGIS Pro

            Start ArcGIS Pro, open the Python window

            type "import pysal"

            type "pysal." A popup menu with a list of pysal-provided functions is a pretty good sign the install succeeded.

        Testing in PyCharm

            Start PyCharm, in File\Settings…, choose Project then Project Interpreter

            Ignore the drop down list for Project Interpreter, and click the cog button to Add Local, and in the file browser pick C:\Anaconda3\envs\arcgispro\python.exe

            
            To run your script, right click it in the Project window, and choose either Run or Debug

            Restart PyCharm for the Python Console to use the arcpro environment.


=======
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420

|


<<<<<<< HEAD
Resources
------------

=======


Resources
------------

`Get started with Python in ArcGIS Pro <https://learn.arcgis.com/en/projects/get-started-with-python-in-arcgis-pro/>`_

`Getting started with Anaconda <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-nav-mac>`_

>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
Getting Started With Python Programming (QGIS3) - https://www.qgistutorials.com/en/docs/3/getting_started_with_pyqgis.html

Customizing QGIS with Python (Full Course Material) - https://courses.spatialthoughts.com/pyqgis-in-a-day.html

Free and Open Source GIS Ramblings - https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/

<<<<<<< HEAD

=======
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420
GIS Python API documentation - https://qgis.org/pyqgis/master/

PyQGIS Developer Cookbook - https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html

Streamlining GIS with Automation - https://www.geospatialworld.net/prime/technology-and-innovation/streamlining-gis-with-automation/

<<<<<<< HEAD
Getting started with Anaconda - https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-nav-mac


 
=======
>>>>>>> 46e4da9bdd6f75a5d9039bf89d369caeca931420







