# Description of the Project
This is a Flask app that allows users to register, login, and create notes.

The create_app() function in __init__.py initializes a Flask app, sets up the database, and registers the blueprints for the views and auth functionality.

The views blueprint in views.py handles requests related to creating and deleting notes, and renders the main page where users can view their notes.

The auth blueprint in auth.py handles requests related to user authentication, such as logging in and registering new accounts.

The models.py file defines the database schema using SQLAlchemy.

Overall, this code appears to be a good starting point for building a Flask app with user authentication and a database for storing notes. However, there are some improvements that could be made, such as refactoring the code for improved readability, adding input validation to prevent security issues, and implementing tests to ensure the code works as expected.

# UML Class Diagrams and Their Descriptions

In order to draw the UML class diagrams of the project, it is first necessary to determine the relationships of the classes in the project. Below is a summary of the classes included in the project and their relationships:

Flask class: The main class used to launch and manage the Flask application.
SQLAlchemy class: The class used in the Flask implementation for the ORM (Object Relational Mapping) system.
User class: The class that holds the data of the users registered in the application.
Note class: The class that holds the data of user-created notes.
LoginManager class: Class used to manage user login and logout operations.
To draw UML class diagrams, we can use arrows that show the relationships between these classes. Below is a UML class diagram showing the relationships between these classes:

            +-----------------+
            | Flask |
            +-----------------+
            | |
            +-----------------+
                      |
                      |
                      |
            +-----------------+
            | SQLAlchemy |
            +-----------------+
            | |
            +-----------------+
                      |
                      |
                      |
            +-----------------+
            | LoginManager |
            +-----------------+
            | |
            +--------+--------+
                     |
                     |
                     |
            +--------v--------+
            | User |
            +-----------------+
            | -id: int |
            | -username: str |
            | -email: str |
            | -firstname: str |
            | -password: str |
            | -tel: str |
            | |
            | +notes |
            +--------+--------+
                     |
                     |
                     |
            +--------v--------+
            | Note |
            +-----------------+
            | -id: int |
            | -dataNote: str |
            | -datetime: date |
            | -user_id: int |
            +-----------------+
In this diagram, arrows indicate that a class uses or derives from another class. According to the diagram, the Flask class uses the SQLAlchemy class and the SQLAlchemy class uses the User and Note classes. Also, the User class is associated with many Note classes.

# Install
This file indicates that the application has a dependency on the Flask web framework version and that version will be installed. You can store this file in a separate text file and use the command pip install -r requirements.txt to start the application.

# How Do I Run
#!bin/bash
git clone https://github.com/Batuhanaydn/hazard-note-app.git
cd hazard-note-app
pip install -r requirements.txt
python main.py

# Follow Me
<p>You can follow me on my social media accounts below:</p><ul><li>GitHub: <a href="https://github.com/batuhanaydn">Batuhanaydn</a></li><li>Twitter: <a href="https://twitter.com/telumak" target="_new">@telumak</a></li><li>LinkedIn: <a href="https://www.linkedin.com/in/batuhan-aydinn/" target="_new">Muhammed Batuhan Aydın</a></li></ul><p>You can easily access my articles, projects and posts, follow me and stay in touch with me...</p>
