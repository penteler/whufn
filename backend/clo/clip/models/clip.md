### Detailed Explanation (Line by Line)

#### 1. **Importing the `db` instance from the configuration module**
```python
from config import db
```
- **Purpose**: This line imports the `db` object (an instance of `SQLAlchemy`) from a file named `config.py`.
- The `db` object is initialized and configured elsewhere, typically in the `config.py` file, with database settings.
- **Why it matters**: This allows the `Contact` class to use SQLAlchemy for ORM (Object Relational Mapping) to connect with a database.

#### 2. **Defining the `Contact` class as a model**
```python
class Contact(db.Model):
```
- **Purpose**: This line declares a class named `Contact` that inherits from `db.Model`.
- **`db.Model`**: A base class provided by SQLAlchemy to define models (tables in the database).
- The class `Contact` represents a table in the database, and its attributes will map to table columns.

---

### Inside the `Contact` Class

#### 3. **Defining the `id` column**
```python
id = db.Column(db.Integer, primary_key=True)
```
- **Purpose**: This defines a column named `id` in the table.
- **`db.Integer`**: Specifies the column's data type as an integer.
- **`primary_key=True`**: Sets this column as the primary key, meaning it uniquely identifies each row in the table.
- The database will ensure that no two rows have the same `id`, and it often auto-increments the value.

#### 4. **Defining the `first_name` column**
```python
first_name = db.Column(db.String(80), unique=False, nullable=False)
```
- **Purpose**: This creates a column named `first_name` to store text data.
- **`db.String(80)`**: Limits the string length to 80 characters.
- **`unique=False`**: Allows multiple rows to have the same `first_name` (not enforced as unique).
- **`nullable=False`**: Ensures that this column cannot be left empty (null).

#### 5. **Defining the `last_name` column**
```python
last_name = db.Column(db.String(80), unique=False, nullable=False)
```
- **Purpose**: Similar to `first_name`, this defines a column for the last name.
- **Attributes**: 
  - String length limited to 80.
  - Not unique.
  - Cannot be null.

#### 6. **Defining the `email` column**
```python
email = db.Column(db.String(80), unique=True, nullable=False)
```
- **Purpose**: This creates a column for storing email addresses.
- **`unique=True`**: Ensures that each email address is unique across the table. No two rows can have the same `email` value.
- **`nullable=False`**: Prevents the `email` field from being empty.

---

### `to_json` Method

#### 7. **Defining a `to_json` method**
```python
def to_json(self):
```
- **Purpose**: This method converts an instance of the `Contact` class into a JSON-compatible dictionary.
- JSON (JavaScript Object Notation) is a common format for exchanging data, especially in APIs.

#### 8. **Building the dictionary**
```python
return {
    "id": self.id,
    "firstName": self.first_name,
    "lastName": self.last_name,
    "email": self.email,
}
```
- **Purpose**: This line constructs a dictionary where:
  - `"id"` maps to `self.id` (the value of the `id` column).
  - `"firstName"` maps to `self.first_name`.
  - `"lastName"` maps to `self.last_name`.
  - `"email"` maps to `self.email`.
- **Why it matters**: Converting database objects to JSON format is useful for sending data in APIs or rendering it in a frontend application.

---

### Summary
1. **`from config import db`**: Imports the database object for defining models.
2. **`class Contact(db.Model)`**: Defines the table `Contact`.
3. **Columns**:
   - `id`: Primary key, integer.
   - `first_name`: Non-unique, non-nullable string.
   - `last_name`: Non-unique, non-nullable string.
   - `email`: Unique, non-nullable string.
4. **`to_json` Method**: Converts a `Contact` object to a JSON-friendly dictionary format.

This structure makes it easy to interact with the database using SQLAlchemy, ensuring clear definitions of table columns and a straightforward way to serialize objects into JSON.