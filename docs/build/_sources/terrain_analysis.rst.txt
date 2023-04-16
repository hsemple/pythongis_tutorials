
Terrain Analysis
===================

|


There are many python libraries that are available for terrain analysis.  Below, I use Arcpy, RichDEM, Rasterio, GDAL and pysheds for basic terrain analysis.  


|



Displaying DEM
----------------

Terrain analysis starts with displaying digital elevation models.  We have touched on this topic before.  Below, a DEM is displayed with the RichDEM library.  

.. code-block:: python

   import richdem as rd
   import numpy as np

   src = rd.LoadGDAL(r'/Users/.../elevation/w001001.adf')

   rd.rdShow(src, ignore_colours=[0], axes=False, cmap='jet', figsize=(8,5.5))



.. image:: img/stowe_dem_richdem.png
   :alt: DEM Loaded with RichDEM


|



Generating Hillshades
----------------------

Hillshades are used in terrain analysis to make elevation data appear more 3-Dimensional and thus visually appealing. Hillshades are also often used as an underlay to make other kinds of data more visually interesting.


|

**Generate Hillshade with ArcPy**


The two scripts below show how to generate hillshade maps using ArcPy within ArcMap or ArcGIS Pro.   


1. Run this script from the ArcPy Window.

.. code-block:: python

	from arcpy.ia import *
	out_hillshade_raster = Hillshade("elevation.tif", 180, 75, 0.3048)
	out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")



2.  This example calculates the hillshade using IDLE or any other IDE

.. code-block:: python

	# Import the system modules
	import arcpy
	from arcpy.ia import *

	# Set the analysis environments
	arcpy.env.workspace = "C:/arcpyExamples/data"

	# Set the local variables
	in_dem = "elevation.tif"

	# Execute the Hillshade function
	out_hillshade_raster = Hillshade(in_dem, 180, 75, 0.3048)

	# Save the output
	out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")


*Source*
https://pro.arcgis.com/en/pro-app/latest/arcpy/image-analyst/hillshade.htm



|


**Generate Hillshade  using GDAL**

.. code-block:: python

	from osgeo import gdal
	from numpy import gradient
	from numpy import pi
	from numpy import arctan
	from numpy import arctan2
	from numpy import sin
	from numpy import cos
	from numpy import sqrt
	from numpy import zeros
	from numpy import uint8
	import matplotlib.pyplot as plt



	def hillshade(array, azimuth, angle_altitude):
	        
	    x, y = gradient(array)
	    slope = pi/2. - arctan(sqrt(x*x + y*y))
	    aspect = arctan2(-x, y)
	    azimuthrad = azimuth*pi / 180.
	    altituderad = angle_altitude*pi / 180.
	     
	 
	    shaded = sin(altituderad) * sin(slope)\
	    + cos(altituderad) * cos(slope)\
	    * cos(azimuthrad - aspect)
	    return 255*(shaded + 1)/2


	ds = gdal.Open('/Users/semple/Desktop/topography/dem')   
	band = ds.GetRasterBand(1)  
	arr = band.ReadAsArray()

	hs_array = hillshade(arr,315, 45)
	plt.imshow(hs_array,cmap='gist_earth')
	plt.show()




.. image:: img/stowe_gray_scale.png
   :alt: Hillshade Calculated with GDAL


|

Generate Hillshade with Earthpy

.. code-block:: python

	import matplotlib.pyplot as plt
	import earthpy as et
	import earthpy.spatial as es
	import earthpy.plot as ep


	with rasterio.open('/Users/hsemple/Downloads/Wayne_DEM/county/wayne/topography/dem') as src:
	    elev = src.read(1)
	    
	    
	hillshade = es.hillshade(elev, azimuth=240, altitude=1)

	ep.plot_bands(
	    hillshade,
	    cbar=False,
	    title="Hillshade of Wayne County",
	    figsize=(10, 6),
	)
	plt.show()



For information in earthpy, see https://earthpy.readthedocs.io/en/latest/gallery_vignettes/plot_dem_hillshade.html#sphx-glr-gallery-vignettes-plot-dem-hillshade-py



|


.. code-block:: python


	import matplotlib.pyplot as plt
	import earthpy as et
	import earthpy.spatial as es
	import earthpy.plot as ep
	import matplotlib.colors as colors


	with rasterio.open('/Users/.../elevation/w001001.adf') as src:
	    elevation = src.read(1)
	    
	    
	#extent=[src.bounds[0], src.bounds[2], src.bounds[1], src.bounds[3]]

	hillshade = es.hillshade(elevation, azimuth=240, altitude=10)

	fig, ax = plt.subplots(figsize=(10, 6))
	ep.plot_bands(
	    elevation,
	    ax=ax,
	    cmap="terrain",
	    norm = colors.Normalize(vmin = 0, vmax = src_array.max()),
	    title="Digital Elevation Model (DEM)\n overlayed on top of a hillshade",
	)

	ep.plot_bands(hillshade, 
	              cmap='Greys', 
	              alpha=0.5, 
	              ax=ax, 
	              cbar=False)


	plt.show()


