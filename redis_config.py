import redis
import os
from dotenv import load_dotenv

load_dotenv()
# connects to external redis database server on redislabs.com
DATABASE_URL = os.getenv('DATABASE_URL')
SERVER_PORT = os.getenv('SERVER_PORT')
DATABASE_PSWD = os.getenv('DATABASE_PSWD')

r = redis.Redis(host=DATABASE_URL,
                port=SERVER_PORT, password=DATABASE_PSWD, db=0, decode_responses=True)
