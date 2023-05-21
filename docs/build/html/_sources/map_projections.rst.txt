
Map Projections
=================

|

Map Projection with Geopandas
------------------------------


|


.. code-block:: python
    
   import geopandas
   import maplotlib
   district_gdf = geopandas.read_file("/Users/.../school_district.shp", encoding='utf-8')

   # view the attribute information
   district_gdf.head()

   # view the geometry
   district_gdf.plot()

   # view the coordinate reference system
   district_gdf.crs

   # set the coordinate reference system
   district_gdf.crs="EPSG:4326"


|


If you want to reproject the data into a different coordinate system, you  need to use .to_crs() method and specify the coordinate system we want to convert the data to.

.. code-block:: python
    
   import geopandas
   import maplotlib
   district_gdf = geopandas.read_file("/Users/.../school_district.shp", encoding='utf-8')

   # view the coordinate reference system
   district_gdf.crs

   # reproject the coordinate system to another coordinate system
   district_utm_gdf = district_gdf.to_crs("EPSG:32643")
  
   # view the reprojected geometry
   district_utm_gdf.plot()


