
Batch Processing & Workflow Automation
========================================


Batch processing is the process of automating repetitive tasks as a block of work rather than attempting to process each operation manually. In GIS, it may be that you have to clip 1000 shapefiles to the extent of some regions. Instead of clipping the shapefiles individually, one can perform batch clipping in which we use a script to complete the task. Batch proessing is far faster than human processing.  It is often done in off-peak hours when computing resources are more commonly available, such as at the end of the day or overnight. 

In GIS, many large volume geoprocessing operations are carried out by batch scripting the operation.  The scripts below provide an introduction to batch operations using various Python libraries.

With the appearance of ChatGPT, it now very easy to develop workflow scripts.  Simply describe the workflow in an much detail as you can and enter it into ChatGPT. ChatGPT will return a sample script that most often will work, but often also after a small amount of modification and testing.




|



Batch Processing Using GDAL  
-----------------------------


There are many code samples for processing a single file.  However, code samples for batch processing are not frequently encountered.  Below is an example for converting multiple .hdr files into .tif files using GDAL.
 

In GDAL, if you wanted to change the file format of a single raster, you can write a script similar to the one below:  


>>> gdal_translate -of GTiff elevation.hdr elevation.tif


Now, if we have 500 rasters in a folder that we would like to change the file format from .rst to tif, we could write a script to loop over all the files in folder and convert them to the desired format. 

To write the script, open a text editor, e.g. Notepad, and add the following code:


.. code-block:: python

	for %%f in (*.hdr) do (
	   echo %%~nf
	   gdal_translate -of GTiff %%f %%~nf.tif
	)


Save the batchfile as rst2tif.bat in the folder with the land-use rasters.

In the above code,  %%f is the variable that contains the filename of each file. The echo statement is used print something to the screen. Here we print %%~nf, which is the part of the filename before the dot that separates it from the extension. Next, we use the gdal_translate command with output format GeoTiff. At the end of the line we add the .tif extension to the filename.


To execute the batchfile, type
rst2tif <ENTER>


Check the results.

Note: Bat files are designed to for Windows machines. On MacOs, the files are called shell scripts and have a .sh ending.


Source:  https://courses.gisopencourseware.org/mod/book/view.php?id=78&chapterid=193


|


**Convert a JPG to a PNG**

.. code-block:: python

	import os, sys
	from PIL import Image

	# Make sure original image ('test.png') is in root directory
	images = ['test.png']

	for infile in images:
	  f, e = os.path.splitext(infile)
	  outfile = f + '.jpg'
	  if infile != outfile:

	      try:

	          with Image.open(infile) as image:
	              in_rgb = image.convert('RGB')
	              in_rgb.save(outfile, 'JPEG')

	        except OSError:
	              print('Conversion failed for', infile)




|



**Batch Processing Using Arcpy**
-------------------------------------



**Buffering Multiple Shapefiles using Arcpy**

The script below can buffer any number of rasters.



.. code-block:: python

	import arcpy

	# Set geoprocessing environments 
	arcpy.env.workspace = r"C:/ata/buffers"
	arcpy.env.overwriteOutput = True

	# Create list of feature classes
	fcList = arcpy.ListFeatureClasses()

	# Create a loop to buffer feature classes
	bufferList = []
	for fc in fcList:
	      if fc == "Lakes" or fc == "Streams":
	          arcpy.Buffer_analysis(fc, fc + "Buffers", "1000 meters", "", "", "ALL")
	bufferList.append(fc + "Buffer")

	 

|



**Batch Clipping Shapefiles**


Clipping shapefiles is a popular GIS geoprocessing operation. With Python, you can clip a single file or hundreds of files using a single script.   

You can also clip a single base map into multiple shapefile. The script below is used to clip a Michigan-wide geology basemap layer into 83 county-wide layers.
 

.. code-block:: python

	import arcpy
	arcpy.env.workspace = r'c:/data/geology'

	#Create a search cursor on the clipping extent shapefile
	cursor = arcpy.SearchCursor('county_miv17a.shp')

	for row in cursor:
	    feat = row.Shape
	    arcpy.Clip_analysis('bedrock_geology.shp', feat,  str(row.getValue('NAME')), '')



|


**Batch Defining Projections**

