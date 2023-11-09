import os
from dotenv import load_dotenv
import pyodbc

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
server = os.getenv("server")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")


# Create a function to establish the database connection
def get_database_connection():
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}; Trusted_Connection=yes'
    )
    return conn
