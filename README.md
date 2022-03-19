# cache-mechanism

An implementation of a local cache storage built with the dictionary approach in python. <br/>
This project was built using the Python FastAPI framework and Redis for key-value pair data storage.

# Features

- [x] Built-in Cache Invalidation/expiry
- [x] Set items to local cache memory
- [x] Get items from from local cache memory
- [x] Backup

# Core Requirements

- FastAPI
- Redis

# Methodology

- Caching is basically a process of storing data in a local storage so as to prevent the waste of bandwidth by making multiple requests to a database for the same data over and over again.

- This mechanism uses the dictionary approach where items are fetched from a redis db and stored locally in a python dictionary as key-value pairs. All items stored in the local cache storage expire or are rendered invalid after a stale time of 5 minutes has passed.

- The `get()` method fetches data from the local cache storage if it exists
  
- The `set()` method adds data that has been fetched from the redis db to the local cache storage.
  
- The `backup()` method updates the cache storage with data that may have been added that was perhaps updated through the API endpoint or any different way.

# Project Setup

1. Clone this repo, activate the virtual environment and install the requirements. Make sure you have Python 3.7+ installed.

```bash
git clone git@github.com:buabaj/cache-mechanism.git
cd cache-mechanism
source cache-env/bin/activate
pip install -r requirements.txt
```

2. Set up your redis server and add your database configuration to `redis_config.py`

3. Run code from terminal in your project root directory using:

```bash
python3 app.py
```

4. Head to `localhost:8000/docs` in your browser to test the CRUD Endpoints and documentation in an interactive SWAGGER UI API Documentation playground/