In GIS work, we often encouter shapefiles for which the projection has not been defined. If you have multiple shapefiles that needs to have their projections defined to a common projection, then you can use a script to perform the task. The example arcpy script below can be used to batch define the projection of multiple map layers.


.. code-block:: python

	# import system modules
	import arcpy
	from arcpy import env
	import os

	# Set workspace environment where the shapefiles are located 
	arcpy.env.workspace = "C:/data/projection"


	# Create a list of feature classes or shapefiles in the current workspace
	fcs = arcpy.ListFeatureClasses('*')

	#Get the spatial reference information
	dsc = arcpy.Describe("2022_streets.shp")
	coord_sys = dsc.spatialReference


	# set local variables
	try:
	      for file in fcs:
	          inData = file
	          coord_sys = dsc.spatialReference
	          arcpy.DefineProjection_management(inData, coord_sys)
	          print (file, ",", coord_sys.name)


	except arcpy.ExecuteError:
	      print (arcpy.GetMessages(2))

	except Exception as e:
	      print (e.args[0])
	      arcpy.AddError(e.args[0])


|




**Batch Reprojecting Shapefiles**


This example script can be used in ArcMap or ArcGIS Pro to reproject multiple map layers:

.. code-block:: python


	# Name: BatchProject.py
	# Description: Changes coordinate systems of several datasets in a batch.

	import arcpy 

	# Set workspace environment
	arcpy.env.workspace = "C:/.data/BedRock_Michigan"
	arcpy.env.overwriteOutput = True

	# Input feature classes
	input_features = arcpy.ListFeatureClasses('*')

	# Output workspace

	out_workspace = "C:/data/BedRock_Michigan/Reproj_Output"

	# Output coordinate system - leave empty
	out_cs = ''

	# Template dataset -  GCS_WGS_1984 coordinate system
	template = "C:/.../Michigan_Projected.shp"

	# Geographic transformation - 
	transformation = "WGS_1984_(ITRF00)_To_NAD_1983"
	res = arcpy.BatchProject_management(input_features, out_workspace, out_cs, template, transformation)

	print "Batch Reprojection successfully completed"



|



**Batch Clipping Rasters**


.. code-block:: python

	import arcpy
	from arcpy.sa import *
	arcpy.CheckOutExtension("spatial")
	arcpy.env.overwriteOutput = True

	arcpy.env.workspace = "C:/data/Bedrock_Geology"
	clipshapefile = "counties_v17a.shp"

	rasterfile = "Michigan_DEM.tif"

	#Create a cursorcursor = arcpy.SearchCursor('Counties_v17a.shp')
	cursor = arcpy.SearchCursor('Counties_v17a.shp')

	for row in cursor:
	county = arcpy.gp.ExtractByMask_sa(rasterfile, clipshapefile, str(row.getValue('NAME')))
	print str(row.getValue('NAME')), "completed"



|



**Batch Mosaicing Rasters**


