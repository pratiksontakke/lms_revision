Here are the full lecture notes in Markdown format:

# Human: Technical Note-Taker

## Introduction to FastAPI Framework

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

### Features of FastAPI

* Fast to code: Increase the speed to develop features by about 200% to 300%.
* Fewer bugs: Reduce about 40% of human (developer) induced errors.
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn.
* Short: Minimize code duplication.
* Robust: Get production-ready code with automatic interactive API documentation.
* Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema.

### Basic FastAPI Application Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Run the server:

`uvicorn app:app --reload`
Access the API at `http://127.0.0.1:8000/`.

### FastAPI Routing and Path Parameters

```python
from fastapi import FastAPI
app = FastAPI()

products_db = {
    101: {"name": "Mobile", "price": 19999},
    102: {"name": "Laptop", "price": 39999}
}

@app.get('/products')
def get_products():
    return products_db

@app.get('/products/{product_id}')
def get_product(product_id: int):
    return products_db.get(product_id, "Product not found")
```

### CRUD Operations and HTTP Methods in FastAPI

* GET: Read data
* POST: Create data
* PUT: Update data
* DELETE: Delete data

Example CRUD implementation:

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products_db = {}

@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_product(product: dict):
    new_id = max(products_db.keys(), default=100) + 1
    products_db[new_id] = product
    return {"id": new_id, "product": product}

@app.put('/products/{product_id}')
def update_product(product_id: int, product: dict):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[product_id] = product
    return {"status": "updated"}

@app.delete('/products/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    if product_id in products_db:
        del products_db[product_id]
        return
    raise HTTPException(status_code=404, detail="Product not found")
```

### HTTP Exception Handling and Status Codes in FastAPI

* Raise exceptions that return specific status codes and error messages to the client.

Common HTTP status codes:

* 200 OK: Successful GET or PUT
* 201 Created: Resource successfully created (POST)
* 204 No Content: Successful deletion with no response body
* 404 Not Found: Resource not found

Example:

```python
from fastapi import HTTPException, status

@app.get('/products/{product_id}')
def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return products_db[product_id]
```

### Pydantic for Data Validation and Parsing in FastAPI

* Define models by extending `BaseModel` and automatically validates incoming data, returning clear errors if validation fails.

Example of a Pydantic model for User:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

### Python Virtual Environment

* A virtual environment is an isolated Python environment that allows multiple projects to have their own dependencies, regardless of what dependencies every other project has.

Creating a virtual environment:

`python3 -m venv project_env`
Activating the virtual environment:

(Linux/macOS) `source project_env/bin/activate`
(Windows) `project_env\Scripts\activate`

After activation, any Python package installed via pip only affects this environment.