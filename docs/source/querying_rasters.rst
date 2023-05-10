
Querying Rasters
=================


Below are sample scripts that can be used to query rasters

\

1. Querying Rasters Using an ArcPy Map Algebra Expression

# Find all values in an elevation raster that greater than 800 (meters).


.. code-block:: python

	import arcpy
	from arcpy.sa import *
	arcpy.env.overwriteOutput = True

	# Specify the input raster
	inRaster = "C:/workspace/dem"

	# Check out the Spatial Analyst extension
	arcpy.CheckOutExtension("Spatial")

	# Make a map algebra expression and save the resulting raster
	outRaster = Raster(inRaster) > 800
	outRaster.save("C:/workspace/query800c")

	# Check in the Spatial Analyst extension now that you're done
	arcpy.CheckInExtension("Spatial")
	print "Query successfully executed.

|




2. Querying a Raster using Arcpy with the "Con" Keyword

‘Con’ is abbreviation for condition and allows for the execution of conditional statements.  The basic syntax when using "Con" is:

Con(in_conditonal_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause}).

 

Example (a)


.. code-block:: python

	import arcpy
	from arcpy import env
	from arcpy.sa import *

	env.overwriteOutput = True

	# Check out ArcGIS Spatial Analyst extension
	arcpy.CheckOutExtension("Spatial")

	env.workspace = "C:/workspace"

	outElev1 = Con(dem > 700, 1, 0)
	outElev1.save("C:/workspace/outElev1")

	#or

	# Execute Con using a map algebra expression instead of a where clause
	outCon2 = Con(Raster("dem") > 700, "dem")

	outCon2.save("C:/workspace/outCon2")


|

Example (b)

.. code-block:: python

	import arcpy
	from arcpy import env
	from arcpy.sa import *

	env.overwriteOutput = True

	# Check out ArcGIS Spatial Analyst extension
	arcpy.CheckOutExtension("Spatial")

	env.workspace = "C:/workspace"

	outCon = Con("dem", "dem", "", "VALUE > 700")
	outCon.save("C:/workspace/outcon.img")


|



3.  Using the Con tool with 2 different Rasters


.. code-block:: python


	import arcpy
	from arcpy import env
	from arcpy.sa import *

	env.overwriteOutput = True
	env.workspace = "c:/workspace"

	# Check out ArcGIS Spatial Analyst extension
	arcpy.CheckOutExtension("Spatial")

	inSlope = Slope("dem", "DEGREE", 0.3043)
	inSlope.save("C:/workspace/inslope01")

	# Execute Aspect
	inAspect = Aspect("dem")

	# Save the output
	inAspect.save("C:/workspace/inaspect02")


	outCon = Con(((inSlope >= 0) & (inSlope <= 10)) & ((inAspect >= 110) & (inAspect <= 160)), 1, "")

	outCon.save("C:/workspace/con56")

	print ("Query Executed Successfully")

|



4.  Querying a Raster Using ExtractByAttributes


.. code-block:: python

	import arcpy
	from arcpy import env
	from arcpy.sa import *

	env.overwriteOutput = True
	env.workspace = "c:/workspace"

	# Check out ArcGIS Spatial Analyst extension
	arcpy.CheckOutExtension("Spatial")


	attExtract = ExtractByAttributes("inslope01", "VALUE > 2 & VALUE < 10")
	attExtract.save("C:/workspace/extract01")

	print "Query Executed Successfully"

|




5. Querying Rasters with Non- ESRI Libraries



#a. Find all places with elevation greater than 2500 ft  (Method 1)



.. code-block:: python

	import gdal
	import matplotlib.pyplot as plt

	#Open raster and read number of rows, columns, bands
	dataset = gdal.Open("C:/Users/Hugh/Desktop/N47E010.hgt")
	band = dataset.GetRasterBand(1)

	elevation = band.ReadAsArray(0,0,cols,rows)

	a2500 = elevation > 2500

	plt.imshow(a2500)
	plt.show()

|



#b. Find all places with elevation greater than 2500 ft  (Method 2)


.. code-block:: python

	import gdal
	import matplotlib.pyplot as plt

	#Open raster and read number of rows, columns, bands
	dataset = gdal.Open("C:/Users/Hugh/Desktop/N47E010.hgt")
	band = dataset.GetRasterBand(1)

	cols = dataset.RasterXSize
	rows = dataset.RasterYSize

	elevation = band.ReadAsArray(0,0,cols,rows)

	outData = np.zeros((rows, cols))

	for y in range(rows):
	     for x in range(cols):
	          if elevation[y, x] > 2500:
	              outData[y, x] = 1
	          else:
	              outData[y, x] = 0

	plt.imshow(outData)
	plt.show()