.. code-block:: python

	from arcpy import (CheckOutExtension, da)
	from arcpy.management import MosaicToNewRaster
	from os import path
	workspace = r"C:/Users/Hugh/Desktop/merged/topo"

	arcpy.env.workspace = workspace
	arcpy.env.overwriteOutput = True
	#sr = arcpy.SpatialReference(3174) # assuming this is your spatial reference 

	rasters = [] 

	for dirpath, dirnames, filenames in da.Walk(workspace, topdown=True, datatype="RasterDataset"):
	   for filename in filenames: 
	      rasters.append(filename)

	MosaicToNewRaster(rasters, "C:/Users/Hugh/Desktop/merged/topo", newraster.tif", "#", "16_BIT_UNSIGNED", "30", "1")



|



**Batch Generation of Slope Rasters**


.. code-block:: python

	import arcpy

	from arcpy.sa import *
	arcpy.env.workspace = 'C:/data/DEMs'
	arcpy.env.overwriteOutput = True
	rasterlist = arcpy.ListRasters() # Get a list of input rasters

	for raster in rasterlist:
	     arcpy.Slope_3d(raster, "outslope", "DEGREE", 0.3043)
	     print (raster)



|
|



Automating GIS Workflows
--------------------------

Whereas batch processing involves repeating tasks many times, automating workflows involves writng codes to carry out tasks that involves multiple tools and multiple steps. Typically, the output of one step becomes the input for the next step.  The code samples below illustrates workflow automation for basic GIS tasks such as watershed delineation, site stelection analysis, geocoding, and thematic mapping. Workflow automation is required in a wide range of scenarios by organizations and GIS developers are deeply involved in these tasks.




**Watershed Delineation (Arcpy)**


.. code-block:: python

	# Import system modules
	import arcpy
	from arcpy import env 
	from arcpy.sa import * 
	try:
	    # Set environment settings
	    env.workspace = "C:/Users/Hugh/Desktop/watershed"
	    env.overwriteOutput = True

	    # Check out ArcGIS Spatial Analyst extension 
	    arcpy.CheckOutExtension("Spatial")

	    # Fill sink
	    outFill = Fill("elevation")
	    outFill.save("fill01")


	    #Flow Direction
	    outFlowDirection = FlowDirection("fill01", "NORMAL")
	    outFlowDirection.save("flowdir")

	    # Flow Accumulation
	    outFlowAccumulation = FlowAccumulation("flowdir")
	    outFlowAccumulation.save("flowAccum")

	    # Define stream length
	    streams = Con(Raster("flowAccum") > 1500, 1)
	    streams.save("streams")

	    # Stream Link
	    outStreamLink = StreamLink("streams", "flowdir")
	    outStreamLink.save("outStreamLink")

	    # Stream to Feature
	    outStreamFeat = StreamToFeature("streams", "flowdir", "outstrm01.shp", "NO_SIMPLIFY")


	    #Delineate Watershed
	    PourPoint = "PourPoint.shp"
	    outWatershed = Watershed("flowdir", PourPoint, "Id")
	    outWatershed.save("watershed")#Delineate Watershed


	    print ("Watershed successfully delineated")
	except Exception as e:
	    print (e)



|








**Geocoding Events and and Finding Standard Distance Circle**


.. code-block:: python

    import arcpy

	# Set the project and map
	aprx = arcpy.mp.ArcGISProject("CURRENT")
	mapx = aprx.listMaps()[0]

	# Set the input table and output feature class names
	input_table = r"C:\data\project.gdb\event_table"
	output_fc = r"C:\data\project.gdb\geocoded_points"

	# Geocode the input table using the ArcGIS World Geocoding Service
	arcpy.geocoding.GeocodeAddresses(input_table, "World", output_fc)

	# Add the feature layer to the map
	lyr = mapx.addDataFromPath(output_fc)

	# Set the symbology for the layer
	sym = arcpy.mp.LayerFile("path/to/symbology.lyrx")
	lyr.symbology = sym.symbology

	# Calculate the mean center and standard distance circle of the geocoded points
	mean_center = arcpy.stats.MeanCenter(output_fc, "mean_center")
	std_distance = arcpy.stats.StandardDistance(output_fc, "std_distance")

	# Print the mean center and standard distance circle locations
	print("Mean Center location: ({0}, {1})".format(mean_center.centroid.X, mean_center.centroid.Y))
	print("Standard Distance Circle location: ({0}, {1})".format(std_distance.centroid.X, std_distance.centroid.Y))

	# Add the mean center and standard distance circle to the map
	mean_center_lyr = mapx.addDataFromPath(mean_center)
	std_distance_lyr = mapx.addDataFromPath(std_distance)

	# Save the project
	aprx.save()




|




**Calculate Slope and Aspect Using a Single Script**

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


**Automating Thematic Mapping**

Here's a Python workflow that takes a CSV file containing total counts of COVID-19 cases for each county, plots these on a shapefile of counties using Geopandas and create a graduated color map with five classes and natural breaks classification:

.. code-block:: python

	import geopandas as gpd
	import pandas as pd
	import matplotlib.pyplot as plt
	import pysal as ps

	# Read in the county shapefile
	county_shapefile = gpd.read_file('path/to/county/shapefile.shp')

	# Read in the CSV file containing the COVID-19 case counts
	covid_data = pd.read_csv('path/to/covid/data.csv')

	# Merge the county shapefile and the COVID-19 case data
	merged_data = county_shapefile.merge(covid_data, left_on='FIPS', right_on='FIPS')

	# Calculate the natural breaks for the case counts
	classifier = ps.Natural_Breaks.make(k=5)
	breaks = classifier(merged_data['cases'], initial=0)

	# Create a colormap with five classes
	cmap = plt.cm.get_cmap('YlOrRd', 5)

	# Plot the data on a map with graduated colors
	fig, ax = plt.subplots(figsize=(12, 8))
	merged_data.plot(column='cases', ax=ax, cmap=cmap, edgecolor='grey', linewidth=0.5, legend=True)

	# Add a title to the map
	ax.set_title('COVID-19 Cases by County')

	# Add a legend to the map
	legend = ax.get_legend()
	legend.set_bbox_to_anchor((0.18, 0.95))

	# Save the map to a file
	plt.savefig('path/to/output/map.png', dpi=300)


|




**Automating Selection Analysis**

To find the best site to locate a warehouse in a city, we can define the basic locational requirements, then submit a query to ChatGPT. In the example below, the locational requirements are:


"Using Python, find the best site to locate a ware house given the following criteria: warehouse must be 100 meters from railway lines, 100 meters from highways, not more than 1000 meters from a seaport, and located in light industrial areas. Generate a map of the results using matplotlib."

I generated sample code from ChatGPT using geopandas and arcpy.


*Geopandas*

.. code-block:: python

	import geopandas as gpd
	import matplotlib.pyplot as plt

	# Load the data layers
	railways = gpd.read_file('path/to/railways.shp')
	highways = gpd.read_file('path/to/highways.shp')
	industrial_areas = gpd.read_file('path/to/industrial_areas.shp')

	# Define a buffer of 100 meters around the railways and highways
	railway_buffer = railways.buffer(100)
	highway_buffer = highways.buffer(100)

	# Intersect the buffers around the railways and highways to get the final buffer area
	buffer_area = railway_buffer.intersection(highway_buffer)

	# Subtract the buffer area from the industrial areas layer to get the final area that meets all criteria
	final_area = industrial_areas.difference(buffer_area)

	# Generate a map of the final area using matplotlib
	fig, ax = plt.subplots(figsize=(10, 10))

	# Plot the final area in green
	final_area.plot(ax=ax, color='green')

	# Plot the railways and highways buffers in gray
	railway_buffer.plot(ax=ax, color='gray')
	highway_buffer.plot(ax=ax, color='gray')

	# Add a legend and scale bar
	ax.set_title('Best Site for Warehouse in Boston, MA')
	ax.legend(['Final Area', 'Railway/Highway Buffer'])
	scalebar = ScaleBar(1, location='lower left')
	ax.add_artist(scalebar)

	plt.show()


|

*Arcpy*

.. code-block:: python

	import arcpy
	import matplotlib.pyplot as plt

	# Set workspace and input data paths
	arcpy.env.workspace = r"C:\GIS\data\Boston.gdb"
	railway_lines = "Railway_Lines"
	highways = "Highways"
	seaports = "Seaports"
	light_industrial_areas = "Light_Industrial_Areas"

	# Buffer railway lines and highways by 100 meters
	railway_buffer = arcpy.Buffer_analysis(railway_lines, "Railway_Buffer", "100 Meters")
	highway_buffer = arcpy.Buffer_analysis(highways, "Highway_Buffer", "100 Meters")

	# Create a 1000-meter buffer around seaports
	seaport_buffer = arcpy.Buffer_analysis(seaports, "Seaport_Buffer", "1000 Meters")

	# Overlay buffers to obtain areas that are at least 100 meters from all three features
	exclude_areas = arcpy.Intersect_analysis([railway_buffer, highway_buffer, seaport_buffer], "Exclude_Areas")

	# Overlay exclude areas with light industrial areas to obtain candidate locations
	candidate_areas = arcpy.Intersect_analysis([exclude_areas, light_industrial_areas], "Candidate_Areas")

	# Generate map of candidate locations using matplotlib
	fig, ax = plt.subplots()
	arcpy.management.ExportToPNG(candidate_areas, "candidate_areas.png")
	im = plt.imread("candidate_areas.png")
	ax.imshow(im, extent=[191500, 199000, 88200, 121700])
	ax.set_xlabel("Eastings")
	ax.set_ylabel("Northings")
	ax.set_title("Candidate Locations for Warehouse")
	plt.show()



|




**Geocoding Workflow**

Here's a Python workflow that prompts the user for an address, geocodes the address using OpenStreetMap, maps the resulting latitude and longitude using Folium, and sends the address to a PostgreSQL database.


In this workflow, we first prompt the user for an address and then geocode the address using OpenStreetMap. If the geocoding is successful, we extract the latitude and longitude from the geocoded data and create a map using Folium. We then add a marker to the map at the geocoded location and save it to an HTML file. Next, we connect to a PostgreSQL database, insert the address along with its latitude and longitude into the database, and commit the changes. Finally, we close the database connection. If the geocoding is unsuccessful, we notify the user to enter a valid address.



.. code-block:: python

	import psycopg2
	import requests
	import json
	import folium

	# Prompt the user for an address
	address = input("Enter an address: ")

	# Geocode the address using OpenStreetMap
	url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
	response = requests.get(url)
	data = json.loads(response.content)

	# Check if the geocoding was successful
	if data:
	    # Extract the latitude and longitude from the geocoded data
	    latitude = data[0]['lat']
	    longitude = data[0]['lon']

	    # Create a map using Folium
	    map = folium.Map(location=[latitude, longitude], zoom_start=15)

	    # Add a marker to the map at the geocoded location
	    folium.Marker([latitude, longitude]).add_to(map)

	    # Display the map
	    map.save('map.html')
	    print("Map saved to map.html")

	    # Connect to the PostgreSQL database
	    conn = psycopg2.connect(database="mydatabase", user="myusername", password="mypassword", host="localhost", port="5432")
	    cur = conn.cursor()

	    # Insert the address into the database
	    cur.execute("INSERT INTO addresses (address, latitude, longitude) VALUES (%s, %s, %s)", (address, latitude, longitude))
	    conn.commit()
	    print("Address inserted into database")

	    # Close the database connection
	    cur.close()
	    conn.close()

	else:
	    print("Geocoding failed. Please enter a valid address.")



|

.. code-block:: python

	from arcgis.gis import GIS
	from arcgis.features import FeatureLayer, FeatureSet
	from arcgis.geometry import buffer, distance
	import matplotlib.pyplot as plt

	# Connect to the GIS
	gis = GIS("https://www.arcgis.com", "username", "password")

	# Define the search criteria
	railway_distance = 100
	highway_distance = 100
	seaport_distance = 1000
	industrial_areas = "Light Industrial"

	# Load the relevant layers from the Boston dataset
	boston_map = gis.map("Boston, MA", zoomlevel=12)
	boston_railways = FeatureLayer("https://services.arcgis.com/HRPe58bUyBqyyiCt/arcgis/rest/services/MBTA_Rail_Lines/FeatureServer/0")
	boston_highways = FeatureLayer("https://services.arcgis.com/HRPe58bUyBqyyiCt/arcgis/rest/services/MassDOT_Highways/FeatureServer/0")
	boston_seaports = FeatureLayer("https://services.arcgis.com/HRPe58bUyBqyyiCt/arcgis/rest/services/Port_Authority_Facilities/FeatureServer/0")
	boston_industrial_areas = FeatureLayer("https://services.arcgis.com/HRPe58bUyBqyyiCt/arcgis/rest/services/Boston_Zoning/FeatureServer/0")

	# Buffer the railways and highways
	boston_railways_buffer = buffer(boston_railways.query(), railway_distance)
	boston_highways_buffer = buffer(boston_highways.query(), highway_distance)

	# Find the seaports within the specified distance
	boston_seaports_within_distance = boston_seaports.query().distance(seaport_distance, "meters")

	# Query the industrial areas
	boston_industrial_areas_query = boston_industrial_areas.query(where=f"Use = '{industrial_areas}'")

	# Use the geometry engine to find the suitable location for the warehouse
	suitable_locations = boston_industrial_areas_query.geometry.difference(boston_railways_buffer.union(boston_highways_buffer)).intersect(boston_seaports_within_distance.geometry)

	# Convert the suitable locations to a FeatureSet and add it to the map
	suitable_locations_feature_set = FeatureSet.from_features(suitable_locations)
	suitable_locations_layer = boston_map.add_layer(suitable_locations_feature_set, {"renderer": "SimpleRenderer"})

	# Save the map to an image file
	plt.savefig("warehouse_location.png")



|



**Geodatabase Administration**

 The code example below perform the following operations as the geodatabase administrator:

    * Identify connected users.
    * Send an email notification.
    * Prevent the geodatabase from accepting new connections.
    * Disconnect users.
    * Reconcile versions and post changes.
    * Compress the geodatabase.
    * Allow the geodatabase to begin accepting new connections.
    * Rebuild indexes and update statistics on system tables.



.. code-block:: python

	import arcpy, time, smtplib

	# Set the workspace 
	arcpy.env.workspace = 'C:\\Projects\\MyProject\\admin.sde'

	# Set a variable for the workspace
	adminConn = arcpy.env.workspace

	# Get a list of connected users.
	userList = arcpy.ListUsers(adminConn)

	# Get a list of user names of users currently connected and make email addresses
	emailList = [user.Name + "@yourcompany.com" for user in arcpy.ListUsers(adminConn)]

	# Take the email list and use it to send an email to connected users.
	SERVER = "mailserver.yourcompany.com"
	FROM = "SDE Admin <python@yourcompany.com>"
	TO = emailList
	SUBJECT = "Maintenance is about to be performed"
	MSG = "Auto generated Message.\n\rServer maintenance will be performed in 15 minutes. Please log off."

	# Prepare actual message
	MESSAGE = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (FROM, ", ".join(TO), SUBJECT, MSG)

	# Send the mail
	print("Sending email to connected users")
	server = smtplib.SMTP(SERVER)
	server.sendmail(FROM, TO, MESSAGE)
	server.quit()

	# Block new connections to the database.
	print("The database is no longer accepting connections")
	arcpy.AcceptConnections(adminConn, False)

	# Wait 15 minutes
	time.sleep(900)

	# Disconnect all users from the database.
	print("Disconnecting all users")
	arcpy.DisconnectUser(adminConn, "ALL")

	# Get a list of versions to pass into the ReconcileVersions tool.
	# Only reconcile versions that are children of Default
	print("Compiling a list of versions to reconcile")
	verList = arcpy.ListVersions(adminConn)
	versionList = [ver.name for ver in verList if ver.parentVersionName == 'sde.DEFAULT']

	# Execute the ReconcileVersions tool.
	print("Reconciling all versions")
	arcpy.ReconcileVersions_management(adminConn, "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "c:/temp/reconcilelog.txt")

	# Run the compress tool. 
	print("Running compress")
	arcpy.Compress_management(adminConn)

	# Allow the database to begin accepting connections again
	print("Allow users to connect to the database again")
	arcpy.AcceptConnections(adminConn, True)

	# Update statistics and indexes for the system tables
	# Note: to use the "SYSTEM" option the user must be an geodatabase or database administrator.
	# Rebuild indexes on the system tables
	print("Rebuilding indexes on the system tables")
	arcpy.RebuildIndexes_management(adminConn, "SYSTEM")

	# Update statistics on the system tables
	print("Updating statistics on the system tables")
	arcpy.AnalyzeDatasets_management(adminConn, "SYSTEM")

	print("Finished.")


See this link for explanation of this code - https://desktop.arcgis.com/en/arcmap/latest/manage-data/geodatabases/using-python-scripting-to-batch-reconcile-and-post-versions.htm#GUID-913CD4A9-F765-4253-87DC-C5665A4AF2CC




|

**Moving Data from Survey123 Data Tables to Postgresql Database**

Python script that lets a user log into Arcgis Enterprise and move data from a Survey123 data table to a Postgresql Database with daily updates.

.. code-block:: python

	import getpass
	import schedule
	import time
	from arcgis.gis import GIS
	from arcgis.features import FeatureLayerCollection
	import psycopg2

	# ArcGIS Enterprise credentials
	portal_url = "https://your_portal_url/arcgis"  # Replace with your ArcGIS Enterprise URL
	username = input("Enter your ArcGIS Enterprise username: ")
	password = getpass.getpass("Enter your ArcGIS Enterprise password: ")

	# Survey123 feature service details
	survey123_item_id = "1234567890abcdef"  # Replace with the Survey123 feature service item ID
	survey123_layer_id = 0  # Replace with the Survey123 feature layer ID

	# PostgreSQL database details
	database_host = "localhost"  # Replace with the PostgreSQL database host
	database_name = "your_database_name"  # Replace with the PostgreSQL database name
	database_user = "your_database_user"  # Replace with the PostgreSQL database username
	database_password = getpass.getpass("Enter your PostgreSQL database password: ")

	# Function to move data from Survey123 to PostgreSQL
	def move_data():
	    try:
	        # Connect to ArcGIS Enterprise
	        gis = GIS(portal_url, username, password)

	        # Get the Survey123 feature layer collection
	        survey123_item = gis.content.get(survey123_item_id)
	        survey123_flc = FeatureLayerCollection.fromitem(survey123_item)

	        # Query the Survey123 data
	        query_result = survey123_flc.layers[survey123_layer_id].query()

	        # Connect to the PostgreSQL database
	        conn = psycopg2.connect(
	            host=database_host,
	            database=database_name,
	            user=database_user,
	            password=database_password
	        )
	        cursor = conn.cursor()

	        # Iterate over the features and insert into the PostgreSQL database
	        for feature in query_result.features:
	            # Extract the required attributes from the feature
	            attribute1 = feature.attributes['attribute1']  # Replace with the attribute names in your Survey123 form
	            attribute2 = feature.attributes['attribute2']
	            # Add more attributes as needed

	            # Prepare the SQL insert statement
	            sql = "INSERT INTO your_table_name (attribute1, attribute2) VALUES (%s, %s);"  # Replace with your table name and attributes

	            # Execute the SQL insert statement
	            cursor.execute(sql, (attribute1, attribute2))  # Add more attribute values as needed

	        # Commit the changes and close the database connection
	        conn.commit()
	        cursor.close()
	        conn.close()

	        print("Data successfully moved to the PostgreSQL database.")

	    except Exception as e:
	        print("An error occurred:", str(e))

	# Schedule the data movement at a specific time each day
	schedule.every().day.at("08:00").do(move_data)  # Replace "08:00" with your desired time

	# Continuously run the scheduled tasks
	while True:
	    schedule.run_pending()
	    time.sleep(1)



|


**Other Workflow Examples**


* Locator rebuilder (Rebuild, Republish)
* Create Custom reports from Survey 123 results
* Replicate data to file geodatabases
* Rebuild address locators
* Rebuild tiles for cached map services
* Extract data and upload zipped geodatabase to FTP
* Update datasets from map services 
* Compress enterprise geodatabase


|




Reading
----------

* `The need for GIS automation <https://www.e-education.psu.edu/geog485/node/202>`_

* `Streamlining GIS with Automation <https://www.geospatialworld.net/prime/technology-and-innovation/streamlining-gis-with-automation/>`_

* `Automating ArcGIS Enterprise Workflows using ArcGIS API for Python <https://blog.somideolaoye.com/automating-arcgis-enterprise-workflows-using-arcgis-api-for-python>`_

* `Sample Python scripts <https://gis.wsu.edu/portal/portalhelp/en/portal/latest/administer/windows/sample-python-scripts.htm>`_

* `Automate a geoprocessing workflow with Python <https://learn.arcgis.com/en/projects/automate-a-geoprocessing-workflow-with-python/>`_

* `Automating GIS and remote sensing workflows with open python libraries <https://towardsdatascience.com/automating-gis-and-remote-sensing-workflows-with-open-python-libraries-e71dd6b049ee>`_

* `Geoprocessing Workflow <https://github.com/pmacMaps/ArcPy/blob/master/LogResults_CaptureErrors_Template.py>`_

* https://pnmcartodesign.wordpress.com/2017/05/12/automating-gis-workflows-with-python-scripts/

* GeoPython - AutoGIS - https://automating-gis-processes.github.io/2016/index.html

* Customizing QGIS with Python (Full Course Material) - https://courses.spatialthoughts.com/pyqgis-in-a-day.html

* GIS Python API documentation - https://qgis.org/pyqgis/master/

* PyQGIS Developer Cookbook - https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html

* Geocoding Workflows in Python - https://mediaspace.esri.com/media/t/1_rcrehowf

*  https://cdn.tnris.org/documents/potts-georodeo-20180514.pdf

*  https://desktop.arcgis.com/en/arcmap/latest/manage-data/geodatabases/using-python-scripting-to-batch-reconcile-and-post-versions.htm#GUID-913CD4A9-F765-4253-87DC-C5665A4AF2CC


* Scheduling Scripts - https://pnmcartodesign.com/assets/documents/automating-workflows-python-scripts-pa-gis-conference-2017.pdf







