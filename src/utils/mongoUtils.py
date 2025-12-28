import os
import logging
from dotenv import load_dotenv

from pymongo import MongoClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

load_dotenv()


def get_mongo_db(database):
  try:
    MONGO_URL = os.getenv("MONGO_URL")
    if not MONGO_URL:
        logger.error("MONGO_URL not found in environment variables.")
        return None
    
    if not database:
        logger.error(f"Invalid database name: {database}")
        return None

    client = MongoClient(MONGO_URL)
    db = client[database]
    return db
  except Exception as e:
    logger.error("Error connecting to MongoDB: {e}")
    return None




