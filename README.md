# 0x00. AirBnB clone - The console

![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220706T132852Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dde38c6d2a6ae7982440a650ca2462966c5bfb4452a57b06ef8e669157ed094d)

The goal of the AirBnB clone project is to deploy on our server a simple copy of the AirBnB website, where we will be covering all fundamental concepts of the higher level programming track.

At the end of this project we will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### Steps

This application won't be built all at once, but step by step, every step being linked to a concept:

- The console
- Web static
- MySQL storage
- Web framewor - templating
- RESTful API
- Web dynamic
- Files and Directories

## The console

This project is all about the console:

- create the data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI that will be build later, there won't be a need to pay attentiont to (take care of) how the objects are stored.

This abstraction will also allow us to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

### The first step is to write a command interpreter to manage our AirBnB objects.
This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
It’s exactly the same as a Shell, but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

For this purpose, it is needed to understand and integrate these concepts:

- Python abstract classes
- cmd module
- uuid module
- datetime
- unittest module
- args/kwargs

##Examples:

- **create:** Creates a new instance of _BaseModel_
- **show:** Prints the string representation of an instance based on the class name and id.
- **destroy:** Deletes an instance based on the class name and id
- **all:** Prints all string representation of all instances based or not on the class name.


Project team members: [Manuela Ríos Sosa](https://github.com/MaRS-208), [Ricardo Danta](https://github.com/RicardoDanta)

>>>>>>> c923c22df4a5d80b68029f96e5bf79073d2dcdd5


