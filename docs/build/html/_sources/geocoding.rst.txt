

Geocoding
============

|


**Geocoding a Single Address Using World Geocoding Services**


.. code-block:: python

	import arcpy

	# Sign in to ArcGIS Online
	username = "your_username"
	password = "your_pwd"
	arcpy.SignInToPortal("https://www.arcgis.com/", username, password)

	# Create a new Locator object from the ArcGIS World Geocoding Service
	locator_path = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service"
	locator = arcpy.geocoding.Locator(locator_path)
	        
	# Geocode to find the location of an address
	geocoding_candidates = locator.geocode("1670 W Peachtree St NE, Atlanta, GA 30309", False)
	geocoding_candidates


|



**Batch Geocoding Using the World Geocoding Services**


.. code-block:: python

	import arcpy
	arcpy.SignInToPortal("https://www.arcgis.com/", username='your_username', password='your_pwd')
	arcpy.env.workspace = "C:/Users/Hugh/Desktop/geocoding"

	# Set local variables
	address_table = r"C:/Users/Hugh/Desktop/geocoding/Anchorage_addresses.csv"

	# Using the World Geocoding Service for geocoding
	address_locator = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/ArcGIS World Geocoding Service"

	field_map = ("\'Address or Place\' Address VISIBLE NONE;Address2 <None> VISIBLE NONE;Address3 <None> VISIBLE NONE;" +
	             "Neighborhood <None> VISIBLE NONE;City City VISIBLE NONE;Subregion <None> VISIBLE NONE;" +
	             "Region <None> VISIBLE NONE;ZIP ZIP <None> VISIBLE NONE;ZIP4 <None> VISIBLE NONE;" +
	             "Country Country VISIBLE NONE")

	geocode_result = geocode_result.shp"

	arcpy.GeocodeAddresses_geocoding(address_table, address_locator,
	                                 address_fields, geocode_result,
	                                 'STATIC')




|

**Create a Locator object from a locator item on your own ArcGIS Enterprise Portal**

.. code-block:: python

	import arcpy

	# Sign in to your portal
	username = "MyPortalUsername"
	password = "MyPortalPassword"
	arcpy.SignInToPortal("https://myenterpriseportal.esri.com/portal",username,password)

	# Create a new Locator object from the locator on your portal
	locator_path = "https://myenterpriseportal.esri.com/server/rest/services/Geocode/Atlanta/GeocodeServer/Atlanta"
	locator = arcpy.geocoding.Locator(locator_path)


|



**Geocoding with Geopandas**

.. code-block:: python

    import pandas as pd 
    import geopandas as gpd 
    from shapely.geometry import Point

    # Filepath 
    fp = "data/Helsinki/addresses.txt"

    # Read the data 
    data = pd.read_csv(fp, sep=”;”)

    len(data) data.head()

    # Import the geocoding tool 
    from geopandas.tools import geocode

    # Geocode addresses using Nominatim. # You can provide your own 
    geo = geocode(
    data[“addr”], provider=”nominatim”, user_agent=”pythongis_book”, timeout=10)

    geo.head()

    join = geo.join(data)

    join.head()

    # Output file path outfp = “data/Helsinki/addresses.shp”

    # Save to Shapefile join.to_file(outfp)



https://pythongis.org/part2/chapter-06/nb/05-geocoding.html


|





**Geocoding with ArcGIS API for Python**


.. code-block:: python

	from arcgis.gis import GIS
	from arcgis.geocoding import geocode

	gis = GIS()

	geocoded_features = geocode(
	    address=None,
	    location=[-118.71511, 34.09042],
	    category="Coffee shop",
	    out_fields="Place_addr, PlaceName",
	    max_locations=25,
	    as_featureset=True,
	)

	geocoded_df = geocoded_features.sdf
	geocoded_df.head(2)

	m = gis.map()
	m

	m.center = [34.09042, -118.71511]
	m.zoom = 11
	m.draw(geocoded_features)





