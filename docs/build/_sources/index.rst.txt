


Welcome to Python GIS Tutorials
==========================================

This website provides information on the use of Python in GIS. Python has many uses in GIS including the ones listed below:

   1. Performing traditional GIS operations without the use of dedicated GIS software such as ArcGIS or QGIS. Such operations include thematic mapping, attribute and spatial queries, changing map projections, terrain analysis, geocoding, spatial analysis, geoprocessing, spatial statistics, etc. Instead of relying on dedicated GIS software, many organizations and individuals simply use Python to perform required GIS operations.

   2. Batch processing large amount of datasets. This is especially important for geoprocessing situations when the same operations must be repeated many times; Examples of batch include clipping 1,000 shapefiles to the extent of a study area, or reprojecting 1000 layers to a new coordinate system. The use of Python saves lots of time in these situations as the software will quickly and precisely repeat the desired operations any number of times. Batch processing can be done by programming GIS software or Python geospatial libraries to conduct the operations.

   3. Python is used extensively to automate GIS workflows which involve many sequential steps. Such workflows include watershed delineation, site selection analysis, or any snumber of GIS steps an individual or organization may require to solve spatially related problem.

   4. Python can be used for building APIs and and for reading data from APIs.

Python uses many widely available geospatial libraries to perform GIS operations. Such libraries include gdal, geopandas, rasterio, leafmap, shapely, plotly, fiona, earthpy, and many others. It also relies extensively on matplotlib for visualization.

As these are introductory tutorials, the topics covered deal mostly with using Python for traditional GIS operations, batch processing, and automating workflows. 

Since Python scripting in GIS relies on different spatial libraries, the example scripts provided in these tutorials are drawn from different spatial libraries.  This approach is intended to give readers a broad-based exposure to working with Python in GIS.  In addition, readers will be exposed to arcpy for the ArcGIS Desktop platform, PyQGIS for QGIS, and ArcGIS API for those working with ESRI products in a web-based environment.  


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:
   :numbered:

   getting_started.rst
   intro_programs.rst
   strings_lists_conditional.rst
   conditionals_and_looping.rst 
   functions.rst
   error_handling.rst
   object_oriented_programming.rst
   displaying_files.rst
   map_projections.rst
   attribute_and_spatial_queries.rst
   querying_rasters.rst
   geocoding.rst
   spatial_analysis.rst
   terrain_analysis.rst
   workflow_automation.rst
   api.rst
   search_algorithms.rst


