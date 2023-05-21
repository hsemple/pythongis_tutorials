Basic Concepts in Object Oriented Programming
===========================================================

|

Much of programming these days is dominated by the object oriented programming paradigm.  Therefore, understanding this approach to programming is important for deciphering the many programming libraries you will come across regardless of the object oriented language. 

When working with different object oriented languages, including Python, you will soon notice that they all follow the same style.  For example, they all have classes which serve as templates for producing the objects that represent different aspects of the program. Objects are software elements that are pre-programmed to perform specific actions in predictable ways.  So, much of object oriented programming is knowing the different objects in the library, understanding how these objects are related to each other, instantiating the objects, and manipulating them via code to achieve the goals of the program.

|


What is Object Oriented Programming (OOP)
---------------------------------------------

OOP is a programming methodology or paradigm in which programs are designed using objects. Objects are named features or elements of the program that carry out specfic tasks.  Objects may interact with each other in specified ways as they to carry out their tasks. 

The first step in understanding an object oriented program is to identify the main objects in the program and how they relate to each other. This information is typically contained in a class diagram, or it may appear as simple descriptions in the program documentation.  Once objects are identified, they can be manipulated based on the published methods provided in the program documentation.


If a person is writing an object-oriented program, the approach is basically the same. They must define all the objects that will appear in the program and then group them into classes. They must also identify relationships and responsibilities of the different objects, and also identify attributes (Data) and operations (methods) for each object. This process is called object modeling. Once this process is completed, then code can be written to implement the ideas in the program.  Below, we go into further details about basic concepts in object oriented programming.

 

|


Classes 
---------

Classes are generalizations that define the kinds of data a particular type of objects may contain and the logic sequences that can be used to manipulate them. In general,  we use classes as templates or blueprints for creating objects.

To create a class, we must first define the actions and characteristics of the objects that will be created.  In the example below, we are building a program that simulates how `elephants <https://www.wwf.org.uk/learn/fascinating-facts/elephants>`_ behave in the wild. The goal is to highlight three of the many classes that could appear in the program. The three classes are the animal class, the mammal class and the elephant class.  

The animal class defines behavior (methods) and characteristics (properties) that all animals will have in the program, not just elephants.  For animals that are mammals, a class has been defined that specifies things that mammals can do (methods) within the program. Since mammals are also animals, they will also inherit all the features contained in the animal class.  Finally, an elephant class has been defined to specify all the things that only elephants can do within the program.


.. image:: img/classes_and_methods.png
   :alt: Classes and Methods



Typically, class diagrams are not drawn in the informal way shown above. Rather, specific conventions are used to ceate these diagrams.  An example is shown below where the diagram is drawn using UML notation.  `Microsoft Visio <https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software>`_ is a popular tool to use to create class diagrams. A good free tool to use is `Dia <http://dia-installer.de/>`_ . 


.. image:: img/uml_class_diagram.png
   :alt: UML Class Diagram



In addition to creating a class diagram, programmers write code to implement the various classes in a program. The illustraton below shows the code for creating the various classes in the program. As you ca see, tne code is actually a set of functions.