|





Slope Mapping
--------------------


**Generate Slope Map with Arcpy**


The two scripts below show how to calculate slope using ArcPy.   


1. Run this script from the ArcPy Window.

.. code-block:: python

   import arcpy
   from arcpy import env
   from arcpy.sa import *
   env.workspace = "C:/Washtenaw/county/washtenaw/topography" # Set your own path
   outSlope = Slope("dem", "DEGREE", 0.3043)  # Slope Tool
   outSlope.save("C:/Washtenaw/county/outslope01")



2. Run this script using Idle in Python 2.7 on a machine that has ArcMap, or from Jupyter Notebook in ArcGIS Pro.

.. code-block:: python

   # Import system modules
   import arcpy
   from arcpy import env
   from arcpy.sa import *

   # Set environment settings
   env.workspace = "C:/Washtenaw"

   # Set local variables
   inRaster = "C:/Washtenaw/county/washtenaw/topography/dem"
   outMeasurement = "DEGREE"
   zFactor = 0.3043

   # Check out the ArcGIS Spatial Analyst extension license
   arcpy.CheckOutExtension("Spatial")

   # Execute Slope
   outSlope = Slope(inRaster, outMeasurement, zFactor) # Slope Tool

   # Save the output
   outSlope.save("C:/Washtenaw/county/outslope02")

 
 |


**Generate Slope using the RichDem Library**


First, install the RichDEM library. run the sample script below.

.. code-block:: python

   from osgeo import gdal
   import matplotlib.pyplot as plt
   import numpy as np
   import os
   import matplotlib
   import elevation
   import richdem as rd


   #Open raster and read number of rows, columns, bands
   dataset = gdal.Open("C:/Users/Hugh/Desktop/N47E010.hgt")
   cols = dataset.RasterXSize
   rows = dataset.RasterYSize
   allBands = dataset.RasterCount
   band = dataset.GetRasterBand(1)

   elev = band.ReadAsArray(0,0,cols,rows).astype(np.int)

   slope = rd.TerrainAttribute(elev, attrib='slope_riserun')
   rd.rdShow(slope, axes=False, cmap='magma', figsize=(8, 5.5))
   plt.show()


   plt.figure(figsize = (10,10))
   ax = plt.imshow(elev)

   # Make a legend
   cbar = plt.colorbar(ax, fraction=0.046, pad=0.04)
   plt.show()


|


**Generate Slope using the Rasterio Library**


.. code-block:: python

	from osgeo import gdal
	import numpy as np
	import rasterio
	import matplotlib.pyplot as plt

	def calculate_slope(DEM):
	      gdal.DEMProcessing('slope.tif', DEM, 'slope')
	     with rasterio.open('slope.tif') as dataset:
	          slope = dataset.read(1)
	          return slope


	slope=calculate_slope("/Users/student/Desktop/TestDEM.tif")

	plt.imshow(slope, cmap='copper')
	plt.show()



|



Aspect Mapping
-----------------


**Calculate Aspect with Arcpy**

The script below show how to generate an aspect map using ArcPy.   


1. Calculate Aspect

.. code-block:: python

   # Import system modules
   import arcpy
   from arcpy import env
   from arcpy.sa import *

   # Set environment settings
   env.workspace = "C:/sapyexamples/data"

   # Set local variables
   inRaster = "elevation"

   # Execute Aspect
   outAspect = Aspect(inRaster)  # Aspect tool

   # Save the output
   outAspect.save("C:/sapyexamples/output/outaspect02")


|



**Generate Aspect Maps susing the RichDem Library**



.. code-block:: python

	from osgeo import gdal
	import numpy as np
	import rasterio
	import matplotlib.pyplot as plt


	def calculate_aspect(DEM):
	       gdal.DEMProcessing('aspect.tif', DEM, 'aspect')
	              with rasterio.open('aspect.tif') as dataset:
	              aspect = dataset.read(1)
	              return aspect

	aspect=calculate_aspect("/Users/student/Desktop/TestDEM.tif")

	plt.imshow(slope, cmap='copper')
	plt.show()




For more information, please see this website - https://richdem.readthedocs.io/en/latest/terrain_attributes.html


