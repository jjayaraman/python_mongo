import os
import logging
from typing import List, Dict, Any, Optional
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB = os.getenv('MONGO_DB')

def get_db_connection() -> Optional[Any]:
    """Establishes and returns a connection to the MongoDB database."""
    if not MONGO_URL:
        logging.error("MONGO_URL not found in environment variables.")
        return None
    if not MONGO_DB:
        logging.error("MONGO_DB not found in environment variables.")
        return None

    try:
        client = MongoClient(MONGO_URL, tls=True, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        logging.info("Successfully connected to MongoDB.")
        return client[MONGO_DB]
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        return None

def read_todos() -> List[Dict[str, Any]]:
    """Reads and returns all todos from the database."""
    db = get_db_connection()
    if db is None:
        return []

    try:
        todos_cursor = db['todos'].find()
        todos_list = list(todos_cursor)  # Consuming cursor into a list
        logging.info(f"Retrieved {len(todos_list)} todos.")
        return todos_list
    except Exception as e:
        logging.error(f"Error reading todos: {e}")
        return []

if __name__ == "__main__":
    todos = read_todos()
    print('Todos:', todos)
