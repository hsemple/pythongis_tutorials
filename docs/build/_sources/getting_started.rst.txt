




Development Environments
==========================

For these tutorials, we will run Python in the following development environments: The Standard Python Distribution, Anaconda Distribution, ArcGIS Pro, ArcGIS API for Python, and QGIS. 


|


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



|
 


 
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

 .. image:: img/python_notebook.png
   :alt: Python's Notebook in ArcGIS Pro 


3. If you wish to add new libraries to ArcGIS, you will first have to clone Python's default environment in ArcGIS Pro then install the new libraries to the cloned environment.  This `ESRI tutorial <https://support.esri.com/en/technical-article/000020560>`_shows  how to clone Python's default environment within ArcGIS Pro.
 

 

|


Python Window in ArcGIS Pro 
-----------------------------
The Python window is a convenient environment for running the numerous geoprocessing tools that comes with ArcGIS. The environment is fully integrated with ArcGIS and saves the users the time needed to perform this configuration.



1. In ArcGIS Pro, select the Analysis tab. Depending on your version of ArcGIS Pro, you will be able to select the Python Window. As shown below, in ArcGIS Pro you can click the drop-down menu to the right of the Python button and click Python Window. In other versions, or you may just have to click on the Python Window.. This opens the Python window, as shown below.
   
 .. image:: img/new_jupyter_notebook.png
   :alt: New Python Notebook

  
2. The top section of the Python Window is called the transcript while the bottom section is called the prompt. The transcript is initially blank. The transcript provides a record of previously entered code and its results.

3. The prompt is where you type your code. When the Python window first opens, the message in the prompt reads Initializing Python interpreter, which means the window is getting ready to receive your code. After a few seconds the message is replaced with Enter Python code here, which means you can start typing your code. After you have opened the Python window for the first time, these messages don’t appear again in the current session.
See this link for a tutorial.
 


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

   >>> layer = iface.activeLayer()


5. Once you get a reference to the active layer object, you can access methods and properties associated with this object. For example, to get the name of the active layer, we write:
   
   >>> layer.sourceName()



|


**Accessing the QGIS Python Editor**

1.  The editor is used to write scripts that would be too lengthy to run from the Console Shell.   It can be accessed by right-clicking Show Editor in the upper part of the console.

2.  To write a simple script to print the names of the fields in the attribute table of a shapefile, we can enter ::

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


Jupyter Notebook with QGIS
-----------------------------

1. It is possible to run Jupyter notebook from within QGIS.  First, you must install the pyqgis modules into an environment. After than, you can with QGIS outside of the application itself. 

2. Create a Python GIS environment  - https://autogis-site.readthedocs.io/en/latest/course-info/create-python-gis-environment.html




|




Resources
------------

`Get started with Python in ArcGIS Pro <https://learn.arcgis.com/en/projects/get-started-with-python-in-arcgis-pro/>`_

`Getting started with Anaconda <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-nav-mac>`_

Getting Started With Python Programming (QGIS3) - https://www.qgistutorials.com/en/docs/3/getting_started_with_pyqgis.html

Customizing QGIS with Python (Full Course Material) - https://courses.spatialthoughts.com/pyqgis-in-a-day.html

Free and Open Source GIS Ramblings - https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/

GIS Python API documentation - https://qgis.org/pyqgis/master/

PyQGIS Developer Cookbook - https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html

Streamlining GIS with Automation - https://www.geospatialworld.net/prime/technology-and-innovation/streamlining-gis-with-automation/








