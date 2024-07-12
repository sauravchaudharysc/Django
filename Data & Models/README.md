# Data

Values that we work with in an application can be categorized into three types:

1. **Temporary Data**: 
   - Example: User input to select a blog post.
   - These data are not required in the future and are stored in variables.

2. **Semi-Persistent Data**: 
   - Example: User authentication status.
   - This data is stored for a certain amount of time and is typically stored in browser temporary files.

3. **Persistent Data**: 
   - Example: Blog posts, user profiles.
   - This data must not be lost and should be stored forever. It is stored in a database.

# Databases

### SQL vs NoSQL

1. **SQL Databases**:
   - Stores data in tables.
   - Uses rows and columns.
   - All entries follow the same schema for the entire table.

2. **NoSQL Databases**:
   - Stores data in a document-based format.
   - Uses dictionaries.
   - Two dictionaries can have different fields in the same collection.

These are just ways of storing data, and choosing between them depends on the task at hand. 

Django has great support for SQL databases. For using NoSQL with Django, we need to install additional packages.

# Django Models

Django models allow us to work with data at a higher level, focusing on the data rather than the queries. We define data models (classes in Python) and use objects based on those model classes to run common operations.

Django models translate instructions (written in Python) to SQL queries.

The `models.py` file is used to create Django models and interact with databases. Here, we define data entities and blueprints for data objects.

**Note**: Django automatically creates an `id` column with an auto-incrementing number.

After defining the class in `models.py`, we need to make Django aware of it by registering the app where we defined the model, as Django isn't aware of the app and model implicitly. Follow these steps:

1. **Make Django aware of the app**:
    - Go to the project's `settings.py` file.
    - In the `INSTALLED_APPS` list, add the app name.

2. **Make Django aware of the database changes**:
    - Migrations are a feature that defines the steps to touch the database and manipulate the tables. Whenever we update our models in `models.py`, we need to create migrations and run them.
    - Run the following command at the project level to create new migration files:
      ```bash
      python3 manage.py makemigrations
      ```
        - Purpose: This command is used to create new migration files based on the changes you have made to your models (e.g., adding a new model, modifying fields).
        - Function: It generates a file (or files) in the migrations directory of your app that contains the code needed to apply the changes to the database schema.
        - When to Use: Use this command whenever you have made changes to your models and you want to prepare those changes to be applied to the database.
    - Apply Migrations to the database, update its schema
      ```bash
      python3 manage.py migrate
      ```

# Working with the Database Using Django Shell

This guide provides step-by-step instructions on how to interact with the database using the Django shell.

## Open the Django Shell

**Question:**
How do you open the Django shell to interact with your database?

**Command:**
```bash
python3 manage.py shell
```

## Import the Model

**Question:**
How do you import the `Book` model from the `book_outlet` app in the Django shell?

**Command:**
```python
from book_outlet.models import Book
```

## Create a New Object

**Question:**
How do you create a new `Book` object with the title "Harry Potter 1- The Philosopher's Stone" and a rating of 5?

**Command:**
```python
harry_potter = Book(title="Harry Potter 1- The Philosopher's Stone", rating=5)
```

This commands creates and saves in the same call
```python
Book.objects.create(title="Let us C",author="Yashavant", rating=2, is_bestselling=False)
```
## Save the Object

**Question:**
How do you save the newly created `Book` object to the database?

**Command:**
```python
harry_potter.save()
```
The above command checks if the objects exist it simply updates it. 

## Accessing Attributes of an Object

**Question:**
How do you access the attributes of the `Book` object?

**Command:**
To retrieve and view all `Book` objects:
```python
Book.objects.all()
```

Example output:
```python
<QuerySet [<Book: Harry Potter 1- The Philosopher's Stone (5)>]>
```

To access the rating of the first book in the QuerySet:
```python
Book.objects.all()[0].rating
```

Output:
```python
5
```

To access the title of the first book in the QuerySet:
```python
Book.objects.all()[0].title
```

Output:
```python
'Harry Potter 1- The Philosophers Stone'
```


## Querying & Filtering Data 

**Question:**
How do you retrieve a single `Book` object with the title "Let Us C"?

**Command:**
```python
book = Book.objects.get(title="Let Us C")
```

**Explanation:**
- `Book.objects.get(title="Let Us C")` retrieves the `Book` object where the title exactly matches "Let Us C".
- If no matching object is found, it will raise a `DoesNotExist` exception.
- If more than one matching object is found, it will raise a `MultipleObjectsReturned` exception.

**Example Usage:**
```python
# Retrieve the book
book = Book.objects.get(title="Let Us C")

# Accessing attributes
print(book.title)
print(book.rating)
```

**Output:**
```python
'Let Us C'
<rating_of_the_book>
```

**NOTE:** The get() method retrieves a single object that matches the query. If multiple objects match, as in Book.objects.get(is_bestselling=False), it raises a MultipleObjectsReturned exception, indicating the query is too broad. So we should use unique identifier to access an object using get. 


## Handling Multiple Results with `filter()`

**Scenario Explanation:**

- **Using `get()`:** The `get()` method retrieves a single object that matches the query. If multiple objects match, such as in `Book.objects.get(is_bestselling=False)`, it raises a `MultipleObjectsReturned` exception, indicating the query is too broad.

- **Using `filter()`:** To handle multiple results, use the `filter()` method. For example, `Book.objects.filter(is_bestselling=False)` returns a QuerySet with all `Book` objects where `is_bestselling` is `False`, without raising an exception.

**Example Command:**
```python
books = Book.objects.filter(is_bestselling=False)
```

**Field Lookups:**
- **Field lookups** can be used with `filter()` to specify conditions similar to SQL's `WHERE` clause. For example:
  ```python
  books = Book.objects.filter(rating__lt=5, title__contains="C")
  ```
  This command retrieves all `Book` objects where the rating is less than 5 and the title contains the letter "C".

**Combining Conditions with `Q` Objects:**
- To combine conditions using `OR`, use Django’s `Q` objects. For example:
  ```python
  from django.db.models import Q
  
  books = Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
  ```
  This retrieves all `Book` objects where the rating is less than 3 or the book is a bestseller.

- If you need to combine conditions using `AND` and `OR`, you can use `Q` objects together:
  ```python
  books = Book.objects.filter(Q(rating__lt=3), Q(is_bestselling=True))
  ```
  This retrieves all `Book` objects where the rating is less than 3 and the book is a bestseller.

- If you don’t want to use `Q` for conditions combined with `AND`, you can write them directly:
  ```python
  books = Book.objects.filter(rating__lt=3, is_bestselling=True)
  ```

  
**Note:**
- `filter()` returns a QuerySet, which can contain zero or more objects.
- Unlike `get()`, `filter()` does not raise an exception for multiple results.
- For more information on field lookups, refer to the [Django documentation on field lookups](https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups).

**

