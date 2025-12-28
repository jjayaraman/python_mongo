import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient

from utils import get_mongo_db

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")

logger.debug(f"MONGO_URL: {MONGO_URL}, DB: {MONGO_DB}")

# def get_db():
#   try:
#     client = MongoClient(MONGO_URL)
#     db = client[MONGO_DB]
#     return db
#   except Exception as e: 
#     logger.error(f"Error connecting to MongoDB: {e}")
#     return None
  

def read_todos():
  try:
    db = get_mongo_db(MONGO_DB)
    if db is None:
        return []
    col = db['todos']
    
    # Use list() to consume cursor, .to_list() is async usually or pymongo specific with arguments
    # Standard pymongo find() returns a cursor. list(cursor) is safe for small datasets.
    todos = list(col.find())
    
    logger.info(f"Read {len(todos)} todos")
    logger.debug(f"Todos data: {todos}")
    return todos
  except Exception as e:
    logger.error(f"Error in read_todos(): {e}")
    return None
  
if __name__ == "__main__":
  read_todos()