|




Curvature Maps 
------------------


**Generate Curvature Maps using Arcpy**

The two scripts below show how to calculate curvature using ArcPy.  


1. Curvature Example 1. Use in ArcGIS Python Window

.. code-block:: python

	from arcpy.ia import *
	out_curvature_raster = Curvature("curvature_input.tif", "profile", 2)
	out_curvature_raster.save("C:/arcpyExamples/outputs/curv_profile.tif")



|

 2. Curvature Example 2

This example calculates the curvature of a given slope. Use in Idle or Python Notebook


.. code-block:: python

	# Import system modules
	import arcpy
	from arcpy.ia import *

	# Set the analysis environments
	arcpy.env.workspace = "C:/arcpyExamples/data"

	# Set the local variables
	in_raster = "curvature_input.tif"

	# Execute Curvature function
	out_curvature_raster = Curvature(in_raster, "planform", 3)

	# Save the output
	out_curvature_raster.save("C:/arcpyExamples/outputs/cur_planform.tif")



Click on this link for more code samples - https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst




|




**Integrating Multiple Tools into a Single Script to Automate Workflows**



a. Calculate Slope and Aspect Using a Single Script

.. code-block:: python

   #Import system modules
   import arcpy
   from arcpy import env
   from arcpy.sa import *

   try:
	   # Set environment settings
	   env.workspace = "C:/workspace"
	   # Set local variables
	   inRaster = "dem"
	   outMeasurement = "DEGREE" 
	   zFactor = 0.3043

	   # Check out the ArcGIS Spatial Analyst extension license
	   arcpy.CheckOutExtension("Spatial")

	   # Execute Slope
	   outSlope = Slope(inRaster, outMeasurement, zFactor)
	    
	   # Save the output
	   outSlope.save("C:/workspace/outslope02")
	   print "Slope successfully calculated"      
	     
	   # Execute Aspect
	   outAspect = Aspect(inRaster)
	   outAspect.save("C:/workspace/outaspect02")
	
	except Exception as e:
	    print (e.message)



|


Watershed Delineation
----------------------


*Watershed Delineation with pysheds**

I came across a library called pysheds that can be used for watershed delineation. You can learn more about the library at this site. Simple and fast watershed delineation in python.


.. code-block:: python


	from pysheds.grid import Grid

	grid = Grid.from_raster('/Users/hsemple/Desktop/elevation.tiff')
	dem = grid.read_raster('/Users/hsemple/Desktop/elevation.tiff')


	# Fill Sinks
	# ----------------------
	# Fill pits in DEM
	pit_filled_dem = grid.fill_pits(dem)

	# Fill depressions in DEM
	flooded_dem = grid.fill_depressions(pit_filled_dem)
	    
	# Resolve flats in DEM
	inflated_dem = grid.resolve_flats(flooded_dem)


	# Determine D8 flow directions from DEM
	# ----------------------
	# Specify directional mapping
	dirmap = (64, 128, 1, 2, 4, 8, 16, 32)
	    
	# Compute flow directions
	# -------------------------------------
	fdir = grid.flowdir(inflated_dem, dirmap=dirmap)


	# Calculate flow accumulation
	# --------------------------
	acc = grid.accumulation(fdir, dirmap=dirmap)


	# Delineate a catchment
	# ---------------------
	# Specify pour point
	x, y = -97.294, 32.737

	# Snap pour point to high accumulation cell
	x_snap, y_snap = grid.snap_to_mask(acc > 1000, (x, y))

	# Delineate the catchment
	catch = grid.catchment(x=x_snap, y=y_snap, fdir=fdir, dirmap=dirmap, 
	                       xytype='coordinate')

	# Crop and plot the catchment
	# ---------------------------
	# Clip the bounding box to the catchment
	grid.clip_to(catch)
	clipped_catch = grid.view(catch)


	# Extract river network
	# ---------------------
	branches = grid.extract_river_network(fdir, acc > 50, dirmap=dirmap)


	# Calculate distance to outlet from each cell
	# -------------------------------------------
	dist = grid.distance_to_outlet(x=x_snap, y=y_snap, fdir=fdir, dirmap=dirmap,
	                               xytype='coordinate')

	

	http://mattbartos.com/pysheds/





http://mattbartos.com/pysheds/




|


Resources
-----------

Building your own color map

.. code-block:: python

     from matplotlib.colors import LinearSegmentedColormap
     italy_colormap = LinearSegmentedColormap.from_list('italy', ['#008C45', '#0b914c', '#F4F5F0', '#cf2a32', '#CD212A'], N=value_range)

     