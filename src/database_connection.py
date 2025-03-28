import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

dirname = os.path.dirname(__file__)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

os.makedirs(os.path.join(dirname, "..", "data"), exist_ok=True)

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

def get_database_connection():
    """Palauttaa tietokantayhteyden."""
    return connection