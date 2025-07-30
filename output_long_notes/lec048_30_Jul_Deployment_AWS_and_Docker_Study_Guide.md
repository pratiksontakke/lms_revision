Here are the full lecture notes in markdown format:

**Introduction to Caching**
==========================

Caching is a technique used to store the results of expensive API calls or database queries so that they don't have to be recomputed every time a request is made. In web applications, especially e-commerce sites, the majority of operations are read operations (e.g., fetching products). Accessing the database repeatedly for these can slow down the application due to database latency. Thus, caching helps by storing frequently accessed data closer to the application to reduce latency and improve performance.

**Types of Caching: In-Memory Cache vs Redis Cache**
---------------------------------------------------

### In-Memory Cache

Stores cache data directly in the RAM of the server where the application is running. It is faster but the cache is lost if the server restarts or crashes, and it consumes server memory.

Example:
```python
from cachetools import TTLCache
cache = TTLCache(maxsize=100, ttl=300)
```

### Redis Cache

Redis is an external, in-memory data store which can be used as a distributed cache. It persists independently of the application server, so the cached data survives restarts and is shared across multiple instances.

Example:
```python
import aioredis
redis = await aioredis.from_url("redis://localhost:6379")
```

**Caching Algorithms**
----------------------

### Least Recently Used (LRU) Cache

Removes the cache entries which have not been accessed recently.

### Time To Live (TTL) Cache

Cache entries live for a specified time and get expired after that.

### Least Frequently Used (LFU) Cache

Removes entries which are used the least number of times.

Example:
```python
from cachetools import TTLCache
cache = TTLCache(maxsize=100, ttl=300)  # max 100 items, live for 5 minutes
```

**Implementing Caching in FastAPI using Cachetools**
---------------------------------------------------

FastAPI applications can utilize caching by manually implementing cache logic using libraries like cachetools. You typically generate unique cache keys based on the API operation and parameters (e.g., get_book:123), check the cache before querying the database, and store the results back to cache after the query.

You must clear the cache upon any data modification (create, update, delete) to avoid stale data.

Example:
```python
from cachetools import TTLCache
cache = TTLCache(maxsize=100, ttl=300)

# Generate cache key
def make_cache_key(operation: str, *args):
    return operation + ":" + ":".join(str(arg) for arg in args)

@app.get("/books/{book_id}")
def get_book(book_id: int):
    key = make_cache_key('get_book', book_id)
    if key in cache:
        return cache[key]  # cache hit
    book = db.get_book(book_id)  # hypothetical db call
    cache[key] = book
    return book

@app.post("/books")
def create_book(book: Book):
    db.create_book(book)
    clear_book_cache()

Clearing Cache on Data Mutations
---------------------------------

Whenever there is a mutation operation like create, update, or delete, the cache related to that data must be cleared or invalidated so the cache does not serve stale data.

Example:
```python
def clear_book_cache():
    keys_to_remove = [key for key in cache.keys() if key.startswith('get_book') or key.startswith('list_books')]
    for key in keys_to_remove:
        cache.pop(key, None)

@app.post("/books")
def create_book(book: Book):
    db.create_book(book)
    clear_book_cache()  # clear cache on create
```

**Using Redis for Caching in FastAPI**
--------------------------------------

Redis caching can be integrated with FastAPI using libraries like fastapi-cache which provide decorators and utilities to cache API responses easily. The Redis server is separate from the application server and runs independently.

To use Redis in FastAPI caching:

Connect to Redis server.
Initialize FastAPI cache with Redis backend.
Use decorators to cache responses with namespaces and TTL.
Clear cache namespaces when data updates.

Example:
```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import aioredis

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="bookstore-cache")

@app.get("/books/{book_id}")
@FastAPICache(cache_namespace="books", expire=300)
async def get_book(book_id: int):
    # fetch book from db
    return book

@app.post("/books")
async def create_book(book: Book):
    db.create_book(book)
    await FastAPICache.clear(namespace="books")  # clear redis cache
```

**Introduction to Queues and Celery**
--------------------------------------

Queues are used to manage and decouple tasks between systems running at different speeds. For example, sending emails can be slow, and doing it synchronously blocks the main application. Queues allow the application to offload these tasks to background workers asynchronously.

Celery is a popular distributed task queue for Python, which works with brokers like Redis. The main application sends tasks to the queue (broker), and workers process these tasks in the background.

Example:
```python
from celery import Celery

celery_app = Celery('worker', broker='redis://localhost:6379/0')

@celery_app.task
def send_email(to_email):
    # code to send email
    pass

# In FastAPI route
@app.post("/signup")
def signup(user: User):
    # Create user
    send_email.delay(user.email)  # Queue email task
    return {"message": "User created"}
```

**How Celery and Redis Work Together**
-----------------------------------------

FastAPI application puts tasks (e.g., send email) into Redis queue via Celery. Celery workers listen to Redis, pick up tasks, and process them asynchronously. This reduces response time and lets the main application focus on serving HTTP requests without being blocked by time-consuming operations.

Example flow:

User signs up.
FastAPI puts send email task into Redis queue using send_email.delay().
Celery worker fetches task from Redis and executes.
Email is sent without blocking the signup response.

Diagramatic flow:
```mermaid
graph LR
    FastAPI(Enqueue task) -->|Redis Queue|> Redis
    Redis -->|Consume|> Celery Worker
    Celery Worker -->|Process Task|> Email Sent
```

I hope this helps! Let me know if you have any questions or need further clarification.