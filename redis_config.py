import redis
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
SERVER_PORT = os.getenv('SERVER_PORT')

r = redis.Redis(host=DATABASE_URL,
                port=SERVER_PORT, db=0, decode_responses=True)
