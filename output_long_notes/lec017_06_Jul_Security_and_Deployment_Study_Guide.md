Here are the full lecture notes in Markdown format:

**Human:**
You are a world-class technical note-taker trained to convert full lectures into complete notes.

### Defining Database Models with SQLAlchemy ORM

Each class inheriting from the Base declarative base corresponds to a table.
Columns are defined as class attributes using SQLAlchemy's Column function specifying datatypes and constraints.
Primary keys and indexes can be specified.
Relationships (one-to-many, many-to-many) between tables can be established using relationship() and foreign keys.

Example: One-to-many relationship between User and Item:

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    items = relationship('Item', back_populates='owner')

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='items')
```

### Authentication and Authorization Using JWT

Authentication verifies who the user is, while authorization determines what the user can access.

Workflow:

1. User logs in with credentials.
2. Server validates credentials and creates a JWT access token signed with a secret key.
3. Client stores token and sends it with every API request in the Authorization header.
4. Server verifies token to authenticate the request.
5. Tokens typically have expiry times after which the user must re-authenticate.

Example: Creating and verifying JWT token and hashing password

```python
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
hashed_password = pwd_context.hash("plain_password")

# Verify password
pwd_context.verify("plain_password", hashed_password)

# Create JWT Token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode & verify JWT Token (in a dependency)
try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
except JWTError:
    raise credentials_exception
```

### Managing CORS (Cross-Origin Resource Sharing)

CORS is a security feature enforced by browsers that controls requests coming from different origins (domains or ports).

If your frontend runs on one origin (e.g., localhost:3000) and backend on another (e.g., localhost:8000), the browser checks CORS policy.

Backend must explicitly allow frontend origins; otherwise, requests get blocked with CORS errors.

Handling CORS in FastAPI: Use FastAPI's CORS middleware to allow specific origins:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Rate Limiting to Prevent Abuse

Rate limiting restricts the number of requests a user or IP can make within a timeframe.

Prevents server overload and denial-of-service due to excessive requests.
Protects against malicious bots that flood the server with requests.

Implementation in FastAPI:

Middleware or third-party libraries can be used to enforce rate limits.

Example limit: 20 requests per minute per IP.

Example (conceptual):

```python
@app.post("/items")
@limiter.limit("20/minute")
def create_item(...):
    # function body
```

### Global Error Handling in FastAPI

Instead of duplicating error handling logic across multiple endpoints, FastAPI supports central/global error handling.

Define a global exception handler to capture and respond to specific exceptions (e.g., 500 Internal Server Error).

Example:

```python
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error. Please try again later."},
    )
```

### Deploying FastAPI Applications

Deployment involves making your FastAPI application accessible publicly.

Push your project code to a git repository (e.g., GitHub).
Use deployment platforms like Render.com that allow deploying applications from GitHub with minimal setup.

Typical steps:

1. Create a new web service on Render.com
2. Connect your GitHub repository
3. Set build and start commands (e.g., uvicorn main:app --host 0.0.0.0 --port 8000)
4. Provide environment variables such as secret keys if needed
5. Deploy and get a public URL for your app
6. You can update deployed apps by pushing code changes and redeploying.

### Best Practices: Environment Variables and Logging

Environment Variables:

Sensitive information like API keys and secret keys should never be hardcoded or pushed to version control.
Use .env files and libraries like python-dotenv to manage environment variables locally.
Production platforms (e.g., Render) allow setting environment variables securely.

Example of .env usage:

```python
SECRET_KEY=supersecretkey123
DATABASE_URL=sqlite:///./test.db
```

Accessing environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
```

Logging and Monitoring:

Logging provides insights into application behavior and errors.
FastAPI supports logging to monitor incoming requests, errors, and other runtime info.
Analyze logs to detect issues and optimize performance.

Basic logging example:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/items/{item_id}")
def read_item(item_id: int):
    logger.info(f"Fetching item with ID: {item_id}")
    # rest of the function
```

Monitoring request patterns and errors enables better application maintenance.