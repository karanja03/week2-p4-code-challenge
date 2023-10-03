# Heroes and Superheroes API

This is a Flask-based web application that serves as an API for managing heroes, superheroes, their powers, and related information. The application uses SQLAlchemy for database management and Marshmallow for serialization/deserialization of data.

## GETTING STARTED

These instructions will help you set up and run the application on your local machine.

## PREREQUISITES

Before you begin, make sure you have the following installed:

1. Python (version 3.x)
2. Flask
3. Flask-SQLAlchemy
4. Flask-Migrate
5. Flask-RESTful
6. SQLAlchemy
7. Marshmallow


## INSTALLATION

1. Clone the repository to your local machine:

    git clone https://github.com/karanja03/week2-p4-code-challenge$ .git

2. Change to the project directory:

    cd week2-p4-code-challenge$ 

3. Create a virtual environment (optional but recommended):
 
            python -m venv venv

4. Activate the virtual environment:
      source venv/bin/activate

5. Install the project dependencies:
       
       pip install -r requirements.txt


## CONFIGURATION

1. Modify the database URI in the config.py file to suit your database setup:
       app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # Example SQLite URI
   
   You can change the URI to use other database engines like PostgreSQL, MySQL, or SQL Server if needed.


   Create the database tables by running the following commands:

            flask db init
            flask db migrate
            flask db upgrade
## Running the Application
To run the application, execute the following command:

python run.py
The application should now be running on http://localhost:5555. You can access the API endpoints using tools like curl or Postman.

## API Endpoints
This API provides endpoints for managing heroes, superheroes, powers, and their relationships. Here are some of the available endpoints:

1. GET /heroes: Get a list of all heroes.
2. GET /heroes/{id}: Get details of a specific hero by ID.
3. POST /heroes: Create a new hero.
4. PUT /heroes/{id}: Update details of a specific hero by ID.
5. DELETE /heroes/{id}: Delete a hero by ID.
Similar endpoints are available for superheroes, powers, and their relationships.

## Data Serialization
This application uses Marshmallow for data serialization. Serialization schemas are defined in the schemas.py file. You can customize these schemas as needed to format API responses.

## Contribution
Feel free to contribute to this project by creating issues, suggesting improvements, or sending pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.







