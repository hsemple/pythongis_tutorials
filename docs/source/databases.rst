

Database Interaction and SQL
=============================


|

In this module, we will lean how to connect Python with databases using libraries like SQLite3 or SQLAlchemy.  We will also focus on understanding SQL basics for querying and manipulating data in databases.



|

Here are two sample scripts that demonstrate how to connect Python with databases using SQLAlchemy. The first script shows how to connect to a SQLite database, and the second script demonstrates connecting to a MySQL database.

|

Connecting to a SQLite Database using SQLAlchemy:
-----------------------------------------------------

.. code-block:: python

	from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

	# Create an engine to connect to the SQLite database
	engine = create_engine('sqlite:///example.db')

	# Create a metadata object
	metadata = MetaData()

	# Define a table schema
	users = Table('users', metadata,
	              Column('id', Integer, primary_key=True),
	              Column('name', String),
	              Column('age', Integer))

	# Create the table in the database (if it doesn't exist)
	metadata.create_all(engine)

	# Perform database operations
	with engine.connect() as conn:
	    # Insert data into the table
	    conn.execute(users.insert().values(name='John', age=25))
	    conn.execute(users.insert().values(name='Alice', age=30))

	    # Retrieve data from the table
	    select_query = users.select()
	    result = conn.execute(select_query)
	    for row in result:
	        print(row['name'], row['age'])



In this script, SQLAlchemy is used to create an engine that connects to a SQLite database. The create_engine() function is called with the connection URL to establish the connection. We define a table schema using SQLAlchemy's Table and Column classes. The metadata.create_all(engine) line creates the table in the database if it doesn't exist. We then perform database operations using the connection object (conn).


|




Connecting to a MySQL Database using SQLAlchemy:
------------------------------------------------

.. code-block:: python

	from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

	# Create an engine to connect to the MySQL database
	engine = create_engine('mysql+pymysql://username:password@host/database_name')

	# Create a metadata object
	metadata = MetaData()

	# Define a table schema
	users = Table('users', metadata,
	              Column('id', Integer, primary_key=True),
	              Column('name', String),
	              Column('age', Integer))

	# Create the table in the database (if it doesn't exist)
	metadata.create_all(engine)

	# Perform database operations
	with engine.connect() as conn:
	    # Insert data into the table
	    conn.execute(users.insert().values(name='John', age=25))
	    conn.execute(users.insert().values(name='Alice', age=30))

	    # Retrieve data from the table
	    select_query = users.select()
	    result = conn.execute(select_query)
	    for row in result:
	        print(row['name'], row['age'])



In this script, SQLAlchemy is used to connect to a MySQL database. The create_engine() function is called with the appropriate connection URL for MySQL. The rest of the script is similar to the SQLite example, where we define the table schema, create the table if it doesn't exist, and perform database operations using the connection object.

Make sure to replace the placeholder values in the connection URLs (username, password, host, database_name) with the actual credentials and connection details for your SQLite or MySQL database.





|

Recommended YouTube Videos:
----------------------------

* Corey Schafer's Python SQLite Database: https://youtu.be/pd-0G0MigUA
* Corey Schafer's Python SQLAlchemy Tutorial: https://youtu.be/eXfDB6n_xO0