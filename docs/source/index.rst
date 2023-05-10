


Welcome to Python GIS Tutorials
==========================================

This website provides information on the use of Python in GIS. Python has many uses in GIS including the ones listed below:

   1. Performing traditional GIS operations without the use of dedicated GIS software such as ArcGIS or QGIS. Such operations include thematic mapping, attribute and spatial queries, changing map projections, terrain analysis, geocoding, spatial analysis, geoprocessing, spatial statistics, etc. 

   2. Batch processing large amount of datasets. This is especially important in geoprocessing situations when the same operations must be repeated many times, for example, clipping 1000 shapefiles to the extent of a study area, or reprojecting 1000 layers to a new coordinate system. The use of Python saves lots of time in these situations. Batch processing can be done by programming GIS software to conduct the operations or by using Python geospatial libraries.

   3. Python is used extensively to automate GIS workflows which involve many sequential steps. Such workflows include watershed delineation, site selection analysis, or any snumber of GIS steps an individual or organization may require to solve spatially related problem.

   4. Python can be used for building APIs and and for reading data from APIs.

Python uses widely available geospatial libraries to perform GIS operations. Such libraries include gdal, geopandas, rasterio, leafmap, shapely, fiona, earthpy, and many others. It also relies extensively matplotlib for visualization.

As this is an introductory course, the topics covered deal mostly with using Python for traditional GIS operations, batch processing, and automating workflows. 

Since Python scripting in GIS relies on different spatial libraries, the example scripts provided in the lessons are drawn from different spatial libraries.  This approach is intended to give readers a broad-based exposure to working with Python in GIS.  In addition, readers will be exposed to arcpy for the ArcGIS Desktop platform, PyQGIS for QGIS, and ArcGIS API for those working with ESRI products in a web-based environment.  


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
   terrain_analysis.rst
   workflow_automation.rst
   api.rst


