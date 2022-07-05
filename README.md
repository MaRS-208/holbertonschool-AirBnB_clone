# 0x00. AirBnB clone - The console
 Project team members: Manu Ríos Sosa, Ricardo Danta

The goal of the AirBnB clone project is to deploy on our server a simple copy of the AirBnB website, where we will be covering all fundamental concepts of the higher level programming track.

At the en of this project we will have a complete web application composed by:

_ A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
_ A website (the front-end) that shows the final product to everybody: static and dynamic
_ A database or files that store data (data = objects)
_ An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Steps

This application won't be built all at once, but step by step, every step being linked to a concept:

_ The console
_ Web static
_ MySQL storage
_ Web framewor - templating
_ RESTful API
_ Web dynamic
_ Files and Directories

## The console

_ create the data model
_ manage (create, update, destroy, etc) objects via a console / command interpreter
_ store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI that will be build later, there won't be a need to pay attentiont to (take care of) how the objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

### First step: Write a command interpreter to manage your AirBnB objects.
This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

_ put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
_ create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
_ create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
_ create the first abstracted storage engine of the project: File storage.
_ create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
It’s exactly the same as a Shell, but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

_ Create a new object (ex: a new User or a new Place)
_ Retrieve an object from a file, a database etc…
_ Do operations on objects (count, compute stats, etc…)
_ Update attributes of an object
_ Destroy an object

For this purpose, we it is needed to understand and integrate these concepts:

_ Python abstract classes
_ cmd module
_ uuid module
_ datetime
_ unittest module
_ args/kwargs

