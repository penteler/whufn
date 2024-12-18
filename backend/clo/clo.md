` crud` Create read update delete

`CORS`  Cross Origin Resource Sharing
### In this image
![image](c1.jpg)
1- Imports the flask 
class from the flask module

![image](i1.jpg)

"The `Flask` class is used to
create an instance of a Flask 
application."

2- imports the `SQLAlchemy` 
class from the `flask_sqlalchemy` module

"`Flask-SQLAlchemy` is an extension for 
Flask that adds support for SQLAlchemy, 
a SQL toolkit and Object-Relational Mapping (ORM) 
system for Python.
The SQLAlchemy class is used to interact with the 
database and perform operations such as querying, 
inserting, updating, and deleting data."

3- "This line imports the `CORS` class from the `flask_cors` module. `Flask-CORS` is an extension for Flask that handles Cross-Origin Resource Sharing (CORS), making it possible to make cross-origin AJAX requests.
  - The `CORS` class is used to enable CORS support in the Flask application, allowing resources to be accessed from different domains."

5- This how you initialize an instance of a flask app using the `Flask` class
and assign it as a value to 
a variable which is `app` in this case.

![image](c2.jpg)

`__name__` is a kind of "variable in Python which is set to the name of the module in which it is used.
When a script is run directly, `__name__` is set to `'__main__'`"
"The Flask instance `app` is the central object of the application, and it will be used to configure the app and register routes"

6- `CORS(app)`
Enables CORS (Cross Origin Resourse sharing) for the entire app.
Here `CORS` is the class that was imported and the argument is the
 `app` varable. As you know from line 5 `app` is the flask app instance 
`Flask(__name__)`
 
8-
A configuration variable of the flask app is being set to the URI of the database. `SQLALCHEMY_DATABASE_URI` is a key 
in the app's configuration dictionary and we are using it to specify the location and type of database. Flask SQLAlchemy 
will determine the type and location of the database using this key.
![image](c3.jpg)
As you can see the path to a sqlite database is being passed as a
 string. In this URI you can see the type of database which is 
sqlite and the rest of the path will include the name.

9- Another app configuration key takes in a boolean as a value
![image](c4.jpg)
This is clearly setting the `["SQLALCHEMY_TRACK_MODIFICATIONS"]` 
to `False`

11- `db = SQLAlchemy(app)`
An instance of sqlalchemy being initialised 
with the flask app instance `app` and assigned to the 
variable `db`
### Models
In the last line of your **configuration module** `config.py` an instance of the `SQLAlchemy` class was created so now in `models.py` we can import that object: 
```python
from config import db
```
In this module `db` has already been configured as an instance of SQLAlchemy linked to an instance of a Flask app. Using the `app` variable wich has been further configured using configuration variables using configuration dictionary keys setting them to string or boolean values and enabling `CORS` for the app.
Now the classes in this app can connect with the database using `db`.
# class Contact
2- Declaring a class named `Contact` that inherets from `db.Model`:
---
```python
class Contact(db.Model):
```
"- **`db.Model`**: A base class provided by SQLAlchemy to define models (tables in the database)."
"by inhering from this base class Contact becomes a model that SQLAlchemy can map to a database table." so you're defining a model to map out a database table.
The `class Contact` in itself represents a table in the database and it's **attributes** will be used to map out its columns so here we have defined the `Contact` as a model/table in the database. Of course this is only the first line of its definition.

In the `Contact` class we will define a column named `id` as the primary key 
---
```python
id = db.Column(db.Integer, primary_key=True)
```
`db.Column` is a function that has been provided by SQLAlchemy to define table columns. The data type of the primary key is usually Integer and this integer can be used to uniquely identify every row so we can imagine this as a sequence of numbers in a column with every row being assigned a unique number which would serve as its `primary_key`. The database will automatically increase this integer and will never allow these to match. I think we might end up having a key value pair here.

Creating a `first_name` Column for storing text:
---
```python
first_name = db.Column(db.String(80), unique=False, nullable=False)
```
the `first_name` Column definition contains the data type which is `String` and I think a character limit of `(80)` it isn't `unique` or `nullable` so this Column can contain the same name twice but it wont have any empty cells to ensure that every row has an entry in the column containing `first_name`s you can pass in parameteres of the `db.Column` function to specifiy the data types, constraints and behaviors.

Another compulsory entry column for `last_name`
---
```python
last_name = db.Column(db.String(80), unique=False, nullable=False)
```
the attributes are passed in as function parameters same as before and they're exatly the same. Can't be left empty, entries don't have to be unique and the string length is `(80)` Same as above.

Now you have `email`:
---
```python
email = db.Column(db.String(80), unique=True, nullable=False)
```
and again it only differs in terms of it's uniqueness because we can't have matching emails

# `to_json` Method
Defining a `to_json` method to convert any instance of the `Contact` class into a json compatible dictionary. Javascript Object Notation a common format to exchange data, especialy in APIs.
---
```python
def to_json(self):
```
the way I see it we've got the `def` keyword the name of the method `to_json` and a parameter list which contains `(self):`

building the dictionary:
---
```python
return {
    "id": self.id,
    "firstName": self.first_name,
    "lastName": self.last_name,
    "email": self.email,
}
```

