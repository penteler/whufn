The way I see it there's an instance of the Flask app `app = Flask(__name__)` and theres an instance of the `SQLAlchemy` when they are linked:
```python
db = SQLAlchemy(app)
```
the SQLAlchemy ORM is linked with the Flask application