.. code-block:: python

    class Animals():
        def __init__(self, name, species, gender): 
            self.name = name 
            self.species = species 
            self.gender = gender 

        def getName(self): 
            return self.name 

        def getSpecies(self): 
            return self.species 

         def getGender(self): 
            return self.gender
        
        def breathe(self): 
            print('I am breathing') 
          
        def moving(self):
            print('I am moving') 

        def eat(self): 
            print('I am eating') 
            

    class Mammals(Animals): 
        def feed_young_with_milk(self):
           print('I am feeding my young') 

        def play(self):
           print('I am playing') 


        def dancing(self):
           self.moving() 
           self.moving(()   
           self.moving(()  
           self.moving(() 



    class Elephant (Mammals): 

        def spraying_water (self):
           print('I am spraying water on my body using my trunk') 

        def trumpet (self):
           print('I am trumpeting')



In the example above, the animal class has a function called __init__().  This function is executed when the class is being initialized, i.e., when a new object is being created from the class.  

The __init__() function is used to assign values to object properties, or other operations that are necessary when the object is being created.  In object oriented programming, the "__init__" method  is called called a constructor. 


Notice also that each function within the class has a self parameter that is passed to it. In the first function, the self parameter is passed along with other parameters that the user will supply. In the other functions, only the self parameter is passed.  The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.  It does not have be named self. You can call it whatever you like, but it is typically called self.  Self has to be the first parameter of any function in the class. 


To tell Python that a class is a child of another class, we add the name of the parent class in parentheses after the name of our new class. See this link
for more information.


To run the above code, simply copy it and paste it into Python. Once the code runs successfully, nothing will be printed to the screen, however, the class is created and lives in the computer memory.  We are now ready to create giraffe objects from it.



|


Objects
---------

In object-oriented programming, an object is used to simulate real world objects or concrete aspects of the program.  They hold both data, and methods to manipulate the data. The data is usually not visible outside the object, but it can only be changed by using well-specified mechanisms.  The code below shows how we create objects.



**Creating Animal Objects**

.. code-block:: python

    animal1 = Animals('John', 'Tiger', "Male") 
    animal2  = Animals('Luna', 'Lioness', "Female") 



**Creating Elephant Objects**

.. code-block:: python

    elephant1 = Elephant ('Ben', 'Elephant', "Male") 
    elephant2  = Elephant ('Mary', 'Elephant', "Female") 


|

Attributes
-----------

Attributes are characteristics associated with the object.  Normal attributes are introduced in the  __init___ method, but some attributes of a class are shared by all instances and are introduced at the class level.  In the example above, self.name = name and self.species = species are attributes.

 

When getting an attribute, we write the object name followed by a dot and and the name of the attribute, e.g.


.. code-block:: python

    elephant1.name
    'Ben'



We can also set an attribute by calling the object and supplying an attribute value, for example, 

.. code-block:: python

    elephant1.name = "Ben"
    elephant1.name

    'Ben'


|


Methods
---------

A method is a function that is defined within a class that represent actions that the object can perform.  Methods have access to all the data contained in the instance of the object.  When calling a method, we write the object name followed by a dot then the name of the method and parentheses. The parentheses differntiates between a method and an attribute e.g.

.. code-block:: python

    elephant1.move()


The parenthesis in the move method means that it is expecting arguments. Even if no argument is supplied, the self keyword is automatically passed. 


|


Encapsulation
----------------

The principle of encapsulation entails that all the properties and methods of an object be kept private and safe from unauthorized interference by other objects.

Encapsulation involves bundling of data with the methods that operate on the data.  In each object we can have both private and public variables and methods. Private variables and methods cannot be called or used by other objects, whereas public ones can.

To explain this, let’s again use a car application example. In a car application, some car attributes such as name of manufacturer, year and model of the car can be made private variables, meaning that they cannot be changed by other objects.  However, variables such as color, registration number, and driver can be made public variables meaning that they can be changed by other objects

Let's look at the public and private methods associated with a list object in Python. Let's create a list named mylist:

.. code-block:: python

   mylist = [1, 3,5]


Now, type the code below to see the attributes and methods associated with the list object. You can use the "dir" command with any Python object:

.. code-block:: python

    dir(mylist)


['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 



The methods that have double underscores in their names are used internally by Python. That's encapsualtion. The other ones can be used publicly. 


|


Abstraction
------------

Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only the usage of it. For example, to use a TV remote control, one doesn't have to learn the details of how pressing a key in the remote control changes the channels internally on the TV.  All a person needs to know is what pressing the various key does to the TV. For example, if you want to control the TV's sound, all you need to do is press either the - key or the + key.  Through the process of abstraction, a programmer can hide many of the technical process or data in an application in order to reduce complexity and increase efficiency.

In programming, abstraction can also be achieved by using abstract classes and methods in our programs.  A class containing one or more abstract methods is called an abstract class.

Abstract methods do not contain any implementation. Instead, all the implementations can be defined in the methods of sub-classes that inherit the abstract class. An abstract class cannot be instantiated, i.e., we cannot create objects for the abstract class


|



Inheritance
------------

Inheritance enables new classes to receive or inherit the properties and methods of existing classes.



Class Inheritance


.. code-block:: python

    class Mammals(object): 
        def feed_young_with_milk(self):
           print('feeding young') 

        def dancing(self):
           self.moving() 
           self.moving() 
           self.moving() 
           self.moving()



    class Animals(Mammals):
        def __init__(self, name, species, gender): 
            self.name = name 
            self.species = species 
            elf.gender = gender

        def getName(self): 
            return self.name 

        def getSpecies(self): 
            return self.species 

         def getGender(self): 
            return self.gender
               
        def moving(self):
            print('I am moving') 

        def eat(self): 
            print('I am eating') 
            

|

*Creating and calling Elephant Objects*

.. code-block:: python

    animal4 = Animals('Tom', 'Giraffe', "Male") 
    animal5  = Animals('Olga', 'Lioness', "Female") 

    #Inheritance
    animal1.feed_young_with_milk()
    animal1.eat_leaves_from_trees()
    animal2.dancing()


|


*Looking up the Methods associated with an Object*

To look up the methods and properties of an object in Python, type the word dir followed by the name of the object in parenthesis. In the example below, we first create a list named mylist, then we issue the "dir" command to get a list of all the methods associataed with this object.


.. code-block:: python

    mylist = [1, 3,5]
    dir(mylist)



['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 


Use the methods that do not have double underscores. The ones with double underscore are used internally by Python.


|


Polymorphism
--------------

Polymorphism means the ability to take various forms. In OOPs, polymorphism means that a child class inheriting a function from a parent class can override the function and give it a new set of rules to follow. 

In the code below,  we have a "Dog" super class and three child classes that inherit from the superclass.  The superclass has a bark function, but some of the child classes have their own bark functions which allows them to bark in ways that are different from the super class.  That's an example of polymorphism at work.


.. code-block:: python

    class Dog:
        def __init__(self, name, age, friendliness):
            self.name = name
            self.age = age
            self.friendliness = friendliness

        def likes_walks(self):
            return True

        def barks (self):
            print ("Wooof", "Woof")


    class Samoyed (Dog):
        def __init__(self, name, age, friendliness):
            super().__init__(name, age, friendliness)


        def barks (self):
            print ("rrrrr", "rrrrr")


    class Poodle (Dog):
        def __init__(self, name, age, friendliness):
            super().__init__(name, age, friendliness)

        def barks (self):
            print ("row row", "row row row")


    class GoldenRetriever (Dog):
        def __init__(self, name, age, friendliness):
            super().__init__(name, age, friendliness)


|



**Practice Programs**

Please complete the exercises at the links below.


1. `Classes and Objects Exercises <https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes>`_

2. `Python Class Exercises  <https://www.w3resource.com/python-exercises/class-exercises/python-class-real-life-problem-1.php>`_

3. `Python Classes and Object Oriented Programming <https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/>`_

4. `Why Object Oriented Programming Matters <https://www.apollotechnical.com/why-object-oriented-programming-matters/?external_link=true>`_


|




Exercises
-----------

1. Complete the exercises under Python Classes and Inheritance at `this site <https://www.w3schools.com/python/exercise.asp?filename=exercise_classes1>`_ 

2. Using the code below, do the following:

* Initialize a dog object and call its various methods

* Create multiple instances of dog objects



.. code-block:: python

    class Dog():
        """A simple attempt to model a dog."""  
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def sit (self):
            print(self.name.title() + " is now sitting.")    


        def roll_over(self):
            """Simulate rolling over in response to a command.""" 
            print(self.name.title() + " rolled over!")



3. The class below can be used to create rectangle objects. Extend the class to also compute 
   | a. the perimeter of objects.
   | b. the diagonal of the rectangle object. Diagonal (d) = √(l² + w²), where 'l' is the length and 'w' is the width of the rectangle. The formula for the diagonal of a rectangle is derived from the Pythagoras theorem.


.. code-block:: python

    class Rectangle():
        def __init__(self, l, w):
            self.length = l
            self.width  = w
        def area(self):
            return self.length  * self.width



4. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the circumference of a circle.



|



Readings
-----------

* `Classes and Objects <https://vimeo.com/110920298>`_
* `Python Class Exercises  <https://www.w3resource.com/python-exercises/class-exercises/python-class-real-life-problem-1.php>`_
* `Measuring Heights from Individual and Paired Images <https://wgbis.ces.iisc.ernet.in/envis/Remote/section114.htm>`_