Map Algebra
--------------

Map algebra involves performing mathematical operations on rasters, as shown in the example below.  In ArcGIS, such operations can be performed manually using the Raster Calculator.  Map algebra allows us to plug rasters into equations to perform modeling in a GIS environment.

|


**1. Simple Map Algebra Operations**


.. code-block:: python

	import arcpy
	from arcpy import env 
	from arcpy.sa import * 
	try:
	# Set environment settings
	env.workspace = "C:/workspace"
	env.overwriteOutput = True

	# Check out ArcGIS Spatial Analyst extension 
	arcpy.CheckOutExtension("Spatial")

	outRas2 = Raster("dem") * 8
	outRas3 = outRas2 + Raster("dem") * 10
	print "Calculation successfully completed"


	except Exception as e:
	     print e.message

|



**2. Implementing Algebraic Equations**

The equation below calculates topographic wetness index for an area.  You can read about it here - You can read about the index here - http://soilandwater.bee.cornell.edu/tools/TI.pdf.

Links to an external site. The script below shows how to deal with equations.  In ArcPy,  slope maps in degrees must be converted to radians.

Topographic Wetness Index


.. code-block:: python

	import arcpy
	from arcpy import env
	from arcpy.sa import *
	import math


	# Set environment settings
	env.workspace = "C:\workspace"
	env.overwriteOutput = True

	# Set local variables
	inRaster = "slope1"
	flowaccum1 = "flowaccum"

	# Check out the ArcGIS Spatial Analyst extension license
	arcpy.CheckOutExtension("Spatial")

	# Execute Ln converting. All degrees are converted to degrees to radians
	outLn = Ln(((Raster(flowaccum1) + 1)*10) / Tan((Raster(inRaster) * (math.pi / 180.0))))

	# Save the output 
	outLn.save("C:\workspace\outln6")

	print "Computation executed successfully"

 

|



**3. Calculating NDVI with GDAL**


.. code-block:: python

	from osgeo import gdal
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.colors as colors


	band4 = gdal.Open("/Users/semple/Desktop/LT05/LT05_L1TP_047027_20101006_20200823_02_T1_B4.TIF")
	band3 = gdal.Open("/Users/semple/Desktop/LT05/LT05_L1TP_047027_20101006_20200823_02_T1_B3.TIF")


	b3 = band3.GetRasterBand(1)
	b4 = band4.GetRasterBand(1)


	fig, ax = plt.subplots(figsize= (8,8))

	b3_arr = b3.ReadAsArray().astype(np.float32)
	b4_arr = b4.ReadAsArray().astype(np.float32)

	#Allow division by zero
	np.seterr(divide='ignore', invalid='ignore')

	ndvi = (b4_arr - b3_arr) / (b4_arr + b3_arr)

	plt.imshow(ndvi)
	plt.colorbar(shrink=0.50) 

	plt.show()

	ndvi.png  
	numply.seterror(). - https://numpy.org/doc/stable/reference/generated/numpy.seterr.html



|
 

**4. Calculating NDVI with Rasterio**


.. code-block:: python

	import numpy as np
	import rasterio
	from rasterio.plot import show

	blueband  = rasterio.open("C:/Users/Hugh/Desktop/Landsat/Landsat/LT05_L1TP_019031_20111106_20160830_01_T1_B4.TIF")
	greenband = rasterio.open("C:/Users/Hugh/Desktop/Landsat/Landsat/LT05_L1TP_019031_20111106_20160830_01_T1_B3.TIF")
	mirband    = rasterio.open("C:/Users/Hugh/Desktop/Landsat/Landsat/LT05_L1TP_019031_20111106_20160830_01_T1_B2.TIF")

	green = greenband.read(1).astype(float)
	mir = mirband.read(1).astype(float)

	np.seterr(divide='ignore', invalid='ignore')  # Allow division by zero

	mndwi = np.empty(greenband.shape, dtype=rasterio.float32)  # Create empty matrix

	check = np.logical_or(mir > 0.0, green > 0.0)  # Create check raster with True/False values

	mndwi = np.where(check, (green - mir) / (green + mir), -999)  # Calculate MNDWI

	water = np.where(mndwi > 0, 1, 0) # Set values above 0 as water and otherwise leave it at 0

	show(water, cmap='plasma')


 

 

**Readings**

https://colekrehbiel.wordpress.com/2017/10/18/calculate-ndvi-from-sentinel-2a-data/

https://github.com/ckrehbiel/website/blob/master/Sentinel_NDVI.py

https://stackoverflow.com/questions/16411468/calculate-ndvi-using-python

 

 