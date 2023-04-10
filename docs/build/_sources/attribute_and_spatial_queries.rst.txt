
Attribute and Spatial Queries
================================

|

Retrieving records using ArcPy
--------------------------------



|



Retrieving records using Geopandas
-------------------------------------


.. code-block:: python
    
   import geopandas
   import maplotlib
   district_gdf = geopandas.read_file("/Users/.../school_district.shp", encoding='utf-8')

   # view the attribute information
   district_gdf.head()

   # view the geometry
   district_gdf.plot()


   district_gdf.query("DISTRICT=='Ypsilanti'")

   #Optionally save the output
   district_gdf.to_file(‘filename)



   |


Pyshp 
--------

.. code-block:: python

   import shapefile
   edit_file = shapefile.Editor('/Users/.../school_districts.shp')
   i=0


   #Set i as 0 and iterate over the records for the column in which you want to search by passing the index and check with equal operator
	
   for rec in edit_file.records:
	  if edit_file.records[i][0] == 'Almora':
	    print(rec)
	  i= i+1


|


References
-------------

https://www.geosnips.com/tutorials/python-vector-buffer/

